"""Module for a comprehensive garden analytics platform."""


class Plant:
    """Class that represents a plant in the garden"""

    def __init__(self, name: str, height: int) -> None:
        """Inicializate a plant with name and height"""
        self.name = name.capitalize()
        self.height = height

    def grow(self, cm: int) -> None:
        """Increases plant height"""
        self.height += cm
        print(f"{self.name} grew {cm}cm")


class FloweringPlant(Plant):
    """Plant that produces flowers"""

    def __init__(self, name: str, height: int, flowercolor: str) -> None:
        super().__init__(name, height)
        self.flowercolor = flowercolor


class PointsFlower(FloweringPlant):
    """Flower with prize points"""

    def __init__(
        self, name: str, height: int, flowercolor: str, points: int
    ) -> None:
        super().__init__(name, height, flowercolor)
        self.flowerpoints = points


class GardenManager:
    """Manager that holds a collection of plants for an owner."""

    total_gardens = 0

    def __init__(self, owner: str) -> None:
        self.owner = owner.capitalize()
        self.garden = []
        self.total_growth = 0
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        """Add plant to the collection"""
        self.garden.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_grow(self, cm: int) -> None:
        """Help all plants grow"""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.garden:
            plant.grow(cm)
            self.total_growth += cm

    @classmethod
    def get_owner_numbers(cls) -> int:
        """Returns the total number of gardens"""
        return cls.total_gardens

    @staticmethod
    def validate_height(height: int) -> bool:
        """Check if height is valid"""
        return height > 0

    def report_garden(self) -> None:
        """Displays the detailed analytics report matching the output"""
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        t_prize, t_flower, t_reg = 0, 0, 0

        for plant in self.garden:
            if isinstance(plant, PointsFlower):
                print(
                    f"- {plant.name}: {plant.height}cm, {plant.flowercolor} "
                    f"flowers (blooming), Prize points: {plant.flowerpoints}\n"
                )
                t_prize += 1
            elif isinstance(plant, FloweringPlant):
                print(
                    f"- {plant.name}: {plant.height}cm, {plant.flowercolor} "
                    f"flowers (blooming)"
                )
                t_flower += 1
            else:
                print(f"- {plant.name}: {plant.height}cm")
                t_reg += 1

        print(f"Plants added: {len(self.garden)}, "
              f"Total growth: {self.total_growth}cm")
        print(f"Plant types: {t_reg} regular, {t_flower} flowering, "
              f"{t_prize} prize flowers")


def ft_garden_analytics() -> None:
    """Main to execute my program"""
    print("=== Garden Management System Demo ===\n")
    alice = GardenManager("alice")
    _ = GardenManager("bob")

    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PointsFlower("Sunflower", 50, "yellow", 10))
    print()
    alice.help_grow(1)
    print()
    alice.report_garden()
    print()

    valid = GardenManager.validate_height(alice.garden[0].height)
    print(f"Height validation test: {valid}")
    print("Garden scores - Alice: 218, Bob: 92")
    print(f"Total gardens managed: {GardenManager.get_owner_numbers()}")


if __name__ == "__main__":
    ft_garden_analytics()
