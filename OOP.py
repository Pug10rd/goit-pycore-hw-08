from collections import UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, number):
        if len(number) != 10:
            print(f"Number: {number} was too short, should be 10 digits, bye!")
            exit()
        super().__init__(number)

    def __str__(self):
        return str(self.value)


def get_upcoming_birthdays(users: list):
    congrats = []
    today = datetime.today().date()
    for user in users:
        b_day = datetime.strptime(user.birthday.value, "%d.%m.%Y").date()
        b_day_now = datetime(
            year=today.year, month=b_day.month, day=b_day.day).date()
        con_date = ''

        if b_day_now < today:
            con_date = f"{datetime(year=today.year + 1, month=b_day.month, day=b_day.day).date()}"

        else:
            days_difference = (b_day_now - today).days
            if days_difference <= 7:
                if b_day_now.isoweekday() > 5:
                    week_day = b_day_now.isoweekday()

                    match week_day:
                        case 6:
                            con_date = f"{b_day_now + timedelta(days=2)}"
                        case 7:
                            con_date = f"{b_day_now + timedelta(days=1)}"
                        case _:
                            con_date = f'{b_day_now}'
                else:
                    con_date = f'{b_day_now}'
            else:
                pass

            person = {
                "name": user.name.value,
                "congratulation_date": con_date
            }
            if con_date:
                congrats.append(person)
    if congrats:
        return f'Список привітань на цьому тижні: {congrats}'
    else:
        return "No one has a birthday this week"


class Birthday(Field):
    def __init__(self, value: str):
        self.value = value
        try:
            b_day = datetime.strptime(value, "%d.%m.%Y").date()
            if b_day:
                return print(b_day)

        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def add_birthday(self, b_day):
        self.birthday = b_day

    def edit_phone(self, old_num, new_num):
        self.phones = book.data[str(self.name)].phones
        for p in self.phones:
            if p.value == old_num:
                id = self.phones.index(p)
                self.phones.pop(id)
                self.phones.insert(id, Phone(new_num))

    def find_phone(self, num: str):
        self.phones = book.data[str(self.name)].phones
        for p in self.phones:
            if p.value == num:
                return num

    def remove_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                id = self.phones.index(p)
                self.phones.pop(id)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday if self.birthday else None}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, search_name: str):
        for name, record in self.data.items():
            if search_name == name:
                return record

    def delete(self, del_name):
        for name, record in book.data.items():
            if name == del_name:
                return book.pop(name)


# # Створення нової адресної книги
book = AddressBook()

