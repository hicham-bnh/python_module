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
        return f" Output: {result}"

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
        return f"Output: {result}"
        

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)
    
    def process(self, data: Any):
        count = sum(len(x) for x in data)
        total = len(data.split(" "))
        return f" Processed text: {count} characters, {total} words"
    
    def format_output(self, result: str):
        return f"Output: {result}"

class LogProcessor(DataProcessor):
    pass

if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    num_processor = NumericProcessor()
    text_processor = TextProcessor()

    numeric_data: List = [1, 2, 3, 5, 4]
    text_data = "Hello Nexus World"

    print("Initializing Numeric Processor...")
    print(f"Processing data: {numeric_data}")
    try:
        if (num_processor.validate(numeric_data)):
            print("Validation: Numeric data verified")
        else:
            print("Validation: Numeric data not verified")
        print(f"{num_processor.format_output(num_processor.process(numeric_data))}")
    except Exception as e:
        print(e)
    print("\nInitializing Text Processor...")
    print(f"Processing data: \"{text_data}\"")
    try:
        if (text_processor.validate(text_data)):
            print("Validation: Text data verified")
        else:
            print("Validation: Text data not verified")
        print(f"{text_processor.format_output(text_processor.process(text_data))}")
    except Exception as e:
        print(e)