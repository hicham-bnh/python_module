from abc import ABC, abstractmethod
from typing import Dict, List, Any, Optional, Union

class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str):
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return data_batch
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "processed_count": self.processed_count
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "Environmental Data")

    def filter_data(self, data_batch: List[Any],  criteria: Optional[str] = None) -> List[Any]:
        base_filter = [x for x in data_batch if isinstance(x, str)]
        if criteria == "high_priority":
            return [x for x in base_filter if isinstance(x, str) and (x.startswith("temp:") and float(x.split(":")[1]) > 30)]
        return base_filter

    def process_batch(self, data_batch: List[Any]) -> str:
        result: List[Any] = self.filter_data(data_batch)
        temp = None
        for item in data_batch:
            if isinstance(item, str) and item.startswith("temp:"):
                temp = float(item.split(":")[1])
                break
        self.processed_count += len(result)
        if temp is None:
            return f"{len(result)} operations"
        return f"{len(result)} readings processed, avg temp: {temp}°C"
    

class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "Financial Data")

    def filter_data(self, data_batch: List[Any],  criteria: Optional[str] = None) -> List[Any]:
        base_filter = [x for x in data_batch if isinstance(x, str)]
        if criteria == "high_priority":
            return [x for x in base_filter if int(x.split(":")[1]) > 500]
        return base_filter
    def process_batch(self, data_batch: List[Any]) -> str:
        result: List[Any] = self.filter_data(data_batch)
        transaction = 0
        try:
            for item in result:
                if isinstance(item, str) and item.startswith("buy:"):
                    transaction += int(item.split(":")[1])
                elif isinstance(item, str) and item.startswith("sell:"):
                    transaction -= int(item.split(":")[1])
            self.processed_count += len(result)
            if transaction > 0:
                return f"{len(result)} operations, net flow: +{transaction} units"
            return f"{len(result)}  operations, net flow: {transaction} units"
        except Exception as e:
            return f"{e}"


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "System Events")

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        base_filter = [x for x in data_batch if isinstance(x, str)]
        if criteria == "high_priority":
            return [x for x in base_filter if "error" in x]
        return base_filter
        
    def process_batch(self, data_batch: List[Any]) -> str:
        result = self.filter_data(data_batch)
        error = 0
        try:
            for item in result:
                if isinstance(item, str) and item == "error":
                    error += 1
            self.processed_count += len(result)
            return f"{len(result)} evetns, {error} error detected"
        except Exception as e:
            return f"{e}"
        
class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream):
        self.streams.append(stream)

    def process_all(self, batches: List[List[Any]]):
        for stream, batch in zip(self.streams, batches):
            result = stream.process_batch(batch)
            print(f"- {stream.stream_type}: {result}")

    def process_critical_only(self, batches: List[List[Any]]):
        print("\nStream filtering active: High-priority data only")
        results = []
        for stream, batch in zip(self.streams, batches):
            critical_data = stream.filter_data(batch, criteria="high_priority")
            if isinstance(stream, SensorStream):
                results.append(f"{len(critical_data)} critical sensor alerts")
            elif isinstance(stream, TransactionStream):
                results.append(f"{len(critical_data)} large transaction")   
        print(f"Filtered results: {', '.join(results)}")

if __name__ == "__main__":
    process_sensor = SensorStream(" SENSOR_001")
    process_transaction = TransactionStream("TRANS_001")
    process_event = EventStream("EVENT_001")
    data_sensor: List[Any] = ["temp:22.5", "humidity:65", "pressure:1013"]
    data_transaction = ["buy:100", "sell:150", "buy:75"]
    data_event = ["login", "error", "login"]
    batches = [
        ["temp:40.5", "humidity:16"],
        ["buy:100", "sell:150", "buy:75", "sell:1000"],
        ["login", "error", "logout"]
    ]
    sp = StreamProcessor()
    sp.add_stream(process_sensor)
    sp.add_stream(process_transaction)
    sp.add_stream(process_event)
    print("= CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("\nInitializing Sensor Stream...")
    print(f"Stream ID: {process_sensor.stream_id}, Type: {process_sensor.stream_type}")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print("Sensor analysis:",process_sensor.process_batch(data_sensor))
    print("\nInitializing Transaction Stream...")
    print(f"Stream ID: {process_transaction.stream_id}, Type: {process_transaction.stream_type}")
    print("Processing sensor batch: [buy:100, sell:150, buy:75]")
    print("Sensor analysis:",process_transaction.process_batch(data_transaction))
    print("\nInitializing Event Stream...")
    print(f"Stream ID: {process_event.stream_id}, Type: {process_event.stream_type}")
    print("Processing sensor batch: [login, error, login]")
    print("Sensor analysis:",process_event.process_batch(data_event))
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    print("Batch 1 Results:")
    sp.process_all(batches)
    sp.process_critical_only(batches)
    print("\nAll streams processed successfully. Nexus throughput optimal.")



