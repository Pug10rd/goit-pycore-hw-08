from commands.commands_list import add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, birthdays
from OOP import AddressBook
import pickle

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook() 

def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


book = load_data()


def main():
    print("Welcome to the Choco.py assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            show_all(book)

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday": 
            print(show_birthday(args, book))

        elif command == "birthdays": 
            print(birthdays(book))

        elif command in ["close", "exit"]:
            print("Goodbye!")
            break

        else:
            print("Invalid command.")
            
    save_data(book)

if __name__ == "__main__":
    main()
