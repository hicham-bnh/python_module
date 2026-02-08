def ft_garden_intro() -> None:
    """
    Entry point of the program.

    Initializes plant information and displays it in a formatted output.
    """
    name: str = "Rose"
    height: int = 25
    age: int = 30

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


def main() -> None:
    ft_garden_intro()


if __name__ == "__main__":
    main()
