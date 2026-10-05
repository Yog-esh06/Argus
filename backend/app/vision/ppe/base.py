from __future__ import annotations

from abc import ABC, abstractmethod


class PPEModel(ABC):
    @abstractmethod
    def detect(self, frame):
        raise NotImplementedError
