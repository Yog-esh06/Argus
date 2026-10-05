from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(prefix='/zones', tags=['zones'])

_ZONES = [
    {'id': 'zone-001', 'name': 'Restricted Area', 'zone_type': 'restricted', 'points': [[250, 160], [700, 160], [700, 420], [250, 420]], 'color': '#f87171'},
    {'id': 'zone-002', 'name': 'Emergency Assembly', 'zone_type': 'safe', 'points': [[100, 500], [350, 500], [350, 680], [100, 680]], 'color': '#34d399'},
]


@router.get('/')
def list_zones():
    return {'items': _ZONES}


@router.post('/')
def create_zone(zone: dict):
    zone['id'] = f"zone-{len(_ZONES) + 1:03d}"
    _ZONES.append(zone)
    return zone
