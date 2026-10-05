from __future__ import annotations


def detect_anomaly(velocity: float, direction_changes: int = 0, dwell_time: float = 0.0) -> bool:
    return velocity > 180 or direction_changes > 2 or dwell_time > 180
