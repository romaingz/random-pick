from pathlib import Path
import random
import subprocess

from .internal import build_file_list


def from_path(path, patterns=None):
    r"""Fetch a random file from a path.

    You can specify a list of patterns.

    Examples:
        >>> from random_pick import from_path
        >>> choice = from_path(r"C:\temp", patterns=["*.txt"])
        >>> recursive = from_path(r"C:\temp", patterns=["**/*.txt"])
    """
    if not isinstance(path, Path):
        path = Path(path)

    if not patterns:
        patterns = ["*"]

    files = build_file_list(path, patterns)
    return random.choice(files)


def execute(program, path, patterns=None):
    r"""Execute a program on a random file.

    See `from_path` for more information.

    Examples:
        >>> import os
        >>> from pathlib import Path
        >>> from random_pick import execute
        >>> vlc = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
        >>> home = Path(os.getenv("USERPROFILE"))
        >>> execute(vlc, home / "Videos", ["*.mp4"])
    """
    pick = from_path(path, patterns)
    return subprocess.run([program, pick])
