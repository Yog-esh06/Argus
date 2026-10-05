from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Track:
    track_id: str
    object_class: str
    confidence: float
    bounding_box: list[float]
    centroid: tuple[float, float]
    velocity: float = 0.0
    trajectory: list[tuple[float, float]] = field(default_factory=list)
    first_seen: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    last_seen: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass
class ZoneRecord:
    id: str
    name: str
    zone_type: str
    points: list[list[int]]
    color: str | None = None


@dataclass
class IncidentRecord:
    id: str
    camera_id: str
    event_type: str
    severity: str
    status: str
    summary: str
    created_at: str
    confidence: float = 0.0


@dataclass
class EventRecord:
    id: str
    timestamp: str
    camera_id: str
    event_type: str
    severity: str
    track_ids: list[str]
    confidence: float
    rule: str
    description: str
