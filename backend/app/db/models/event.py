from dataclasses import dataclass, field


@dataclass
class EventModel:
    id: str
    timestamp: str
    camera_id: str
    event_type: str
    severity: str
    track_ids: list[str] = field(default_factory=list)
    confidence: float = 0.0
    rule: str = 'manual'
    description: str = ''
