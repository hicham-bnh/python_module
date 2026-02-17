import alchemy


def healing_potion():
    fire_result = alchemy.create_fire()
    water_result = alchemy.create_water()
    return f"Healing potion brewed with {fire_result} and {water_result}"


def strength_potion():
    earth_result = alchemy.elements.create_earth()
    fire_result = alchemy.create_fire()
    return f"Strength potion brewed with {earth_result} and {fire_result}"


def invisibility_potion():
    air_result = alchemy.elements.create_air()
    water_result = alchemy.create_water()
    return f"Invisibility potion brewed with {air_result} and {water_result}"


def wisdom_potion():
    water_result = alchemy.create_water
    fire_result = alchemy.create_fire
    air_result = alchemy.elements.create_air()
    earth_result = alchemy.elements.create_earth()
    return (
        f"Wisdom potion brewed with all elements: "
        f"{fire_result} and {water_result}"
        f"and {air_result} and {earth_result}"
    )
