from __future__ import annotations

import math


def euclidean_distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def estimate_physical_distance(image_distance_px: float, pixels_per_meter: float = 10.0) -> float:
    """Return an estimated physical distance. This is not exact world distance unless calibrated."""
    if pixels_per_meter <= 0:
        raise ValueError('pixels_per_meter must be positive')
    return image_distance_px / pixels_per_meter
