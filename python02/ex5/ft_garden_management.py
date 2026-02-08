class GardenError(Exception):
    """
    Base exception class for all garden-related errors.
    """
    pass


class PlantError(GardenError):
    """
    Raised when there is an error related to plant data or configuration.
    """
    pass


class WaterError(GardenError):
    """
    Raised when a watering-related problem occurs.
    """
    pass


class PlantHealthError(GardenError):
    """
    Raised when a plant health check fails.
    """

    pass


class GardenManager:
    def __init__(self) -> None:
        """
        Initializes the garden manager with an empty plant collection.
        """
        self.plants: dict[str, dict[str, int]] = {}

    def add_plant(self, name: str, water: int, sun: int) -> None:
        """
        Adds a plant to the garden.

        Args:
            name (str): Name of the plant.
            water (int): Initial water level.
            sun (int): Sunlight level.

        Raises:
            PlantError: If the name is empty or values are invalid.
        """
        if not name:
            raise PlantError("Plant name cannot be empty!")
        elif water < 0 or sun < 0:
            raise PlantError("Water and sun must be positive numbers!")
        else:
            self.plants[name] = {
                "water": water,
                "sun": sun
            }
            print(f"Added {name} successfully")

    def water_plants(self) -> None:
        """
        Waters all plants in the garden.

        Raises:
            WaterError: If there are no plants to water.
        """
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water")
            for plant in self.plants:
                self.plants[plant]["water"] += 1
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self) -> None:
        """
        Checks the health of each plant based on water and sun levels.

        Raises:
            PlantHealthError: If a plant exceeds healthy thresholds.
        """
        for plant in self.plants:
            try:
                water = self.plants[plant]["water"]
                sun = self.plants[plant]["sun"]
                if water > 10:
                    raise PlantHealthError(
                        f"{plant}: Water level {water} is too high (max 10)"
                    )
                print(f"{plant}: healthy (water: {water}, sun: {sun})")
            except PlantHealthError as e:
                print(f"Error checking {e}")


def test_garden_management() -> None:
    """
    Tests the full garden management system, including plant creation,
    watering, health checks, and error recovery.
    """
    print("=== Garden Management System ===")
    print("\nAdding plants to garden...")
    manager = GardenManager()
    for name, water, sun in [
        ("tomato", 4, 8),
        ("lettuce", 14, 6),
        ("", 5, 4)
    ]:
        try:
            manager.add_plant(name, water, sun)
        except PlantError as e:
            print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    try:
        manager.check_health()
    except PlantHealthError as e:
        print(f"Error checking {e}")
    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
