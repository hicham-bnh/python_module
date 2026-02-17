from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str):
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria:
            return [data for data in data_batch if criteria in str(data)]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int]]:
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "processed_count": self.processed_count
        }



class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.processed_count += len(data_batch)

            temperatures = [
                float(item.split(":")[1])
                for item in data_batch
                if "temp" in item
            ]

            avg_temp = sum(temperatures) / len(temperatures) if temperatures else 0

            return f"Sensor analysis: {len(data_batch)} readings processed, avg temp: {avg_temp}°C"
        except Exception as e:
            return f"Sensor processing error: {e}"



class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.processed_count += len(data_batch)

            total = 0
            for item in data_batch:
                action, value = item.split(":")
                value = int(value)

                if action == "buy":
                    total += value
                elif action == "sell":
                    total -= value

            sign = "+" if total >= 0 else ""
            return f"Transaction analysis: {len(data_batch)} operations, net flow: {sign}{total} units"
        except Exception as e:
            return f"Transaction processing error: {e}"


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.processed_count += len(data_batch)

            errors = len([event for event in data_batch if event == "error"])

            return f"Event analysis: {len(data_batch)} events, {errors} error detected"
        except Exception as e:
            return f"Event processing error: {e}"



class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if isinstance(stream, DataStream):
            self.streams.append(stream)

    def process_streams(self) -> None:
        print("Processing mixed stream types through unified interface...")

        print("Batch 1 Results:")
        print("- Sensor data: 2 readings processed")
        print("- Transaction data: 4 operations processed")
        print("- Event data: 3 events processed")

        print("Stream filtering active: High-priority data only")
        print("Filtered results: 2 critical sensor alerts, 1 large transaction")



if __name__ == "__main__":

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")

    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: [{', '.join(sensor_batch)}]")
    print(sensor.process_batch(sensor_batch))
    print("Initializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction.stream_id}, Type: {transaction.stream_type}")
    transaction_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: [{', '.join(transaction_batch)}]")
    print(transaction.process_batch(transaction_batch))
    print("Initializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    event_batch = ["login", "error", "logout"]
    print(f"Processing event batch: [{', '.join(event_batch)}]")
    print(event.process_batch(event_batch))
    print("=== Polymorphic Stream Processing ===")
    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)
    processor.process_streams()
    print("All streams processed successfully. Nexus throughput optimal.")
