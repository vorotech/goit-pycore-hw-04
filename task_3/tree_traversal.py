"""Module which traverses a tree file structure and visualizes it with colors."""
from pathlib import Path

import colorama

def display_tree(file_path: str | Path, indent: int = 0) -> None:
    """Traverses a tree file structure and visualizes it with colors."""
    colorama.init()

    path = Path(file_path)

    if not path.exists():
        raise ValueError(f"Path not found: {path}")

    if path.is_file():
        raise ValueError("Path must be a directory.")

    print(f"{"  " * indent}{colorama.Fore.LIGHTBLUE_EX}{path.name}/{colorama.Style.RESET_ALL}")

    dirs = sorted([item for item in path.iterdir() if item.is_dir()])
    files = sorted([item for item in path.iterdir() if item.is_file()])

    for dir in dirs:
        display_tree(dir, indent+1)

    for file in files:
        print(f"{"  " * (indent + 1)}{colorama.Fore.LIGHTYELLOW_EX}{file.name}{colorama.Style.RESET_ALL}")

    colorama.deinit()
