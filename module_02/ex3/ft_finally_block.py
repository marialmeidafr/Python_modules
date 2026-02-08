def water_plants(plant_list: list[str]) -> None:
    """Water all the plants on the list"""
    print("Opening watering system")
    success: bool = False
    try:
        for plant in plant_list:
            if plant is None:
                # mostramos erro, com a planta invalida
                raise Exception(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
        success = True
    except Exception as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")
    if success:
        print("Watering completed successfully!")


def test_watering_system():
    """testing with normal watering and error"""

    print("Testing normal watering...")
    right_list: list[str] = [
        "tomato",
        "lettuce",
        "carrots"
    ]
    water_plants(right_list)
    print()
    print("Testing with error...")
    wrong_list: list[str] = [
        "tomato",
        None
    ]
    water_plants(wrong_list)


def testing_finally():
    """main for tests"""
    print("=== Garden Watering System ===")
    print()
    test_watering_system()
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    testing_finally()
