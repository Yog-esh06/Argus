from __future__ import annotations

from pydantic import BaseModel, Field


class CameraBase(BaseModel):
    name: str
    location: str
    stream_url: str
    status: str = Field(default='online')
    resolution: str = Field(default='1920x1080')
    fps: int = Field(default=25)


class CameraCreate(CameraBase):
    pass


class Camera(CameraBase):
    id: str
