"""Module to create and manage multiple plant instances."""


class Plant:
    """Class that represents a plant in the garden"""
    def __init__(self, name: str, height: int, age: int):
        """Inicializate a plant with name, height and age"""
        self.name = name.capitalize()
        self.height = height
        self.age = age


def ft_plant_factory() -> None:
    """Streamline the creation of a plant and display its info"""
    print("=== Plant Factory Output ===")

    garden = [
        Plant("rose", 25, 30),
        Plant("oak", 200, 365),
        Plant("cactus", 5, 90),
        Plant("sunflower", 80, 45),
        Plant("fern", 15, 120),
    ]

    for plant in garden:
        print(f"Created {plant.name}: {plant.height}cm, {plant.age} days old")

    print(f"\nTotal plants created: {len(garden)}")


if __name__ == "__main__":
    ft_plant_factory()
