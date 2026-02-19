class GardenError(Exception):
    """Base class for exceptions in this module."""
    pass


class PlantError(GardenError):
    """Exception raised for errors in the plant management."""
    pass


class WaterError(GardenError):
    """Exception raised for errors in the watering system."""
    pass


class GardenManager:
    """Manages a collection of plants and a water tank system."""

    def __init__(self):
        """Initialize the GardenManager with an empty garden and full tank."""
        self.plants = {}
        self.water_tank = 100

    def water_plants(self) -> None:
        """
        Attempt to water all plants in the garden.

        Decreases water_tank by 5 for each plant. If water is insufficient,
        raises a WaterError and stops the process.

        Raises:
            WaterError: If water_tank is below 5 units.
        """
        try:
            for plant in self.plants:
                if self.water_tank < 5:
                    raise WaterError("Not enough water in tank")
                self.plants[plant]["water"] += 5
                self.water_tank -= 5
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(f"Caught GardenError: {e}")

    def add_plant(self, plant_name: str) -> str:
        """
        Add a new plant to the garden system.

        Args:
            plant_name (str): The name of the plant to be added.

        Returns:
            str: A success message confirming the plant addition.

        Raises:
            PlantError: If the plant_name is empty.
        """
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        self.plants[plant_name] = {"water": 0, "sun": 0}
        return f"Added {plant_name} successfully"

    def check_plant_health(self, plant_name: str,
                           water_level: int, sunlight_hours: int) -> str:
        """
        Validate the health parameters of a specific plant.

        Args:
            plant_name (str): Name of the plant to check.
            water_level (int): The current water level (expected 1-10).
            sunlight_hours (int): Daily sunlight hours (expected 2-12).

        Returns:
            str: A status message if all parameters are within range.

        Raises:
            PlantError: If any parameter is outside the allowed thresholds.
        """
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        if water_level < 1:
            raise PlantError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise PlantError(f"Water level {water_level} is too high (max 10)")
        if sunlight_hours < 2:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)")
        if sunlight_hours > 12:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)")
        return (f"{plant_name}: healthy (water: {water_level}, "
                f"sun: {sunlight_hours})")


def test_garden_management() -> None:
    """
    Execute a series of tests to demonstrate the GardenManager functionality,
    including error handling and resource management.
    """
    print("=== Garden Management System ===")

    manager = GardenManager()
    print("\nAdding plants to garden...")
    try:
        print(manager.add_plant("tomato"))
        print(manager.add_plant("lettuce"))
        print(manager.add_plant(""))
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    print("Opening watering system")

    manager.water_plants()
    print("Closing watering system (cleanup)")

    try:
        manager.check_plant_health("tomato", 5, 8)
    except PlantError as e:
        print(f"Error checking tomato: {e}")

    try:
        manager.check_plant_health("lettuce", 5, 11)
    except (GardenError, PlantError, WaterError) as e:
        print(f"Error: {e}")

    print("\nChecking plant health...")
    try:
        result = manager.check_plant_health("tomato", 5, 8)
        print(result)
    except PlantError as e:
        print(f"Error checking tomato: {e}")
    try:
        manager.check_plant_health("lettuce", 15, 6)
    except PlantError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        manager.water_tank = 2
        manager.water_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
