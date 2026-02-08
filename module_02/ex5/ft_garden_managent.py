class GardenError(Exception):
    """Geral garden errors"""
    pass

class PlantError(GardenError):
    """Plant's specific errors"""
    pass

class WaterError(GardenError):
    """Water's specific error"""
    pass

class SunlightError(GardenError):
    """Sunlight's specific error"""
    pass

# --- CLASSE GERENCIADORA ---
class GardenManager:
    def __init__(self):
        self.plants = []

    def garden_size(self, list_of_plants, check_none: bool = True) -> int:
        size: int = 0
        for plant in list_of_plants:
            if check_none and plant[0] is None:
                break
            size += 1
        return size

    def add_plants(self, list_of_plants) -> None:
        # Usamos sua lógica de pré-alocação
        size = self.garden_size(list_of_plants, check_none=False)
        self.plants = [None] * size
        i = 0
        while i < size:
            try:
                if list_of_plants[i][0] is None:
                    raise PlantError("Plant name cannot be empty!")
                self.plants[i] = list_of_plants[i]
                print(f"Added {list_of_plants[i][0]} successfully")
            except PlantError as e:
                print(f"Error adding plant: {e}")
            finally:
                i += 1

    def water_plants(self) -> None:
        print("\nWatering plants...")
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant is None:
                    continue 
                print(f"Watering {plant[0]} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        print("\nChecking plant health...")
        for plant in self.plants:
            if plant is None:
                continue
            try:
                # Validação de Água
                if plant[1] < 1:
                    raise WaterError(f"Water level {plant[1]} is too low (min 1)")
                elif plant[1] > 10:
                    raise WaterError(f"Water level {plant[1]} is too high (max 10)")
                
                # Validação de Sol
                if plant[2] < 2:
                    raise SunlightError(f"Sunlight hours {plant[2]} is too low (min 2)")
                elif plant[2] > 12:
                    raise SunlightError(f"Sunlight hours {plant[2]} is too high (max 12)")
                
                print(f"{plant[0]}: healthy (water: {plant[1]}, sun: {plant[2]})")
            except GardenError as e:
                print(f"Error checking {plant[0]}: {e}")

    def recovery(self) -> None:
        print("\nTesting error recovery...")
        try:
            # Simulação de erro crítico
            raise WaterError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("System recovered and continuing...")

# --- MAIN E TESTE ---
def main():
    print("=== Garden Management System ===\n")
    garden = GardenManager()
    
    # Dados para gerar exatamente o seu output
    plants_data = [
        ["tomato", 5, 8],     # OK
        ["lettuce", 15, 8],    # Erro de água (15 > 10)
        [None, 5, 8]           # Erro de nome
    ]

    print("Adding plants to garden...")
    garden.add_plants(plants_data)
    
    garden.water_plants()
    garden.check_plant_health()
    garden.recovery()
    
    print("\nGarden management system test complete!")

if __name__ == "__main__":
    main()
