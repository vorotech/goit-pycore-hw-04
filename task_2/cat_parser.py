"""Module that reads a file with cats info and returns list of dictionaries with cats properties."""

def get_cats_info(path: str) -> list:
    """Reads a file with cats info and returns list of dictionaries with cats properties."""

    cats = []

    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            id, name, age = line.strip().split(",")
            cats.append({"id": id, "name": name, "age": int(age)})

    return cats
