from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_lenght=3, max_lenght=10)
    name: str = Field(min_lenght=1, max_lenght=50)
    crew_size: int = Field(min_lenght=1, max_lenght=20)
    power_level: float = Field(min_lenght=0.0, max_lenght=100.0)
    oxygen_level: float = Field(min_lenght=0.0, max_lenght=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_lenght=200)


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)
    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
        )
        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        print(
            "Status: "
            f"{'Operational' if valid_station.is_operational else 'Down'}",
        )
    except ValidationError as error:
        print()


if __name__ == "__main__":
    main()
