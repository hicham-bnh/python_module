from typing import Any, List, Protocol
from abc import ABC, abstractmethod


class ProcessingStage(Protocol):
    pass


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        self.stages: List[Any] = []
        self.stats = {
            "runs": 0,
            "errors": 0,
            "total_time": 0
        }

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

class JSONAdapter(ProcessingPipeline):
    pass

class CSVAdapter(ProcessingPipeline):
    pass

class StreamAdapter(ProcessingPipeline):
    def __init__(self) -> None:
        super().__init__()