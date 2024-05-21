"""Module for Task 3."""

from pathlib import Path

import sys

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

    # Ignore any python dirs or files similar to .gitignore
    ignore = [".git", "__pycache__", ".vscode", ".idea", ".gitignore", "venv", ".venv", ".egg-info"]

    dirs = sorted([item for item in path.iterdir() if item.is_dir() and item.name not in ignore])
    files = sorted([item for item in path.iterdir() if item.is_file() and item.name not in ignore])

    for d in dirs:
        display_tree(d, indent+1)

    for f in files:
        print(f"{"  " * (indent + 1)}{colorama.Fore.LIGHTYELLOW_EX}{f.name}{colorama.Style.RESET_ALL}")

    colorama.deinit()

def main():
    """Main function."""

    if len(sys.argv) != 2:
        print("Usage: python main.py <dir_path>")
        sys.exit(1)

    try:
        display_tree(sys.argv[1])
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
