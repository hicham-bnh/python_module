def water_plants(plant_list: list[str]) -> None:
    """
    Waters a list of plants using a simulated watering system.

    The function opens the watering system, iterates over the provided
    plant list, and waters each plant if it is a valid string.
    If an invalid plant is encountered, a ValueError is raised and caught.
    The watering system is always closed using a finally block.

    Args:
        plant_list (List[str]): A list of plant names to water.

    Returns:
        None
    """
    plantes: list = ["tomato", "lettuce", "carrots"]
    error: int = 0
    try:
        print("Opening watering system")
        for plantes in plant_list:
            if not isinstance(plantes, str):
                raise ValueError(f"Cannot water {plantes} - invalid plant!")
            print(f"Watering {plantes}")
    except ValueError as e:
        print(f"Error: {e}")
        error = 1
    finally:
        print("Closing watering system (cleanup)")
    if (error == 0):
        print("Watering completed successfully!")


def test_watering_system() -> None:
    """
    Tests the watering system with valid and invalid plant lists
    to demonstrate error handling and cleanup behavior.

    Returns:
        None
    """
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    plants1: list = ["tomato", "lettuce", "carrots"]
    water_plants(plants1)
    print()
    print("Testing with error...")
    plants2: list = ["tomato", None, "carrots"]
    water_plants(plants2)
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
