from __future__ import annotations

from app.vision.pose.base import PoseEstimator


class SimplePoseEstimator(PoseEstimator):
    def estimate(self, frame):
        return {
            'nose': (0.5, 0.2),
            'shoulders': (0.5, 0.3),
            'hips': (0.5, 0.5),
            'knees': (0.5, 0.7),
            'ankles': (0.5, 0.9),
        }
