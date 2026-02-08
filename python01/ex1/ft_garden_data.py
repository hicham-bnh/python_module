class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            height (int): Height in centimeters.
            age (int): Age in days.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> None:
        """
        Display formatted information about the plant.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant1: Plant = Plant("Rose", 25, 30)
    plant2: Plant = Plant("Sunflower", 80, 45)
    plant3: Plant = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    plant1.get_info()
    plant2.get_info()
    plant3.get_info()
