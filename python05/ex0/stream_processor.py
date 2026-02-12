from abc import ABC, abstractmethod
from typing import Any, List


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
        return (
            isinstance(data, list)
            and all(isinstance(x, (int, float)) for x in data)
        )

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
        return f"Processed text: {count} characters, {total} words"

    def format_output(self, result: str):
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    def validate(self, data):
        return isinstance(data, str)

    def process(self, data):
        return f"Processing data: \"{data}\""

    def format_output(self, result):
        word = result.split(":")
        if word[0] == "ERROR":
            return f"Output: [ALERT] {word[0]} level detected:{word[1]}"
        elif word[0] == "INFO":
            return f"Output: [INFO] {word[0]} level detected:{word[1]}"
        else:
            return "ERROR"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    num_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()

    numeric_data: List = [1, 2, 3, 5, 4]
    text_data = "Hello Nexus World"
    log_data = "ERROR: Connection timeout"

    result_num = num_processor.process(numeric_data)
    result_text = text_processor.process(text_data)
    print("Initializing Numeric Processor...")
    print(f"Processing data: {numeric_data}")
    try:
        if (num_processor.validate(numeric_data)):
            print("Validation: Numeric data verified")
        else:
            print("Validation: Numeric data not verified")
        print(f"{num_processor.format_output(result_num)}")
    except Exception as e:
        print(e)
    print("\nInitializing Text Processor...")
    print(f"Processing data: \"{text_data}\"")
    try:
        if (text_processor.validate(text_data)):
            print("Validation: Text data verified")
        else:
            print("Validation: Text data not verified")
        print(f"{text_processor.format_output(result_text)}")
    except Exception as e:
        print(e)
    print("\nInitializing Log Processor...")
    try:
        print(f"{log_processor.process(log_data)}")
        if log_processor.validate(log_data):
            print("Validation: Log entry verified")
        else:
            print("Validation: Log entry not verified")
        print(f"{log_processor.format_output(log_data)}")
    except Exception as e:
        print(e)
    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")
    try:
        print(f"Result 1: {num_processor.process([1,2,3])}")
        print(f"Result 2: {text_processor.process('helloo wordd')}")
        print(f"Result 3: {log_processor.format_output('INFO: System ready')}")
    except Exception as e:
        print(e)
    print("\nFoundation systems online. Nexus ready for advanced streams.")
