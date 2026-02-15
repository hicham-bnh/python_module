from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional, Union

class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, float, int]]:
        pass

class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.count = 0
        self.total_temp = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.count += len(data_batch)
        self.total_temp += sum(data_batch)
        avg = self.total_temp / self.count
        return f"Sensor analysis: {len(data_batch)} readings processed, avg temp: {avg}°C"

class TransactionStream(DataStream):
    pass


class EventStream(DataStream):
    pass

class StreamProcessor():
    pass