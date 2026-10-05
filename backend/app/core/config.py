from __future__ import annotations

from pydantic import BaseModel, Field


class Settings(BaseModel):
    app_name: str = Field(default='Argus')
    app_env: str = Field(default='development')
    debug: bool = Field(default=True)
    port: int = Field(default=8000)
    model_name: str = Field(default='yolov8n.pt')
    confidence_threshold: float = Field(default=0.45)
    max_track_age: int = Field(default=30)
    pose_enabled: bool = Field(default=False)
    demo_mode: bool = Field(default=True)


settings = Settings()
