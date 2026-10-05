from __future__ import annotations

from app.vision.ppe.base import PPEModel


class PPEDetector(PPEModel):
    def __init__(self, enabled: bool = False):
        self.enabled = enabled

    def detect(self, frame):
        if not self.enabled:
            return {'status': 'disabled', 'detections': []}
        return {'status': 'ok', 'detections': [{'type': 'helmet', 'confidence': 0.92}]}
