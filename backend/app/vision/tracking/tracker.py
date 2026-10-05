from __future__ import annotations

from app.db.base import Track


class Tracker:
    def __init__(self, max_track_age: int = 30):
        self.max_track_age = max_track_age
        self.tracks: dict[str, Track] = {}
        self.next_id = 1

    def register(self, object_class: str, confidence: float, bbox: list[float], centroid: tuple[float, float]) -> Track:
        track_id = f"{object_class.title()}#{self.next_id:02d}"
        self.next_id += 1
        track = Track(
            track_id=track_id,
            object_class=object_class,
            confidence=confidence,
            bounding_box=bbox,
            centroid=centroid,
            trajectory=[centroid],
        )
        self.tracks[track_id] = track
        return track

    def update(self, detections: list[dict]):
        active_ids = []
        for detection in detections:
            centroid = tuple(detection['centroid'])
            track = self._find_match(centroid)
            if track is None:
                track = self.register(detection['class_name'], detection['confidence'], detection['bbox'], centroid)
            else:
                track.confidence = detection['confidence']
                track.bounding_box = detection['bbox']
                track.centroid = centroid
                track.trajectory.append(centroid)
                if len(track.trajectory) > self.max_track_age:
                    track.trajectory = track.trajectory[-self.max_track_age:]
            active_ids.append(track.track_id)
        return active_ids

    def _find_match(self, centroid: tuple[float, float]):
        best_track = None
        best_distance = float('inf')
        for track in self.tracks.values():
            current = track.centroid
            distance = abs(current[0] - centroid[0]) + abs(current[1] - centroid[1])
            if distance < best_distance and distance < 200:
                best_distance = distance
                best_track = track
        return best_track
