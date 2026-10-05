from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import router as v1_router
from app.core.config import settings
from app.core.logging import logger

app = FastAPI(title=settings.app_name, version='0.1.0', debug=settings.debug)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(v1_router)


@app.get('/health')
def health():
    return {'status': 'healthy', 'service': settings.app_name}


@app.get('/health/live')
def live_health():
    return {'status': 'live', 'service': settings.app_name}


@app.get('/health/ready')
def ready_health():
    return {'status': 'ready', 'service': settings.app_name}


@app.get('/')
def root():
    logger.info('Argus API startup complete')
    return {'message': 'Argus API is running', 'version': '0.1.0'}
