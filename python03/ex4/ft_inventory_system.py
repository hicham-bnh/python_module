"""
Inventory System Analysis

This program analyzes an inventory provided via command-line arguments.
It calculates totals, identifies the most and least abundant items,
categorizes stock levels, and demonstrates dictionary properties.
"""
import sys


if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print("Error")
    else:
        print("=== Inventory System Analysis ===")
        args: list[str] = sys.argv[1:]
        items: list[tuple[str, int]] = []
        inventory: dict[str, int] = {}
        max: int = 0
        min: int = 2
        item_max: str = None
        item_min: str = None
        try:
            for arg in args:
                name: str
                qty: int
                name, qty = arg.split(":")
                if max < int(qty):
                    max = int(qty)
                    item_max = name
                if min > int(qty):
                    min = int(qty)
                    item_min = name
                items.append((name, int(qty)))
        except KeyError as e:
            print(e)
        result: int = 0
        try:
            for name, qty in items:
                name: str
                qty: int
                if inventory.get(name):
                    inventory.update({name: inventory.get(name, 0) + qty})
                    result += qty
                else:
                    result += qty
                    inventory.update({name: qty})
        except KeyError as e:
            print(e)
        inventory_sorte: dict[str, int] = dict(sorted(
            inventory.items(), key=lambda inventory: inventory[1],
            reverse=True))
        print("Total items in inventory:", result)
        print("Unique item types:", len(inventory))
        print()
        print("=== Current Inventory ===")
        for name in inventory_sorte:
            name: str
            print(f"{name}: {inventory_sorte.get(name)}", end=" ")
            print(f"({(inventory_sorte.get(name)/result)*100:.1f}%)")
        print()
        print("=== Inventory Statistics ===")
        print(f"Most abundant: {item_max} ({inventory[item_max]} units)")
        print(f"Leats abundant: {item_min} ({inventory[item_min]} units)")
        print()
        moderate: dict[str, int] = {}
        scare: dict[str, int] = {}
        for name, qty in items:
            name: str
            qty: int
            if qty > 3:
                moderate.update({name: qty})
            else:
                scare.update({name: qty})
        print("=== Item Categories ===")
        print("Moderate:", moderate)
        print("Scare:", scare)
        print()
        restock = []
        for name, qty in items:
            name: str
            qty: int
            if qty == 1:
                restock.append(name)
        print("=== Management Suggestions ===")
        print("Restock needed:", restock)
        print()
        print("=== Dictionary Properties Demo ===")
        print("Dictionary keys:", list(inventory.keys()))
        print("Dictionary values:", list(inventory.values()))
        print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")
