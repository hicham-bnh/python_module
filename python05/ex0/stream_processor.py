from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f" output: {result}"

class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(isinstance(x, (int, float)) for x in data)
    
    def process(self, data: Any):
        count = len(data)
        total = sum(data)
        avg = 0.0
        try:
            avg = total / count
        except ZeroDivisionError as e:
            print(e)
        return f"Processed {count} numeric values, sum={total}, avg={avg}"
    
    def format_output(self, result: str):
        return f"output: {result}"
        

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(isinstance(x, (str)) for x in data)
    
    def process(self, data: Any):
        count = len(data)
        total = len(data.split(" "))
        return f" Processed text: {count} characters, {total} words"
    
    def format_output(self, result: str):
        return f"output: {result}"

class LogProcessor(DataProcessor):
    pass

if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")