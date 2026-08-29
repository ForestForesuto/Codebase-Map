"""Git-related file utilities."""

from pathlib import Path

import pathspec
from pathspec import PathSpec
from pathspec.patterns.gitignore.basic import GitIgnoreBasicPattern

from .constants import gitignore_patterns


def is_gitignore_exist(path: Path) -> bool:
    """Check if the given path has a .gitignore file.

    Args:
        path (Path): Given path to be checked.

    Returns:
        bool: True if a .gitignore file exists at the
            given path, False otherwise.
    """
    gitignore_path = path / '.gitignore'
    return gitignore_path.exists()

def read_gitignore(path: Path) -> PathSpec[GitIgnoreBasicPattern]:
    """Read .gitignore content and return its patterns.

    Args:
        path (Path): Given path containing the .gitignore file.

    Returns:
        PathSpec[GitIgnoreBasicPattern]: The parsed .gitignore
            patterns.
    """
    gitignore_path = path / '.gitignore'
    patterns = gitignore_path.read_text().splitlines()

    spec = pathspec.PathSpec.from_lines('gitignore', patterns)
    return spec

def default_gitignore() -> PathSpec[GitIgnoreBasicPattern]:
    """Return a PathSpec built from the default .gitignore patterns.

    Returns:
        PathSpec[GitIgnoreBasicPattern]: The parsed default
            .gitignore patterns.
    """
    return pathspec.PathSpec.from_lines('gitignore', gitignore_patterns)
