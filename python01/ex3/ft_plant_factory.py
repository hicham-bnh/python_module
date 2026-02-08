from typing import List


class Plant:
    def __init__(self, name: str, height: int, day: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            height (int): Height in centimeters.
            day (int): Age in days.
        """
        self.name: str = name
        self.height: int = height
        self.day: int = day

    def grow(self) -> None:
        """
        Increase the plant's height by 1 centimeter.
        """
        self.height += 1

    def age(self) -> None:
        """
        Increase the plant's age by 1 day.
        """
        self.day += 1

    def get_info(self) -> None:
        """
        Display creation information about the plant.
        """
        print(f"Created: {self.name} ({self.height}cm, {self.day} days)")


class PlantFactory:
    def create_plant(self, infos_plantes) -> List[Plant]:
        """
        Create a list of predefined plants and display their information.

        Returns:
            List[Plant]: A list of created Plant objects.
        """

        plantes: List[Plant] = []
        for name, height, day in infos_plantes:
            plantes.append(Plant(name, height, day))

        for plante in plantes:
            plante.get_info()

        return plantes


if __name__ == "__main__":
    infos_plantes: List[tuple[str, int, int]] = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]
    factory: PlantFactory = PlantFactory()

    print("=== Plant Factory Output ===")
    plantes: List[Plant] = factory.create_plant(infos_plantes)
    print(f"\nTotal plants created: {len(plantes)}")
