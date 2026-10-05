"""Run the Argus backend and frontend together for local development."""

from __future__ import annotations

import os
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def start_process(command: list[str], cwd: Path) -> subprocess.Popen[str]:
    return subprocess.Popen(
        command,
        cwd=cwd,
        text=True,
        creationflags=getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0),
    )


def main() -> int:
    backend = start_process(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "app.main:app",
            "--reload",
            "--host",
            "0.0.0.0",
            "--port",
            "8000",
        ],
        ROOT / "backend",
    )
    npm = "npm.cmd" if os.name == "nt" else "npm"
    frontend = start_process([npm, "run", "dev"], ROOT / "frontend")
    processes = [backend, frontend]

    try:
        while True:
            for process in processes:
                return_code = process.poll()
                if return_code is not None:
                    other = frontend if process is backend else backend
                    if other.poll() is None:
                        other.terminate()
                    return return_code
            time.sleep(0.2)
    except KeyboardInterrupt:
        return 0
    finally:
        for process in processes:
            if process.poll() is None:
                process.terminate()
        for process in processes:
            if process.poll() is None:
                process.wait()


if __name__ == "__main__":
    raise SystemExit(main())
