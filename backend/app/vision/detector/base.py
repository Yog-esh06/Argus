from __future__ import annotations

from abc import ABC, abstractmethod


class ObjectDetector(ABC):
    """Detector abstraction used by the ingestion pipeline."""

    @abstractmethod
    def load(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def predict(self, frame):
        raise NotImplementedError
