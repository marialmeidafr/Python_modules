"""Module for specialized plant types using inheritance and polymorphism."""


class Plant:
    """Class that represents a plant in the garden"""
    def __init__(self, name: str, height: int, age: int):
        """Inicializate a plant with name, height and age"""
        self.name = name.capitalize()
        self.height = height
        self.age = age


class Flower(Plant):
    """Specialized plant that has a color and can bloom"""
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def display_status(self) -> str:
        """Returns status specific to flowers"""
        return (f"{self.name} (Flower): {self.height}cm, "
                f"{self.age} days, {self.color} color")

    def bloom(self) -> None:
        """Specific behavior for flowers"""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Specialized plant with trunk diameter and shade ability"""
    def __init__(self, name: str, height: int, age: int, diam: int) -> None:
        super().__init__(name, height, age)
        self.diameter = diam

    def display_status(self) -> str:
        """Returns status specific to trees"""
        return (f"{self.name} (Tree): {self.height}cm, "
                f"{self.age} days, {self.diameter}cm diameter")

    def tam_shade(self) -> None:
        """Specific behavior for trees"""
        shade = 78
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    """Specialized plant with harvest season and nutritional value"""
    def __init__(self, name: str, height: int, age: int,
                 season: str, vitamin: str) -> None:
        super().__init__(name, height, age)
        self.season = season
        self.vitamin = vitamin

    def display_status(self) -> str:
        """Returns status specific to vegetables"""
        return (f"{self.name} (Vegetable): {self.height}cm, "
                f"{self.age} days, {self.season} harvest")

    def show_nutrition(self) -> None:
        """Specialized plant """
        print(f"{self.name} is rich in {self.vitamin}")


def ft_plant_types() -> None:
    """Main function to match the subject's example output"""
    print("=== Garden Plant Types ===\n")

    rose = Flower("rose", 25, 30, "red")
    print(rose.display_status())
    rose.bloom()
    print()
    oak = Tree("oak", 500, 1825, 50)
    print(oak.display_status())
    oak.tam_shade()
    print()
    tomato = Vegetable("tomato", 80, 90, "summer", "vitamin C")
    print(tomato.display_status())
    tomato.show_nutrition()


if __name__ == "__main__":
    ft_plant_types()
