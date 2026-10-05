from __future__ import annotations

from fastapi import APIRouter

from app.api.v1 import analytics, cameras, incidents, models, streams, system, zones

router = APIRouter(prefix='/api/v1')
router.include_router(cameras.router)
router.include_router(incidents.router)
router.include_router(zones.router)
router.include_router(analytics.router)
router.include_router(models.router)
router.include_router(system.router)
router.include_router(streams.router)
