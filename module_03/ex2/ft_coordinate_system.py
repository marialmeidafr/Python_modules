import sys
import math


def main() -> None:
    print("=== Game Coordinate System ===\n")

    check_point: tuple[int, int, int] = (0, 0, 0)
    points: tuple[int, int, int] = (10, 20, 5)
    print(f"Position created: {points}")
    distance: float = math.sqrt((points[0])**2 + (points[1])**2 + (points[2])**2)
    print(f"Distance between {check_point} and {points} : {distance: .2f}")
    print()
    coord: str = "3, 4, 0"
    print(f"Parsing coordinates: \"{coord}\"")
    try:
        x, y, z = coord.split(",")
        new_coord = (int(x), int(y), int(z))
        print(f"Parsed position: {new_coord}")
        dist: float = math.sqrt((new_coord[0])**2 + (new_coord[1])**2 + (new_coord[2])**2)
        print(f"Distance between {check_point} and {new_coord} : {dist: .1f}")
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: ValueError, Args: {error.args}")
    print()
    wrong_coord: str = "abc, def, ghi"
    print(f"Parsing invalid coordinates: \"{wrong_coord}\"")
    try:
        a, b, c = wrong_coord.split(",")
        bad = (int(a), int(b), int(c))
    except ValueError as error:
        print(f"Error parsing coordinates: {error}")
        print(f"Error details - Type: ValueError, Args: {error.args}")
    print()
    print("Unpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={new_coord[0]}, Y={new_coord[1]}, Z={new_coord[2]}")


if __name__ == "__main__":
    main()
