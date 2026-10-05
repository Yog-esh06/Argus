from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(prefix='/analytics', tags=['analytics'])


@router.get('/')
def get_analytics():
    return {
        'summary': {
            'cameras_online': 2,
            'critical_alerts': 1,
            'events_24h': 18,
            'active_tracks': 14,
        },
        'trend': [
            {'time': '00:00', 'events': 2},
            {'time': '03:00', 'events': 4},
            {'time': '06:00', 'events': 5},
            {'time': '09:00', 'events': 7},
            {'time': '12:00', 'events': 3},
        ],
    }
