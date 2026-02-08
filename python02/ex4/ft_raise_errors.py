def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """
    Checks whether a plant is healthy based on its name, water level,
    and daily sunlight exposure.

    Raises a ValueError if any parameter is outside acceptable limits.

    Args:
        plant_name (str): Name of the plant.
        water_level (int): Water level (must be between 1 and 10).
        sunlight_hours (int): Daily sunlight hours (must be between 2 and 12).

    Returns:
        None
    """
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too hight (max 10)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours}", end=" ")
        print("is too hight (max 12)")
    return print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """
    Tests the check_plant_health function with valid and invalid inputs
    to demonstrate error raising and handling.

    Returns:
        None
    """
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        check_plant_health("tomato", 5, 8)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 8)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
