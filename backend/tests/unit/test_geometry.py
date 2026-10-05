from app.vision.geometry.distance import estimate_physical_distance, euclidean_distance
from app.vision.geometry.zones import line_crossing, point_in_polygon


def test_point_in_polygon_true():
    polygon = [[0, 0], [10, 0], [10, 10], [0, 10]]
    assert point_in_polygon((5, 5), polygon) is True


def test_point_in_polygon_false():
    polygon = [[0, 0], [10, 0], [10, 10], [0, 10]]
    assert point_in_polygon((15, 15), polygon) is False


def test_line_crossing_detected():
    start = (1, 1)
    end = (8, 8)
    line = ((4, 0), (4, 10))
    assert line_crossing(start, end, line) is True


def test_point_on_polygon_boundary_is_included():
    polygon = [[0, 0], [10, 0], [10, 10], [0, 10]]
    assert point_in_polygon((5, 0), polygon) is True


def test_line_crossing_returns_false_when_segments_do_not_intersect():
    start = (1, 1)
    end = (2, 2)
    line = ((4, 0), (4, 10))
    assert line_crossing(start, end, line) is False


def test_distance_estimation():
    assert euclidean_distance((0, 0), (3, 4)) == 5.0
    assert estimate_physical_distance(50, pixels_per_meter=10) == 5.0
