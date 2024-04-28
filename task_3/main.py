"""Module for Task 3."""

import sys

from tree_traversal import display_tree

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
