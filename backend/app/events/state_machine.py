from __future__ import annotations


class TemporalStateMachine:
    def __init__(self):
        self.states: dict[str, str] = {}

    def observe(self, key: str, condition: bool) -> bool:
        if condition and self.states.get(key) != 'active':
            self.states[key] = 'active'
            return True
        if not condition and key in self.states:
            self.states[key] = 'clear'
        return False


def cooldown_passed(last_timestamp: float | None, cooldown_seconds: float = 10.0, now: float | None = None) -> bool:
    if last_timestamp is None:
        return True
    if now is None:
        import time
        now = time.time()
    return (now - last_timestamp) >= cooldown_seconds
