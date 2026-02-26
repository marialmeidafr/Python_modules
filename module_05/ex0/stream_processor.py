from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self, name: str) -> None:
        self.name: str = name

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return result   string"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """lidate if data is appropriate for this processor"""
        pass

    def format_output(self, result: str) -> str:
        """Format the output string"""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False

        for x in data:
            if not isinstance(x, (int, float)):
                return False
        print("Validation: Numeric data verified")
        return True

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Validation: Numeric data failed")
        count = len(data)
        total = sum(data)
        if count > 0:
            avg = total / count
        else:
            avg = 0.0
        res_num = f"Processed {count} numeric values, sum={total}, avg={avg}"
        return self.format_output(res_num)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False

        print("Validation: Text data verified")
        return True

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Validation: Text data failed")
        count = len(data)
        words = len(data.split())
        res_text = f"Processed text: {count} characters, {words} words"
        return self.format_output(res_text)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str) and ":" in data:
            print("Validation: Log entry verified")
            return True
        return False

    def format_output(self, result: str) -> str:
        if "ERROR" in result:
            tag = "[ALERT]"
        else:
            tag = "[INFO]"
        return f"Output: {tag} {result}"

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Validation: Log entry failed")

        level_raw, content = data.split(':', 1)
        level = level_raw.strip().upper()

        res_log = f"{level} level detected: {content.strip()}"
        return self.format_output(res_log)


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    p_num = NumericProcessor("Numeric Processor")
    p_text = TextProcessor("Text Processor")
    p_log = LogProcessor("Log Processor")

    tests = [
        (p_num, [1, 2, 3, 4, 5]),
        (p_text, "Hello Nexus World"),
        (p_log, "ERROR: Connection timeout")
    ]

    for processor, data in tests:
        print()
        print(f"Initializing {processor.name}...")

        if isinstance(data, str):
            out = f'"{data}"'
        else:
            out = data

        print(f"Processing data: {out}")

        try:
            print(processor.process(data))
        except Exception as error:
            print(f"Status: Breach detected. Error: {error}")

    print()
    print("=== Polymorphic Processing Demo ===")
    print()
    print("Processing multiple data types through same interface...")

    another_tests = [
        (p_num, [2, 2, 2]),
        (p_text, "Hello World!"),
        (p_log, "INFO: System ready")
    ]

    for i, (processor, data) in enumerate(another_tests, 1):
        try:
            raw_result = processor.process(data)
            final_result = raw_result.replace("Output: ", "")
            print(f"Result {i}: {final_result}")
        except Exception as error:
            print(f"Result {i}: Failed. Error: {error}")
    print()
    print("Foundation systems online. Nexus ready for advanced streams.")
