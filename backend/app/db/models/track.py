from dataclasses import dataclass, field


@dataclass
class TrackModel:
    track_id: str
    object_class: str
    confidence: float
    bounding_box: list[float]
    centroid: tuple[float, float]
    velocity: float = 0.0
    trajectory: list[tuple[float, float]] = field(default_factory=list)
    first_seen: str = ''
    last_seen: str = ''
