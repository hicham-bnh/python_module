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


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialize a Flower instance.

        Args:
            name (str): Name of the flower.
            height (int): Height in centimeters.
            age (int): Age in days.
            color (str): Flower color.
        """
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """
        Simulate the blooming of the flower.
        """
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> None:
        """
        Display detailed information about the flower.
        """
        print(f"{self.name} ({type(self).__name__}): {self.height}cm "
              f"{self.age} days, {self.color} color")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 diameter: int) -> None:
        """
        Initialize a Tree instance.

        Args:
            name (str): Name of the tree.
            height (int): Height in centimeters.
            age (int): Age in days.
            diameter (int): Trunk diameter in centimeters.
        """
        super().__init__(name, height, age)
        self.diameter: int = diameter

    def produce_shade(self) -> None:
        """
        Display the estimated shade area produced by the tree.
        """
        print(f"{self.name} provides {int(self.diameter * 1.56)} "
              "square meters of shade")

    def get_info(self) -> None:
        """
        Display detailed information about the tree.
        """
        print(f"{self.name} ({type(self).__name__}): {self.height}cm, "
              f"{self.age} days, {self.diameter}cm diameter")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest: str,
        value: str
    ) -> None:
        """
        Initialize a Vegetable instance.

        Args:
            name (str): Name of the vegetable.
            height (int): Height in centimeters.
            age (int): Age in days.
            harvest (str): Harvest season.
            value (str): Main nutritional value.
        """
        super().__init__(name, height, age)
        self.harvest: str = harvest
        self.value: str = value

    def nutritional(self) -> None:
        """
        Display nutritional information about the vegetable.
        """
        print(f"{self.name} is rich in vitamin {self.value}")

    def get_info(self) -> None:
        """
        Display detailed information about the vegetable.
        """
        print(f"{self.name} ({type(self).__name__}): {self.height}cm "
              f"{self.age} days, {self.harvest} harvest")


if __name__ == "__main__":
    rose: Flower = Flower("Rose", 25, 30, "red")
    lily: Flower = Flower("Lily", 20, 25, "white")

    oak: Tree = Tree("Oak", 500, 1825, 50)
    maple: Tree = Tree("Maple", 300, 1460, 40)

    tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "C")
    carrot: Vegetable = Vegetable("Carrot", 30, 60, "spring", "B12")

    print("=== Garden Plant Types ===\n")

    rose.get_info()
    rose.bloom()

    print()
    oak.get_info()
    oak.produce_shade()

    print()
    tomato.get_info()
    tomato.nutritional()
