class ContactList(list):
    def __init__(self, list):
        self.list_name = list

    def search_by_name(self, find):
        found_name = []
        for name in self.list_name:
            if name.lower().count(find.lower()) >= 1:
                found_name.append(name)
        return found_name


all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])
print(all_contacts.search_by_name('Ivan'))


class Person:
    def __init__(self):
        self.__name, self.__last_name, self.__age, self.__email = None, None, None, None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: int) -> None:
        self.__name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value: int) -> None:
        self.__last_name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int) -> None:
        self.__age = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value: int) -> None:
        self.__email = value


john = Person()
print(john.name) # None
print(john.last_name) # None
print(john.age) # None
print(john.email) # None
john.name = 'John'
john.last_name = 'Snow'
john.age = 30
john.email = 'johnsnow@gmail.com'
print(john.name) # John
print(john.last_name) # Snow
print(john.age) # 30
print(john.email) # johnsnow@gmail.com


