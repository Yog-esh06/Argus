from __future__ import annotations


class EvidenceStorage:
    def __init__(self, base_dir: str = 'evidence'):
        self.base_dir = base_dir

    def snapshot_path(self, event_id: str, camera_id: str) -> str:
        return f"{self.base_dir}/snapshots/{camera_id}-{event_id}.png"

    def clip_path(self, event_id: str, camera_id: str) -> str:
        return f"{self.base_dir}/clips/{camera_id}-{event_id}.mp4"
