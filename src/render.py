"""Tree rendering-related utilities."""

import os
from pathlib import Path
from typing import Any

from .constants import symbols


def _build_render_struct(paths: list[Path]) -> dict[str, Any]:
    """Build a nested dict that represents the directory structure.

    For each path, it iterates through its parts and creates nested
    dictionaries to represent the folder hierarchy until the whole
    directory has been mapped out.

    Args:
        paths (list[Path]): All given paths to be organized.

    Returns:
        dict[str, Any]: Dictionary of the directory structure.
    """
    print_struct: dict[str, Any] = {}
    for path in paths:
        current = print_struct
        for part in path.parts:
            current = current.setdefault(part, {})

    return print_struct

def render_tree(paths: list[Path], root_path: Path) -> None:
    """Print the directory in a visual ASCII tree.

    The tree displays folders before files, sorts entries
    alphabetically, and shows hierarchy with branching
    symbols. Folders are render with a trailing slash to
    distinguish them from files.

    Args:
        paths (list[Path]): All given paths to be rendered.
        root_path (Path): The root directory that is being mapped.
    """
    print_struct = _build_render_struct(paths)
    print_lines: list[str] = []

    print_lines.append(os.path.basename(root_path) + '/')
    stack: list[tuple[str, dict[str, Any], str, bool, str]] = []

    root_items = sorted(
        print_struct.items(),
        key=lambda item: (0 if item[1] else 1, item[0])
    )
    for idx in range(len(root_items) - 1, -1, -1):
        name, children = root_items[idx]
        is_last_child = (idx == len(root_items) - 1)
        stack.append((name, children, "", is_last_child, name))

    while stack:
        name, node, prefix, is_last, rel_path = stack.pop()

        branch = symbols['last_branch'] if is_last else symbols['branch']

        abs_path = os.path.join(root_path, rel_path)
        is_dir = os.path.isdir(abs_path)

        display_name = name + '/' if is_dir else name
        print_lines.append(f"{prefix}{branch}{display_name}")

        if node:
            new_prefix = prefix + (symbols['indent'] if is_last else symbols['vertical'])
            child_items = sorted(
                node.items(),
                key=lambda item: (0 if item[1] else 1, item[0])
            )
            for idx in range(len(child_items) - 1, -1, -1):
                child_name, child_node = child_items[idx]

                is_last_child = (idx == len(child_items) - 1)
                child_rel_path = os.path.join(rel_path, child_name).replace(os.sep, '/')

                stack.append((child_name, child_node, new_prefix, is_last_child, child_rel_path))

    print("\n".join(print_lines))
