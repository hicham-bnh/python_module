def garden_operations() -> None:
    """
    Demonstrates handling of common Python exceptions using try/except blocks.

    The function tests and catches the following error types:
    - ValueError (invalid integer conversion)
    - ZeroDivisionError (division by zero)
    - FileNotFoundError (missing file)
    - KeyError (missing dictionary key)
    - Multiple exceptions handled together

    Returns:
        None
    """
    print("Testing ValueError...")
    try:
        tmp: int = int('abc')
        print("Caught ValueError: valid literal for int()", tmp)
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("\nTesting ZeroDivisionError...")
    try:
        result: float = 10 / 0
        print(result)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\nTesting FileNotFoundError...")
    try:
        f = open("missing.txt", "r")
        print("File opened correctly")
        f.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("\nTesting KeyError...")
    try:
        ages: dict[str, int] = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
        print(f"Age of Jim: {ages['mobenhab']}")
    except KeyError as e:
        print(f"Caught KeyError: '{e}'")

    print("\nTesting multiple errors together...")
    try:
        first: int = int('abc')
        second: int = 0
        print(f"{first} divided by {second} is {first / second}")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    """
    Runs the garden_operations function to demonstrate different exception
    types and confirms that the program continues running after errors.

    Returns:
        None
    """
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
