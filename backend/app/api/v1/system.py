from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(prefix='/system', tags=['system'])


@router.get('/health')
def health():
    return {'status': 'healthy', 'uptime_seconds': 1840, 'cpu_percent': 35.2, 'memory_percent': 51.8}


@router.get('/metrics')
def metrics():
    return {
        'fps': 24.1,
        'inference_latency_ms': 32.4,
        'queue_depth': 2,
        'frames_processed': 12876,
        'frames_dropped': 3,
        'detection_count': 245,
        'active_tracks': 14,
        'events': 9,
    }
