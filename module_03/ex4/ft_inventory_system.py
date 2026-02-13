import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    args = sys.argv[1:]
    total_args = len(args)
    inventory = {}
    for arg in args:
        name, quantity = arg.split(":")
        inventory[name] = int(quantity)
    print(f"Total items in inventory: {sum(inventory.values())}")
    print(f"Unique item types: {total_args}")
    print()
    print("=== Current Inventory ===")
    total_units = sum(inventory.values())
    for name, quantity in inventory.items():
        calc = (quantity / total_units) * 100
        unit_str = "unit" if quantity == 1 else "units"
        print(f"{name}: {quantity} {unit_str} ({calc:.1f}%)")
    print()
    print("=== Inventory Statistics ===")
    most_name = ""
    least_name = ""
    max_qty = 0
    min_qty = None
    for name, quantity in inventory.items():
        if min_qty is None or quantity < min_qty:
            min_qty = quantity
            least_name = name
        if quantity > max_qty:
            max_qty = quantity
            most_name = name

    print(f"Most abundant: {most_name} ({max_qty} units)")
    print(f"Least abundant: {least_name} ({min_qty} unit)")
    print()
    print("=== Item Categories ===")
    categories = {"Moderate": {}, "Scarces": {}}
    for name, quantity in inventory.items():
        if quantity >= 5:
            categories["Moderate"][name] = quantity
        else:
            categories["Scarces"][name] = quantity
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarces']}")
    print()
    print("=== Management Suggestions ===")
    restock = [name for name, qty in inventory.items() if qty == 1]
    print(f"Restock needed: {restock}")
    print()
    print("=== Dictionary Properties Demo ===")
    only_keys = list(inventory.keys())
    only_values = list(inventory.values())
    print(f"Dictionary keys: {only_keys}")
    print(f"Dictionary values: {only_values}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    main()
