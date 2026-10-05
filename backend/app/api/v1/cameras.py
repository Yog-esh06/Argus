from __future__ import annotations

from fastapi import APIRouter

from app.services.camera_service import camera_store

router = APIRouter(prefix='/cameras', tags=['cameras'])


@router.get('/')
def list_cameras():
    return {'items': [camera.__dict__ for camera in camera_store().values()]}


@router.get('/{camera_id}')
def get_camera(camera_id: str):
    camera = camera_store().get(camera_id)
    if not camera:
        return {'error': 'camera not found'}
    return camera.__dict__
