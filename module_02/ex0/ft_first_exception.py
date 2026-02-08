def check_temperature(temp_str: str) -> None:
    """check if the temperature is valid or not"""
    try:
        temp = int(temp_str)

        if temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
    except ValueError:
        print(f"Error: {temp_str} is not a valid number")


def test_temperature_input() -> None:
    """testing with differents temperatures"""
    print("=== Garden Temperature Checker ===\n")

    good_case: str = "25"
    bad_case: str = "abc"
    hot_case: str = "100"
    cold_case: str = "-50"

    print(f"Testing temperature: {good_case}")
    check_temperature(good_case)
    print()
    print(f"Testing temperature: {bad_case}")
    check_temperature(bad_case)
    print()
    print(f"Testing temperature: {hot_case}")
    check_temperature(hot_case)
    print()
    print(f"Testing temperature: {cold_case}")
    check_temperature(cold_case)
    print()
    print("All tests completed - program didn't crash!")


# if __name__ == "__main__":
    # test_temperature_input()
