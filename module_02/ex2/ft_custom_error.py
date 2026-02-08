class GardenError(Exception):
    """Basic error for a garden problems"""
    pass


class PlantError(GardenError):
    """Problems with plants"""
    pass


class WaterError(GardenError):
    """Problems with watering"""
    pass


def check_plant() -> None:
    """function to check the status of the plant"""

    print("Testing PlantError...")
    try:
        print("Problem with the land")
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print(f"Caught PlantError: {error}")


def check_water() -> None:
    """function to check the water"""

    print("Testing WaterError")
    try:
        print("Problem with the water")
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print(f"Caught WaterError: {error}")


def check_garden() -> None:
    """function to check the garden"""

    print("Testing catching all garden errors...")
    try:
        print("Problem with the land")
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print(f"Caught a garden error: {error}")
    print()
    try:
        print("Problem with the water")
        raise WaterError("Not enough water in the tank!")
    except GardenError as error:
        print(f"Caught a garden error: {error}")


def test_all_errors() -> None:
    """main test runner"""

    print("=== Custom Garden Errors Demo ===\n")
    check_plant()
    print()
    check_water()
    print()
    check_garden()
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_all_errors()
