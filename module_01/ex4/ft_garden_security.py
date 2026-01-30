"""Module for a secure garden system that validates plant data."""


class SecurePlant:
    """Class that represents a plant in the garden"""
    def __init__(self, name: str) -> None:
        """Inicializate a plant with name, height and age"""
        self.name = name.capitalize()
        self._height = 0
        self._age = 0

    def get_height(self) -> int:
        """The protection for height"""
        return self._height

    def get_age(self) -> int:
        """THe protection for age"""
        return self._age

    def set_height(self, height) -> None:
        """Validates the plant height"""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        """Validates the age plant"""
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days [OK]\n")


def ft_garden_security() -> None:
    """Security system with valid and invalid data"""
    print("=== Garden Security System ===")

    rose = SecurePlant("rose")
    print(f"Plant created: {rose.name}")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)

    print(
        f"\nCurrent plant: {rose.name} "
        f"({rose.get_height()}cm, {rose.get_age()} days)"
    )


if __name__ == "__main__":
    ft_garden_security()
