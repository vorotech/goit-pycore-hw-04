"""Module for Task 4."""

import handler

from handler import ContactError

def parse_input(user_input: str) -> tuple:
    """Parses user input and returns command and arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    """Main function."""
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")

        elif command == "all":
            contacts = handler.get_all_contacts()
            print(contacts)

        elif command == "add":
            try:
                name, phone = args
                handler.add_contact(name, phone)
            except ContactError as e:
                print(e)
                continue
            except ValueError:
                print("Invalid command. Usage: add [ім'я] [номер телефону]")
                continue

            print("Contact added.")

        elif command == "change":
            try:
                name, phone = args
                handler.change_contact(name, phone)
            except ContactError as e:
                print(e)
                continue
            except ValueError:
                print("Invalid command. Usage: change [ім'я] [новий номер телефону]")
                continue

            print("Contact updated.")

        elif command == "phone":
            try:
                name = args[0]
                phone = handler.get_phone(name)
                print(phone)
            except ContactError as e:
                print(e)
                continue
            except (ValueError, IndexError):
                print("Invalid command. Usage: phone [ім'я]")
                continue

        elif command in ["exit", "close"]:
            print("Goodbye!")
            break

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
