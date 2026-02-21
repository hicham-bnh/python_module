from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        pass

    def process(self, data: Any) -> str:
        if self.validate(data):
            count: int = len(data)
            sm: int = sum(data)
            avg: float = (sm / count)
            return f"Processed {count} numeric values, sum={sm}, avg={avg:.1f}"
        else:
            return "Processe error"

    def validate(self, data: Any) -> bool:
        for i in data:
            if not isinstance(i, (int, float)):
                return False
        return True


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        pass

    def validate(self, data: Any) -> bool:
        if "ERROR" in data or "INFO" in data:
            return False
        for c in data:
            if not isinstance(c, str):
                return False
        return True

    def process(self, data: Any) -> str:
        if self.validate(data):
            len_c: int = 0
            word: int = 1
            for c in data:
                len_c += 1
                if c == ' ':
                    word += 1
            return f"Processed text: {len_c}  characters, {word} words"
        else:
            return "Processed text error"


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        pass

    def validate(self, data: Any) -> bool:
        if "ERROR" in data or "INFO" not in data:
            return False
        for c in data:
            if not isinstance(c, str):
                return False
        return True

    def process(self, data: Any) -> str:
        if self.validate(data):
            result = data.split(":")
            if result[0] == "ERROR":
                return f"[ALERT] {result[0]} level detected: {result[1]}"
            elif result[0] == "INFO":
                return f"[INFO] {result[0]} level detected: {result[1]}"
            else:
                return "log error"
        else:
            return "Processed log error"


def get_type(Process: DataProcessor):
    if isinstance(Process, TextProcessor):
        return "Text"
    elif isinstance(Process, LogProcessor):
        return "Log"
    elif isinstance(Process, NumericProcessor):
        return "Numeric"


def launch(process: DataProcessor, data: Any):
    try:
        print(f"Initializing {get_type(process)} Processor...")
        print(f"Processing data: {data}")
        if process.validate(data):
            print(f"Validation: {get_type(process)} data verified")
        else:
            print(f"Validation: {get_type(process)} data not verified")
        print(process.format_output(process.process(data)))
    except Exception as e:
        print(f"ERROR : {e}")


def poly(process: List[DataProcessor], datas: List[Any]):
    try:
        i = 1
        for data in datas:
            for proc in process:
                if proc.validate(data):
                    print(f"Result {i}: {proc.process(data)}")
                    i += 1
    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    data_num: List[int] = [1, 2, 3, 4, 5]
    data_text: str = "Hello Nexus World"
    data_log: str = "ERROR: Connection timeout"
    num_process: NumericProcessor = NumericProcessor()
    text_prcoess: TextProcessor = TextProcessor()
    log_process: LogProcessor = LogProcessor()
    pro_poly: List[DataProcessor] = [num_process, text_prcoess, log_process]
    data_poly: List[Any] = [[1, 2, 3], "123456 123456", "INFO: System ready"]
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    launch(num_process, data_num)
    print()
    launch(text_prcoess, data_text)
    print()
    launch(log_process, data_log)
    print()
    print()
    print("=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")
    poly(pro_poly, data_poly)
    print()
    print("Foundation systems online. Nexus ready for advanced streams.")
