class Plant:
    """Class that represents a plant in the garden"""
    def __init__(self, name: str, height: int, age: int):
        """Inicializate a plant with name, height and age"""
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def grow_plant(self):
        """Increases the size of the plant"""
        self.height += 1

    def age_plant(self):
        """Increases the age of the plant"""
        self.age += 1

    def get_info(self):
        """Return the status of the plant"""
        return(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_growth() -> None:
    """Simulates a week of the growth for the garden"""
    rose = Plant("rose", 25, 30)
    initial_height = rose.height

    print("=== Day 1 ===")
    print(rose.get_info())

    for _ in range(6):
        rose.grow_plant()
        rose.age_plant()

    print("=== Day 7 ===")
    print(rose.get_info())
    print(f"Growth this week: +{rose.height - initial_height}cm")


if __name__ == "__main__":
    ft_plant_growth()
