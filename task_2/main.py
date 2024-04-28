"""Main module for task_2."""

from pathlib import Path

from  cat_parser import get_cats_info

def main():
    """Main function."""

    base_path = Path(__file__).resolve().parent

    try:
        cats_info = get_cats_info(Path(base_path, "cats.txt"))
        print(cats_info)
    except FileNotFoundError as e:
        print(f"Error: {e.strerror}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
