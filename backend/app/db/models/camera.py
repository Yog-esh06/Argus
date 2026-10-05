from dataclasses import dataclass, field


@dataclass
class CameraModel:
    id: str
    name: str
    location: str
    stream_url: str
    status: str = 'online'
    resolution: str = '1920x1080'
    fps: int = 25
    metadata: dict = field(default_factory=dict)
