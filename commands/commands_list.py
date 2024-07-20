from OOP import Record, AddressBook, Birthday, get_upcoming_birthdays


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please type name and number"
        except KeyError:
            return "Name does not exist"
        except IndexError:
            return "Provide the name please"

    return inner

def input_error_dob(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please type name and birth date in format DD.MM.YYYY"
        except KeyError:
            return "Name does not exist"
        except IndexError:
            return "Provide the name please"

    return inner

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    name, phone = args
    if book[name]:
        book[name].phones = phone
        return "Contact changed"


@input_error
def show_phone(args, book: AddressBook):
    title, *_ = args
    if title in book.data:
        record = book.data[title]
        return f"Phones for {title}: {', '.join(str(phone) for phone in record.phones)}"
    else:
        return f"No record found for {title}"


def show_all(book: AddressBook):
    for name, record in book.data.items():
        phones_str = ", ".join(str(phone.value) for phone in record.phones)
        if phones_str:
            print(f"Contact name: {record.name.value}, phones: {phones_str}")
        else:
            print(f"Contact name: {record.name.value}, phones: No phones listed")


@input_error_dob
def add_birthday(args, book: AddressBook):
    name, b_day, *_ = args
    record = book[name]
    if record:
        record.birthday = Birthday(b_day)
        message = "B-Day added."
        return message
    return "false"

@input_error_dob
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book[name]
    if record:
        if record.birthday:
            return f'{record.name}: {record.birthday}'


def birthdays(book: AddressBook):
    list_of_dates = []
    for name, contact in book.data.items():
        if contact.birthday:
            list_of_dates.append(contact)
    return get_upcoming_birthdays(list_of_dates)
