from __future__ import annotations

from fastapi import APIRouter

router = APIRouter(prefix='/models', tags=['models'])


@router.get('/')
def list_models():
    return {
        'items': [
            {'name': 'yolov8n.pt', 'type': 'object_detection', 'status': 'ready', 'version': '8.2.0', 'device': 'cpu', 'fps': 28.4, 'latency_ms': 42.1},
            {'name': 'yolov8n-pose', 'type': 'pose_estimation', 'status': 'degraded', 'version': '8.2.0', 'device': 'cpu', 'fps': 16.3, 'latency_ms': 64.2},
        ]
    }
