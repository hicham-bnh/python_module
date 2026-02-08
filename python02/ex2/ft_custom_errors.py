class GardenError(Exception):
    """
    Base exception class for all garden-related errors.
    """
    pass


class PlantError(GardenError):
    """
    Exception raised for plant-related issues.
    """
    pass


class WaterError(GardenError):
    """
    Exception raised for watering-related issues.
    """
    pass


def check_plant() -> None:
    """
    Simulates a plant health check that raises a PlantError.

    Raises:
        PlantError: If the plant is in poor condition.
    """
    raise PlantError("The tomato plant is wilting!")


def water_error() -> None:
    """
    Simulates a watering system failure.

    Raises:
        WaterError: If there is not enough water available.
    """
    raise WaterError("Not enough water in the tank!")


def test_errors() -> None:
    """
    Tests custom garden-related exceptions and demonstrates how to catch
    specific errors as well as a common base error.

    Returns:
        None
    """
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        print("\nTesting WaterError...")
        water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        check_plant()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        water_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
