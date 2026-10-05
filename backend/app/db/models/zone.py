from dataclasses import dataclass


@dataclass
class ZoneModel:
    id: str
    name: str
    zone_type: str
    points: list[list[int]]
    color: str | None = None
