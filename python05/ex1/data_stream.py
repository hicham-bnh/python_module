from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional, Union

class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [x for x in data_batch if isinstance(x, criteria)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "items_processed": self.processed_count
        }

class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        

class TransactionStream(DataStream):
    pass

class EventStream(DataStream):
    pass