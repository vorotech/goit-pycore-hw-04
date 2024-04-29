"""Main module for task_2."""

from pathlib import Path

def get_cats_info(path: str) -> list:
    """Reads a file with cats info and returns list of dictionaries with cats properties."""

    cats = []

    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            id, name, age = line.strip().split(",")
            cats.append({"id": id, "name": name, "age": int(age)})

    return cats

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
