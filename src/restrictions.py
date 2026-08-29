"""Path restrictions checker."""

from pathlib import Path


def is_restricted_path(path: Path) -> bool:
    """Check if the given path is a restricted path.

    A path is considered a restricted path if it's 
    the home directory itself, the root directory, 
    a direct child of the home directory, or any file
    regardless of location.

    Args:
        path (Path): Given path to be checked.

    Returns:
        bool: True if a restricted path, False if not.
    """
    absolute_path = Path(path).expanduser().resolve()
    home = Path().home().resolve()

    is_home = absolute_path == home
    is_root = absolute_path == absolute_path.parent
    is_child_of_home = absolute_path.parent == home
    is_file = absolute_path.is_file()

    return any([is_home, is_root, is_child_of_home, is_file])
