from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(prefix='/streams', tags=['streams'])


@router.get('/health')
def stream_health():
    return {'status': 'OK', 'fps': 24.8, 'dropped_frames': 0, 'queue_depth': 3}
