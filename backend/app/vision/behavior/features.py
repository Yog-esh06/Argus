from __future__ import annotations


def compute_velocity(trajectory: list[tuple[float, float]]) -> float:
    if len(trajectory) < 2:
        return 0.0
    dx = trajectory[-1][0] - trajectory[0][0]
    dy = trajectory[-1][1] - trajectory[0][1]
    return (dx ** 2 + dy ** 2) ** 0.5


def dwell_time(history: list[float]) -> float:
    return sum(history) if history else 0.0
