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

    def filter_data(self, data_bstch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        return data_bstch
    
    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "processed_count": self.processed_count
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str, stream_type: str):
        super().__init__(stream_id, "Environmental Data")

    def filter_data(self, data_batch: List[Any]) -> List[Any]:
        return [x for x in data_batch if isinstance(x, str)]

    def process_batch(self, data_batch: List[Any]) -> str:
        result: List[Any] = self.filter_data(data_batch)
        temp = None
        for item in data_batch:
            if isinstance(item, str) and item.startswith("temp:"):
                temp = float(item.split(":")[1])
                break
        self.processed_count+= len(result)
        if temp is None:
            return f"{len(result)} operations"
        return f"{len(result)} readings processed, avg temp: {temp}°C"
    



if __name__ == "__main__":
    process_sensor = SensorStream(" SENSOR_001","Environmental Data")
    data_sensor: List[Any] = ["temp:22.5", "humidity:65", "pressure:1013"]
    print("= CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print("\nInitializing Sensor Stream...")
    print(f"Stream ID: {process_sensor.stream_id}, Type: {process_sensor.stream_type}")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    print("Sensor analysis:",process_sensor.process_batch(data_sensor))
