"""CLI tool to display a tree file structure of a codebase."""

from argparse import ArgumentParser, Namespace
from pathlib import Path


def main() -> None:
    """Parse command-line arguments and outputs the codebase tree structure."""
    parser = ArgumentParser()

    parser.usage = 'Use to see the tree file structure of your codebase'

    parser.add_argument(
        'path', help='Codebase path you want to see tree structure',
        type=Path, default=Path.cwd(), nargs='?'
    )
    parser.add_argument(
        '-ngi', '--nogitignore',
        help='Ignores the .gitignore in a codebase and uses default exclusions',
        action='store_true'
    )

    args: Namespace = parser.parse_args()
    work_dir = args.path
    print(work_dir)
