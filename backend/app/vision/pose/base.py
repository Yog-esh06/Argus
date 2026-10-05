from __future__ import annotations

from abc import ABC, abstractmethod


class PoseEstimator(ABC):
    @abstractmethod
    def estimate(self, frame):
        raise NotImplementedError
