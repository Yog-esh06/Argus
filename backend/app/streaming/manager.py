from __future__ import annotations

from dataclasses import dataclass


@dataclass
class StreamStatus:
    camera_id: str
    online: bool
    fps: float
    dropped_frames: int
    queue_depth: int


class StreamManager:
    def __init__(self):
        self.streams: dict[str, StreamStatus] = {}

    def register(self, camera_id: str, fps: float = 25.0):
        self.streams[camera_id] = StreamStatus(camera_id=camera_id, online=True, fps=fps, dropped_frames=0, queue_depth=4)

    def snapshot(self):
        return [status.__dict__ for status in self.streams.values()]
