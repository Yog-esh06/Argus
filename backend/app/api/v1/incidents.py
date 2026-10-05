from __future__ import annotations

from datetime import datetime, timezone

from fastapi import APIRouter

router = APIRouter(prefix='/incidents', tags=['incidents'])

_INCIDENTS = [
    {
        'id': 'inc-001',
        'camera_id': 'cam-001',
        'event_type': 'ZONE_BREACH',
        'severity': 'HIGH',
        'status': 'open',
        'summary': 'Person entered restricted machine zone',
        'created_at': datetime.now(timezone.utc).isoformat(),
        'confidence': 0.88,
    },
    {
        'id': 'inc-002',
        'camera_id': 'cam-002',
        'event_type': 'PROXIMITY_WARNING',
        'severity': 'MEDIUM',
        'status': 'investigating',
        'summary': 'Forklift and pedestrian proximity threshold exceeded',
        'created_at': datetime.now(timezone.utc).isoformat(),
        'confidence': 0.76,
    },
]


@router.get('/')
def list_incidents():
    return {'items': _INCIDENTS}


@router.get('/{incident_id}')
def get_incident(incident_id: str):
    for incident in _INCIDENTS:
        if incident['id'] == incident_id:
            return incident
    return {'error': 'incident not found'}
