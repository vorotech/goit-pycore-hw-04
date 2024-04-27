"""Module for Task 1."""

import salary_calc

def main():
    """Main function."""

    file_path = input("Enter the salaries file path: ")

    try:
        total, average = salary_calc.total_salary(file_path)

        print(f"Total salary: {total}, Average salary: {average}")

    except FileNotFoundError as e:
        print(f"Error: {e.strerror}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
