def garden_operations(error: str) -> None:
    """error types"""

    if error == "ValueError":
        int("it's not a int")
    elif error == "ZeroDivisionError":
        print(42 / 0)
    elif error == "FileNotFoundError":
        open("missing.txt")
    elif error == "KeyError":
        dictionary = {}
        dictionary["invalid_key"]


def test_error_types() -> None:
    """function to show the different errors"""

    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        garden_operations("ValueError")
    except ValueError as error:
        print(f"Caught ValueError: {error}\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}\n")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}\n")

    print("Testing KeyError...")
    try:
        garden_operations("KeyError")
    except KeyError as error:
        print(f"Caught KeyError: {error}\n")

    print("Testing multiple errors together...")
    error_name: str = "KeyError"
    try:
        garden_operations(error_name)
    except (KeyError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully")


if __name__ == "__main__":
    test_error_types()
