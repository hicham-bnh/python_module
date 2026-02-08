class SecurePlant:
    def __init__(self, name: str, height: int, day: int) -> None:
        """
        Initialize a SecurePlant instance.

        Args:
            name (str): Name of the plant.
            height (int): Initial height in centimeters.
            day (int): Initial age in days.
        """
        self.name: str = name
        print(f"Plant creatde: {self.name}")
        self.set_height(height)
        self.set_age(day)

    def set_height(self, value: int) -> None:
        """
        Securely update the height of the plant.

        Rejects negative values.

        Args:
            value (int): New height in centimeters.
        """
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        """
        Securely update the age of the plant.

        Rejects negative values.

        Args:
            value (int): New age in days.
        """
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__day = value
            print(f"Age updated: {value} days [OK]")

    def get_height(self) -> int:
        """
        Get the current height of the plant.

        Returns:
            int: Height in centimeters.
        """
        return self.__height

    def get_age(self) -> int:
        """
        Get the current age of the plant.

        Returns:
            int: Age in days.
        """
        return self.__day

    def get_info(self) -> None:
        """
        Display the current information of the plant.
        """
        print(f"Current plant: {self.name} ({self.__height}cm,", end=" ")
        print(f"{self.__day} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant1: SecurePlant = SecurePlant("Rose", 25, 30)
    print()
    plant1.set_age(-5)

    print()
    plant1.get_info()
