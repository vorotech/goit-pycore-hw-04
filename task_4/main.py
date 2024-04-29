"""Module for Task 4."""

import handler

from handler import PhoneBookError

def main():
    """Main function."""
    print("Welcome to the assistant bot!")

    while True:
        command = input("Enter a command: ").strip().lower()

        if command == "hello":
            print("How can I help you?")

        elif command == "all":
            contacts = handler.get_all_contacts()
            print(contacts)

        elif command.startswith("add"):
            try:
                _, name, phone = command.split()
                handler.add_contact(name, phone)
            except PhoneBookError as e:
                print(f"Error: {e}")
                continue
            except ValueError:
                print("Invalid command. Usage: add [ім'я] [номер телефону]")
                continue

            print("Contact added.")

        elif command.startswith("change"):
            try:
                _, name, phone = command.split()
                handler.change_contact(name, phone)
            except PhoneBookError as e:
                print(f"Error: {e}")
                continue
            except ValueError:
                print("Invalid command. Usage: change [ім'я] [новий номер телефону]")
                continue

            print("Contact updated.")

        elif command.startswith("phone"):
            try:
                _, name = command.split()
                phone = handler.get_phone(name)
                print(phone)
            except PhoneBookError as e:
                print(f"Error: {e}")
                continue
            except ValueError:
                print("Invalid command. Usage: phone [ім'я]")
                continue

        elif command in ("exit", "close"):
            print("Goodbye!")
            break

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
