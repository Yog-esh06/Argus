from __future__ import annotations

from datetime import datetime, timezone

from app.events.state_machine import TemporalStateMachine, cooldown_passed


class EventEngine:
    def __init__(self):
        self.machine = TemporalStateMachine()
        self.last_event_at: dict[str, float] = {}

    def evaluate(self, camera_id: str, track_ids: list[str], zone_name: str | None = None, line_crossed: bool = False):
        now = datetime.now(timezone.utc).timestamp()
        event_type = 'ZONE_BREACH' if zone_name else 'LINE_CROSSING' if line_crossed else 'UNUSUAL_MOVEMENT'

        if zone_name:
            if self.machine.observe(f'{camera_id}:{zone_name}', True):
                if cooldown_passed(self.last_event_at.get(event_type), now=now):
                    self.last_event_at[event_type] = now
                    return {
                        'event_type': event_type,
                        'severity': 'HIGH',
                        'description': f"{','.join(track_ids)} entered the {zone_name} zone.",
                        'confidence': 0.83,
                    }
        if line_crossed:
            if cooldown_passed(self.last_event_at.get('LINE_CROSSING'), now=now):
                self.last_event_at['LINE_CROSSING'] = now
                return {
                    'event_type': 'LINE_CROSSING',
                    'severity': 'MEDIUM',
                    'description': f"Track {','.join(track_ids)} crossed the monitored line.",
                    'confidence': 0.76,
                }
        return None
