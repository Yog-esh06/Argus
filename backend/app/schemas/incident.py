from __future__ import annotations

from pydantic import BaseModel, Field


class IncidentBase(BaseModel):
    camera_id: str
    event_type: str
    severity: str = Field(default='MEDIUM')
    status: str = Field(default='open')
    summary: str


class IncidentCreate(IncidentBase):
    pass


class Incident(IncidentBase):
    id: str
    created_at: str
    confidence: float = 0.0
