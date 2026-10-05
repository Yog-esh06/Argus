from __future__ import annotations

from app.vision.detector.base import ObjectDetector


class YOLODetector(ObjectDetector):
    """Placeholder detector that is replaceable with Ultralytics or other backends."""

    def __init__(self, model_name: str = 'yolov8n.pt', confidence_threshold: float = 0.45):
        self.model_name = model_name
        self.confidence_threshold = confidence_threshold
        self._loaded = False

    def load(self) -> None:
        self._loaded = True

    def predict(self, frame):
        if not self._loaded:
            self.load()

        detected = [
            {'class_name': 'person', 'confidence': 0.92, 'bbox': [120, 80, 200, 300], 'centroid': (160, 190)},
            {'class_name': 'forklift', 'confidence': 0.88, 'bbox': [400, 180, 640, 340], 'centroid': (520, 260)},
            {'class_name': 'truck', 'confidence': 0.9, 'bbox': [700, 120, 1040, 420], 'centroid': (870, 270)},
        ]
        return [item for item in detected if item['confidence'] >= self.confidence_threshold]
