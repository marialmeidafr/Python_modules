class Plant:
    """Class that represents a plant in the garden"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Inicializate a plant with name, height and age"""
        self.name = name.capitalize()
        self.height = height
        self.age = age


def ft_garden_data() -> None:
    """Creates plant instances and displays their information."""

    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("cactus", 15, 120)
    print("=== Garden Plant Registry ===")

    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
    print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")


if __name__ == "__main__":
    ft_garden_data()
