from __future__ import annotations

from pydantic import BaseModel, Field


class ZoneBase(BaseModel):
    name: str
    zone_type: str = Field(default='restricted')
    points: list[list[int]]
    color: str | None = None


class ZoneCreate(ZoneBase):
    pass


class Zone(ZoneBase):
    id: str
