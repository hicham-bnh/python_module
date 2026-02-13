from pydantic import BaseModel, ValidationError, field_validator
from typing import Optional
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str
    name: str
    crew_size: int
    power_level: float
    oxygen_level: float
    last_maintenance: datetime
    is_operational: bool
    notes: Optional[str]

    @field_validator("station_id")
    @classmethod
    def check_id(cls, station_id: str) -> str:
        if len(station_id) < 3 or len(station_id) > 10:
            raise ValueError("ID should be less than 10 or more than 3")
        return station_id

    @field_validator("name")
    @classmethod
    def check_name(cls, name: str) -> str:
        if len(name) < 1 or len(name) > 50:
            raise ValueError("name should be more than 1 or less thane 50")
        return name

    @field_validator("crew_size")
    @classmethod
    def crew_size_is_valid(cls, crew_size: int) -> int:
        if crew_size < 1 or crew_size > 20:
            raise ValueError("crew_size must be between 1 and 20")
        return crew_size

    @field_validator("power_level")
    @classmethod
    def check_power(cls, power_level: float) -> float:
        if power_level < 0.0 or power_level > 100.0:
            raise ValueError(
                "power_level should be less than 100.0 or more than 0.0"
            )
        return power_level

    @field_validator("oxygen_level")
    @classmethod
    def check_oxygen(cls, oxygen_level: float) -> float:
        if oxygen_level < 0.0 or oxygen_level > 100.0:
            raise ValueError(
                "oxygen_level should be less than 100.0 or more than 0.0"
            )
        return oxygen_level

    @field_validator("is_operational")
    @classmethod
    def check_operational(cls, is_operational: bool) -> bool:
        if not isinstance(is_operational, bool):
            raise ValueError("is_operational should be true or false")
        return is_operational

    @field_validator("notes")
    @classmethod
    def check_notes(cls, notes: Optional[str]) -> Optional[str]:
        if notes is not None and len(notes) > 200:
            raise ValueError("notes should have max 200 characters")
        return notes


def main():
    print("Space Station Data Validation")
    print("========================================")
    try:
        station1: SpaceStation = SpaceStation(
            station_id=" ISS001",
            name=" International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2024, 5, 20, 14, 30),
            is_operational=True,
            notes=None
        )
        print("Valid station created:")
        print(f"ID: {station1.station_id}")
        print(f"Name: {station1.name}")
        print(f"Crew: {station1.crew_size} people")
        print(f"Power: {station1.power_level}%")
        print(f"Oxygen: {station1.oxygen_level}%")
        print("Status", end=" ")
        if (station1.is_operational):
            print("Operational")
        else:
            print("Not Operational")
    except ValidationError as e:
        print("Expected validation error: ")
        print(e)
    print()
    print("========================================")
    try:
        station2: SpaceStation = SpaceStation(
            station_id="hicham",
            name=" International Space Station",
            crew_size=80,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2024, 5, 20, 14, 30),
            is_operational=False,
            notes=None
        )
        print("Space Station Data Validation")
        print("========================================")
        print("Valid station created:")
        print(f"ID: {station2.station_id}")
        print(f"Name: {station2.name}")
        print(f"Crew: {station2.crew_size} people")
        print(f"Power: {station2.power_level}%")
        print(f"Oxygen: {station2.oxygen_level}%")
        print("Status", end=" ")
        if (station2.is_operational):
            print("Operational")
        else:
            print("Not Operational")
    except ValidationError as e:
        print("Expected validation error:")
        print(e)


if __name__ == "__main__":
    main()
