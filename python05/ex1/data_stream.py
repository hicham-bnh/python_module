from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union


class DataStream(ABC):
    def __init__(
            self, stream_id: str,
            stream_type: str,
            stream: str,
            processe: str
    ) -> None:
        self.stream_id: str = stream_id
        self.stream_type: str = stream_type
        self.stream: str = stream
        self.processe: str = processe
        self.count: int = 0
        self.critique: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
            self, data_batch: List[Any],
            criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [data for data in data_batch if criteria in data]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "count": self.count,
            "stream": self.stream,
            "processe": self.processe
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data", "Sensor", "readings")

    def process_batch(self, data_batch: List[Any]) -> str:
        self.critique: int = 0
        result: = self.filter_data(data_batch, "temp")
        result.extend(self.filter_data(data_batch, "humidity"))
        result.extend(self.filter_data(data_batch, "pressure"))
        if result == []:
            return "No data for stream processe"
        total: int = 0
        tmp: float = 0
        avg: float = 0
        for data in result:
            if "temp" in data:
                final = data.split(":")
                tmp += float(final[1])
                if float(final[1]) > 35:
                    self.critique += 1
                total += 1
                self.count += 1
            elif "humidity" in data:
                self.count += 1
            elif "pressure" in data:
                self.count += 1
        if total > 0:
            avg = tmp / total
            return f"{self.count} readings processed, avg temp: {avg:.1f}°C"
        return f"{self.count} readings processed"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(
            stream_id,
            "Financial Data",
            "Transaction",
            "operations"
        )

    def process_batch(self, data_batch: List[Any]) -> str:
        self.critique = 0
        total: int = 0
        op: int = 0
        trans_data = self.filter_data(data_batch, "sell")
        trans_data.extend(self.filter_data(data_batch, "buy"))
        if trans_data == []:
            return "No data for transaction proceese"
        for data in trans_data:
            if "buy" in data:
                result = data.split(":")
                total += int(result[1])
                if int(result[1]) > 300:
                    self.critique += 1
                op += 1
                self.count += 1
            elif "sell" in data:
                result = data.split(":")
                total -= int(result[1])
                op += 1
                self.count += 1
        if total > 0:
            return f"{op} operations, net flow: +{total}units"
        return f"{op} operations, net flow: {total}units"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events", "Event", "events")

    def process_batch(self, data_batch: List[Any]) -> str:
        self.critique = 0
        result = self.filter_data(data_batch, "login")
        result.extend(self.filter_data(data_batch, "error"))
        result.extend(self.filter_data(data_batch, "logout"))
        if result == []:
            return "No data for event processe"
        error: int = 0
        total: int = 0
        for data in result:
            if "error" in data:
                error += 1
                total += 1
                self.count += 1
                self.critique += 1
            elif "login" in data:
                total += 1
                self.count += 1
            elif "logout" in data:
                total += 1
                self.count += 1
        if error > 0:
            return f"{total} events, {error} error detected"
        return f"{total} events"


class StreamProcessor():
    def launch(self, process: DataStream, data: Any) -> None:
        try:
            print(f"Initializing {process.stream_type} stream")
            print(f"Stream ID: {process.stream_id},", end=" ")
            print(f"Type: {process.stream_type}")
            print(f"Processing sensor batch: {data}")
            print(f"Sensor analysis: {process.process_batch(data)}")
        except Exception as e:
            print(f"ERROR : {e}")

    def polymorphic(
            self,
            processdata: List[DataStream],
            data: List[Any],
            filtre: str
            ) -> None:
        if filtre != "High-priority data only":
            for process in processdata:
                try:
                    process.process_batch(data)
                    result = process.get_stats()
                    print(f"- {result['stream']} data:", end=" ")
                    print(f"{result['count']}", end=" ")
                    print(f"{result['processe']} processed")
                except Exception as e:
                    print(f"ERROR: {e}")

        elif filtre == "High-priority data only":
            try:
                alerts = []
                for process in processdata:
                    process.process_batch(data)
                    if isinstance(process, SensorStream) and process.critique:
                        alerts.append(
                            f"{process.critique} critical sensor alerts"
                            )
                    elif (
                        isinstance(process, TransactionStream)
                            and process.critique):
                        alerts.append(f"{process.critique} large transactions")
                    elif isinstance(process, EventStream) and process.critique:
                        alerts.append(f"{process.critique} event errors")
                print("Filtered results:", ", ".join(alerts) if
                      alerts else "No critical data")
            except Exception as e:
                print(f"ERROR: {e}")


if __name__ == "__main__":
    data_test = [
        "temp:40",
        "temp:40",
        "buy:500",
        "sell:150",
        "buy:75",
        "sell:10",
        "login",
        "logout",
        "login"
    ]
    strams = [
        SensorStream("SENSOR_002"),
        TransactionStream("TRANS_002"),
        EventStream("EVENT_002")
    ]
    stream = StreamProcessor()
    s_stream = SensorStream("SENSOR_001")
    t_stream = TransactionStream("TRANS_001 ")
    e_stream = EventStream("EVENT_001")
    s_data = [
        "temp:22.5",
        "humidity:65",
        "pressure:1013"]
    t_data = [
        "buy:100",
        "sell:150",
        "buy:75",]
    e_data = [
        "login",
        "error",
        "logout"
    ]
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    try:
        stream.launch(s_stream, s_data)
    except Exception as e:
        print(f"ERROR: {e}")
    print()
    try:
        stream.launch(t_stream, t_data)
    except Exception as e:
        print(f"ERROR: {e}")
    print()
    try:
        stream.launch(e_stream, e_data)
    except Exception as e:
        print(f"ERROR: {e}")
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface\n")
    try:
        print("Batch 1 Results:")
        stream.polymorphic(strams, data_test, "")
    except Exception as e:
        print(f"ERROR: {e}")
    print()
    print("Stream filtering active: High-priority data only")
    stream.polymorphic(strams, data_test, "High-priority data only")
    print("\nAll streams processed successfully. Nexus throughput optimal")
