"""Directory tree search utilities"""

import os
import stat
import sys
from pathlib import Path

from pathspec import PathSpec
from pathspec.patterns.gitignore.basic import GitIgnoreBasicPattern


def _is_hidden(root_path: str, path: str) -> bool:
    """Check if the given path is hidden.

    On Windows, checks the FILE_ATTRIBUTE_HIDDEN flag.
    On macOS, checks the UF_HIDDEN flag.
    On other POSIX systems, checks if the path starts
    with a dot (`.`).

    Args:
        root_path (str): The absolute path before the
            given path.
        path (str): The given path to be checked.

    Returns:
        bool: True if the given path has the hidden
            attribute, False otherwise.
    """
    abs_path: str = os.path.join(root_path, path)
    if sys.platform == 'win32':
        file_stats = os.stat(abs_path)
        hidden = bool(file_stats.st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)
    elif sys.platform == 'darwin':
        file_stats = os.stat(abs_path)
        hidden = bool(file_stats.st_flags & stat.UF_HIDDEN)
    else:
        hidden = path.startswith(".")

    return hidden

def tree_search(path: Path, exclusions: PathSpec[GitIgnoreBasicPattern], allow_hiddens: bool) -> list[Path]:
    """Search a directory and return valid paths.

    Returns paths relative to the given directory that are not excluded
    by the gitignore patterns and are not hidden files/directories.

    Args:
        path (Path): The given path to be searched.
        exclusions (PathSpec[GitIgnoreBasicPattern]): Given paths that
            should not be included.

    Returns:
        list[Path]: Valid relative paths.
    """
    found_paths: list[Path] = []
    for root, dirs, files in os.walk(path, topdown=True):
        relative_root = os.path.relpath(root, path)
        relative_root = relative_root.replace(os.sep, '/')

        if relative_root == '.':
            relative_root = ''

        dirs[:] = [
            d for d in dirs
            if (not exclusions.match_file(
                (relative_root + '/' + d if relative_root else d) + '/'
            ) and (allow_hiddens or not _is_hidden(root, d)))
        ]

        files[:] = [
            f for f in files
            if (not exclusions.match_file(
                relative_root + '/' + f if relative_root else f
            ) and (allow_hiddens or not _is_hidden(root, f)))
        ]

        for d in dirs:
            found_paths.append(Path(relative_root) / (d + '/'))

        for f in files:
            found_paths.append(Path(relative_root) / f)

    return found_paths
