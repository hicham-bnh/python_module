def check_temperature(temp_str: str) -> None:
    """
    Checks whether a temperature provided as a string is suitable for plants.

    The function attempts to convert the string to an integer and:
    - reports an error if the temperature is too high (> 40°C),
    - reports an error if the temperature is too low (< 0°C),
    - confirms the temperature is ideal otherwise.

    Args:
        temp_str (str): Temperature to check, provided as a string.

    Returns:
        None
    """
    print(f"Testing temperature: {temp_str}")
    try:
        tmp: int = int(temp_str)
        if tmp > 40:
            print(f"Error: {tmp}°C is too hot for plants (max 40°C)")
        elif tmp < 0:
            print(f"Error: {tmp}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {tmp}°C is perfect for plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    """
    Runs a set of tests to verify the behavior of the check_temperature
    function with various valid and invalid inputs.

    Returns:
        None
    """
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    print()
    check_temperature("abc")
    print()
    check_temperature("100")
    print()
    check_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
