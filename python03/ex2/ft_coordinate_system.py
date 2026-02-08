import math
import sys


def distance(pos1: list, pos2: list) -> float:
    """
    Calculate the Euclidean distance between two 3D positions.

    :param pos1: First position as a list of three integers
    :param pos2: Second position as a list of three integers
    :return: Distance between pos1 and pos2
    """
    return math.sqrt(
        (pos2[0] - pos1[0])**2 +
        (pos2[1] - pos1[1])**2 +
        (pos2[2] - pos1[2])**2
    )


def parsing(string: str, last: int) -> int:
    """
    Parse a coordinate string, create a new position, and compute
    the distance from the origin.

    :param string: Coordinate string formatted as "x,y,z"
    :param last: Index of the last position stored
    :return: Updated index of the last position
    """
    try:
        cordo: list[str] = string.split(",")
        x, y, z = cordo
        position.append((int(x), int(y), int(z)))
        last += 1
        print("Position created:", position[last])
        result = distance(position[0], position[last])
        print(f"Distance between {position[0]} and", end=" ")
        print(f"{position[last]}: {result:.1f}")
    except ValueError as e:
        print("Error parsing coordinates :", e)
        print(f"Error details - Type: ValueError, args: (\"{e}\",)")
    finally:
        return last


if __name__ == "__main__":
    position: list[tuple[int, int, int]] = []
    position.append((0, 0, 0))
    result: float = 0
    last: int = 0
    pos: int = 0
    print("=== Game Coordinate System ===\n")
    position.append((int(10), int(20), int(5)))
    pos += 1
    last += 1
    print("Position created:", position[last])
    result = distance(position[0], position[last])
    print(f"Distance between {position[0]} and", end=" ")
    print(f"{position[last]}: {result:.2f}")
    if (len(sys.argv) < 2):
        print("\nParsing coordinates \"3,4,0\"")
        last = parsing("3,4,0", last)
        print("\nParsing invalid coordinates: \"abc,def,ghi\"")
        last = parsing("abc,def,ghi", last)
    else:
        for coord in sys.argv[1:]:
            print(f"\nParsing coordinates \"{coord}\"")
            last = parsing(coord, last)
    print("\nUnpacking demonstration:")
    print(f"Player at x={position[last][0]}", end="")
    print(f", y={position[last][1]}", end="")
    print(f", z={position[last][2]}")
    print(f"Coordinates: X={position[last][0]}", end="")
    print(f", Y={position[last][1]}", end="")
    print(f", Z={position[last][2]}")
