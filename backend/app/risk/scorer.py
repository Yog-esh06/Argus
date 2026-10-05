from __future__ import annotations


class RiskScorer:
    def __init__(self, policies: dict | None = None):
        self.policies = policies or {
            'base': {'warning_threshold': 35, 'critical_threshold': 70},
            'person_forklift_proximity': {'warning_threshold': 30, 'critical_threshold': 55, 'minimum_duration': 2.0},
        }

    def score(self, distance: float, zone_factor: float = 0.0, velocity: float = 0.0, duration: float = 0.0) -> int:
        score = 15
        score += max(0, 100 - distance) * 0.4
        score += zone_factor
        score += min(velocity * 2.5, 25)
        score += min(duration * 10, 20)
        return min(int(score), 100)

    def severity(self, score: int) -> str:
        if score >= self.policies['base']['critical_threshold']:
            return 'CRITICAL'
        if score >= self.policies['base']['warning_threshold']:
            return 'HIGH'
        return 'MEDIUM'
