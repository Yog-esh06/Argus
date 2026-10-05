from app.risk.scorer import RiskScorer


def test_risk_score_and_severity():
    scorer = RiskScorer()
    score = scorer.score(distance=10, zone_factor=15, velocity=20, duration=3)
    assert score > 0
    assert scorer.severity(score) in {'MEDIUM', 'HIGH', 'CRITICAL'}
