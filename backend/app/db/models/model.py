from dataclasses import dataclass


@dataclass
class ModelInfo:
    name: str
    type: str
    status: str
    version: str
    device: str
    fps: float
    latency_ms: float
