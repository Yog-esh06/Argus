from __future__ import annotations

from app.vision.detector.yolo_detector import YOLODetector
from app.vision.tracking.tracker import Tracker


class VisionPipeline:
    def __init__(self, detector: YOLODetector | None = None):
        self.detector = detector or YOLODetector()
        self.tracker = Tracker(max_track_age=30)

    def process_frame(self, frame):
        self.detector.load()
        detections = self.detector.predict(frame)
        active_track_ids = self.tracker.update(detections)
        return {'detections': detections, 'active_track_ids': active_track_ids}
