from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import List


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_mission(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with M")
        error = 0
        for cr in self.crew:
            if cr.rank is Rank.captain or cr.rank is Rank.commander:
                error += 1
        if error == 0:
            raise ValueError("Must have at least one Commander or Captain")
        if self.crew:
            for crews in self.crew:
                if not crews.is_active:
                    raise ValueError("All crew members must be active")
        if self.duration_days > 365:
            experienced_count = sum(
                1 for m in self.crew if m.years_experience >= 5
                )
            if experienced_count < len(self.crew) / 2:
                raise ValueError(
                    "Long missions need 50% experienced crew (5+ years)"
                    )
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    try:
        crew1: CrewMember = CrewMember(
            member_id="001",
            name="Sarah Connor",
            rank=Rank.commander,
            years_experience=10,
            age=50,
            specialization="Mission Command"
        )
        crew2: CrewMember = CrewMember(
            member_id="002",
            name="John Smith",
            rank=Rank.lieutenant,
            years_experience=10,
            age=50,
            specialization="Navigation"
        )
        crew3: CrewMember = CrewMember(
            member_id="003",
            name="Alice Johnson",
            rank=Rank.officer,
            years_experience=10,
            age=50,
            specialization="Engineering"
        )
        crew4: CrewMember = CrewMember(
            member_id="003",
            name="Alice Johnson",
            rank=Rank.officer,
            years_experience=10,
            age=50,
            specialization="Engineering"
        )
        crews: List[CrewMember] = [crew1, crew2, crew3]
        crews2: List[CrewMember] = [crew4, crew2, crew3]
        mission1: SpaceMission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            duration_days=900,
            budget_millions=2500.0,
            crew=crews,
            launch_date=datetime.now()
        )
        print(f"Mission: {mission1.mission_name}")
        print(f"ID: {mission1.mission_id}")
        print(f"Destination: {mission1.destination}")
        print(f"Duration: {mission1.duration_days} days")
        print(f"Budget: {mission1.budget_millions}M")
        print(f"Crew size: {len(mission1.crew)}")
        print("Crew members:")
        for cr in mission1.crew:
            print(f"- {cr.name} ({cr.rank}) - {cr.specialization}")
    except ValidationError as e:
        print(e.errors()[0]['msg'])
    print()
    print("=========================================")
    print("Expected validation error:")
    try:
        mission2: SpaceMission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            duration_days=900,
            budget_millions=2500.0,
            crew=crews2,
            launch_date=datetime.now()
        )
        print(f"Mission: {mission2.mission_name}")
        print(f"ID: {mission2.mission_id}")
        print(f"Destination: {mission2.destination}")
        print(f"Duration: {mission2.duration_days} days")
        print(f"Budget: {mission2.budget_millions}M")
        print(f"Crew size: {len(mission2.crew)}")
        print("Crew members:")
        for cr in mission2.crew:
            print(f"- {cr.name} ({cr.rank}) - {cr.specialization}")
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
