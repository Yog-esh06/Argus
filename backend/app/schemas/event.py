from __future__ import annotations

from pydantic import BaseModel


class EventRecord(BaseModel):
    id: str
    timestamp: str
    camera_id: str
    event_type: str
    severity: str
    track_ids: list[str]
    confidence: float
    rule: str
    description: str
