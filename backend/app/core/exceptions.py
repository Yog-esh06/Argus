class ArgusError(RuntimeError):
    """Base error for Argus API operations."""


class CameraNotFoundError(ArgusError):
    pass


class IncidentNotFoundError(ArgusError):
    pass
