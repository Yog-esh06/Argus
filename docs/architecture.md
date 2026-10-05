# Architecture

Argus is structured around a modular, event-driven design. The platform is intentionally layered so object detection, tracking, zone logic, risk scoring, and evidence management remain independent subsystems.

## Components

- Ingestion: reads live or recorded video and decouples source handling from processing
- Detection: object detection abstraction with a YOLO-compatible implementation
- Tracking: persistent object identity and trajectory maintenance
- Analysis: zone checks, line crossing, proximity, pose, and anomaly evaluation
- Event Engine: temporal confirmation and confidence-aware alert generation
- Risk: severity scoring and policy configuration
- Evidence: captures snapshots and clips for incident investigation
- API/UI: dashboard and operational support
