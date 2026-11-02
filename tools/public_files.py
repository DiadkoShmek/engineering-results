"""One public-candidate traversal shared by scans and the hash manifest.

This is deliberately not a git-tracked-file filter: new untracked public
files must receive the same privacy/link checks before publication.
"""
import os
from pathlib import Path

RUNTIME_DIRECTORIES = {'.git', '__pycache__', '.venv', '.pytest_cache'}


def public_files(root: Path):
    for directory, directories, files in os.walk(root):
        directories[:] = sorted(d for d in directories if d not in RUNTIME_DIRECTORIES)
        for name in sorted(files):
            if name in RUNTIME_DIRECTORIES or name == '.DS_Store' or Path(name).suffix in {'.pyc', '.pyo'}:
                continue
            yield Path(directory) / name
