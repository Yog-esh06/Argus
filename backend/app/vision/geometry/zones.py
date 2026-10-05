from __future__ import annotations


def _orientation(a: tuple[float, float], b: tuple[float, float], c: tuple[float, float]) -> float:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def _on_segment(point: tuple[float, float], start: tuple[float, float], end: tuple[float, float]) -> bool:
    if abs(_orientation(start, end, point)) > 1e-9:
        return False
    return min(start[0], end[0]) - 1e-9 <= point[0] <= max(start[0], end[0]) + 1e-9 and min(start[1], end[1]) - 1e-9 <= point[1] <= max(start[1], end[1]) + 1e-9


def point_in_polygon(point: tuple[float, float], polygon: list[list[int]]) -> bool:
    """Ray-casting algorithm for point-in-polygon tests, including edge membership."""
    if not polygon:
        return False

    x, y = point
    inside = False
    n = len(polygon)
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i + 1) % n]

        if _on_segment(point, (xi, yi), (xj, yj)):
            return True

        intersects = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi + 1e-9) + xi)
        if intersects:
            inside = not inside
    return inside


def line_crossing(start: tuple[float, float], end: tuple[float, float], line: tuple[tuple[float, float], tuple[float, float]]) -> bool:
    """Return True when the tracked path intersects the configured line segment."""
    p1, p2 = start, end
    p3, p4 = line

    o1 = _orientation(p1, p2, p3)
    o2 = _orientation(p1, p2, p4)
    o3 = _orientation(p3, p4, p1)
    o4 = _orientation(p3, p4, p2)

    if abs(o1) < 1e-9 and _on_segment(p3, p1, p2):
        return True
    if abs(o2) < 1e-9 and _on_segment(p4, p1, p2):
        return True
    if abs(o3) < 1e-9 and _on_segment(p1, p3, p4):
        return True
    if abs(o4) < 1e-9 and _on_segment(p2, p3, p4):
        return True

    return (o1 > 0) != (o2 > 0) and (o3 > 0) != (o4 > 0)
