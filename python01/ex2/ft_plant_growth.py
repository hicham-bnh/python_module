class Plant:
    def __init__(self, name: str, height: int, day: int) -> None:
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            height (int): Initial height in centimeters.
            day (int): Initial age in days.
        """
        self.name: str = name
        self.height: int = height
        self.day: int = day

    def grow(self) -> None:
        """
        Increase the plant's height by 1 centimeter.
        """
        self.height += 1
        self.age()

    def age(self) -> None:
        """
        Increase the plant's age by 1 day.
        """
        self.day += 1

    def get_info(self) -> None:
        """
        Display the current state of the plant.
        """
        print(f"{self.name}: {self.height}cm, {self.day} days old")


if __name__ == "__main__":
    plant1: Plant = Plant("Rose", 25, 30)
    day: int = 6

    print("=== Day 1 ===")
    plant1.get_info()

    for _ in range(day):
        plant1.grow()
        plant1.age()

    print("=== Day 7 ===")
    plant1.get_info()
    print(f"Growth this week: +{day}cm")
