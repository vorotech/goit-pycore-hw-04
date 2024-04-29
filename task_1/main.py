"""Module for Task 1."""

from pathlib import Path
from typing import Tuple

def total_salary(path: str) -> Tuple[float, float]:
    """Load files by path and claculate total and average salary.

    Args:
        path (str): Absolute or relative path to file with salaries
        where each lime foramtted as "<name>,<salary>".

    Returns:
        Tuple[float, float]: Returns tuple of total and average salary.
    """
    total, average = 0, 0

    absolute_path =  Path(path).resolve()

    print("Calculating total and average salary from file:", absolute_path)

    with open(absolute_path, "r", encoding="utf-8") as file:
        records = file.readlines()
        for record in records:
            _, salary = record.split(",")
            total += float(salary.strip())

    average = total / len(records)

    return total, average

def main():
    """Main function."""

    file_path = input("Enter the salaries file path: ")

    try:
        total, average = total_salary(file_path)

        print(f"Total salary: {total}, Average salary: {average}")

    except FileNotFoundError as e:
        print(f"Error: {e.strerror}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
