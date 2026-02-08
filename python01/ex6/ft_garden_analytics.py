from typing import List


class GardenManager:
    total_gardens: int = 0

    class GardenStats:
        """
        Computes statistics for a single garden.
        """

        def __init__(self, garden: "Garden") -> None:
            """
            Initialize statistics for a garden.

            Args:
                garden (Garden): Garden to analyze.
            """
            self.garden: Garden = garden
            self.total: int = 0
            self.total_grow: int = 0
            self.regular: int = 0
            self.flowering: int = 0
            self.prize: int = 0

        def stats(self) -> None:
            """
            Calculate and display statistics about plants in the garden.
            """
            for plant in self.garden.plants:
                if plant.get_type() == "Plant":
                    self.regular += 1
                elif plant.get_type() == "FloweringPlant":
                    self.flowering += 1
                elif plant.get_type() == "PrizeFlower":
                    self.prize += 1
                self.total += 1
                self.total_grow += 1

            print(f"Plants added: {self.total},", end=" ")
            print(f"Total growth: {self.total_grow}cm")
            print(f"Plant type: {self.regular} regular,", end=" ")
            print(f"{self.flowering} flowering,", end=" ")
            print(f"{self.prize} prize flowers")

    def __init__(self) -> None:
        """
        Initialize the GardenManager.
        """
        self.gardens: List[Garden] = []

    def add_garden(self, garden: "Garden") -> None:
        """
        Add a garden to the manager.

        Args:
            garden (Garden): Garden to add.
        """
        self.gardens.append(garden)
        GardenManager.total_gardens += 1

    @classmethod
    def create_garden_network(cls, manager: "GardenManager") -> None:
        """
        Display scores for all managed gardens.

        Args:
            manager (GardenManager): Manager containing gardens.
        """
        print("Garden score -", end=" ")
        garden_nmb: int = 0
        for garden in manager.gardens:
            if garden_nmb > 0:
                print(f", {garden.name}: {garden.get_score()}", end="")
            else:
                print(f"{garden.name}: {garden.get_score()}", end="")
                garden_nmb += 1

        print()
        print(f"Total gardens managed: {cls.total_gardens}")

    @staticmethod
    def height_validation(height: int) -> bool:
        """
        Validate plant height.

        Args:
            height (int): Height to validate.

        Returns:
            bool: True if height is positive.
        """
        return height > 0


class Garden:
    def __init__(self, name: str) -> None:
        """
        Initialize a garden.

        Args:
            name (str): Garden owner name.
        """
        self.name: str = name
        self.plants: List[Plant] = []

    def add_plant(self, plant: "Plant") -> None:
        """
        Add a plant to the garden.

        Args:
            plant (Plant): Plant to add.
        """
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")

    def help_plants_grow(self) -> None:
        """
        Make all plants grow.
        """
        print(f"{self.name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def show_repot(self) -> None:
        """
        Display garden report.
        """
        print(f"=== {self.name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.get_info()

    def get_score(self) -> int:
        """
        Calculate garden score.

        Returns:
            int: Total score.
        """
        score: int = 0
        for plant in self.plants:
            score += plant.height
            if plant.get_type() == "PrizeFlower":
                score += plant.prize
        return score


class Plant:
    def __init__(self, name: str, height: int) -> None:
        """
        Initialize a plant.

        Args:
            name (str): Plant name.
            height (int): Plant height in centimeters.
        """
        self.name: str = name
        self.height: int = height

    def get_info(self) -> None:
        """
        Display plant information.
        """
        print(f"- {self.name}: {self.height}cm")

    def grow(self) -> None:
        """
        Increase plant height by 1cm.
        """
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_type(self) -> str:
        """
        Get plant type.

        Returns:
            str: Type name.
        """
        return "Plant"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        """
        Initialize a flowering plant.

        Args:
            name (str): Plant name.
            height (int): Height in centimeters.
            color (str): Flower color.
        """
        super().__init__(name, height)
        self.color: str = color

    def get_info(self) -> None:
        """
        Display flowering plant information.
        """
        print(f"- {self.name}: {self.height}cm,", end=" ")
        print(f"{self.color} flowers (blooming)")

    def get_type(self) -> str:
        """
        Get plant type.
        """
        return "FloweringPlant"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        """
        Initialize a prize flower.

        Args:
            name (str): Plant name.
            height (int): Height in centimeters.
            color (str): Flower color.
            prize (int): Prize points.
        """
        super().__init__(name, height, color)
        self.prize: int = prize

    def get_info(self) -> None:
        """
        Display prize flower information.
        """
        print(f"- {self.name}: {self.height}cm, {self.color}", end=" ")
        print(f"flowers (blooming), prize points: {self.prize}")

    def get_type(self) -> str:
        """
        Get plant type.
        """
        return "PrizeFlower"


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    alice_garden = Garden("Alice")
    # bob_garden = Garden("Bob")
    # dj_garden = Garden("mobenais")
    manager = GardenManager()
    manager.add_garden(alice_garden)
    # manager.add_garden(bob_garden)
    # manager.add_garden(dj_garden)
    stats = GardenManager.GardenStats(alice_garden)
    oak = Plant("Oak", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sun = PrizeFlower("Sunflower", 50, "yellow", 10)
    # bob_garden.add_plant(sun)
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sun)
    # dj_garden.add_plant(rose)
    print()
    alice_garden.help_plants_grow()
    print()
    alice_garden.show_repot()
    # bob_garden.show_repot()
    print()
    stats.stats()
    print(f"\nHeight validation test: {GardenManager.height_validation(10)}")
    GardenManager.create_garden_network(manager)
