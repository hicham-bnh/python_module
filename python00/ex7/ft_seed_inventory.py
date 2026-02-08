def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    if (unit == "packets"):
        print(f"{seed_type} seeds: {quantity} {unit} avaible")
    elif (unit == "grams"):
        print(f"{seed_type} seeds: {quantity} {unit} avaible")
    elif (unit == "area"):
        print(f"{seed_type} seeds: quantity {quantity} meters")
    else:
        print("Unknown unit tquantity")
