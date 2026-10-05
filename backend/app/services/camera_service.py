from __future__ import annotations

from app.db.models.camera import CameraModel
from app.db.session import store


def get_demo_cameras() -> list[CameraModel]:
    return [
        CameraModel('cam-001', 'Dock 12', 'Warehouse North', 'rtsp://demo/warehouse-north', 'online', '1920x1080', 25, {'zone_count': 3}),
        CameraModel('cam-002', 'Loading Bay', 'Inbound Logistics', 'rtsp://demo/loading-bay', 'online', '1280x720', 20, {'zone_count': 2}),
    ]


def camera_store() -> dict[str, object]:
    if 'cameras' not in store:
        store['cameras'] = {camera.id: camera for camera in get_demo_cameras()}
    return store['cameras']
