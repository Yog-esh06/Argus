from dataclasses import dataclass


@dataclass
class IncidentModel:
    id: str
    camera_id: str
    event_type: str
    severity: str
    status: str
    summary: str
    created_at: str
    confidence: float = 0.0
