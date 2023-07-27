class Phone:
    def __init__(self, name: str, last_name: str, phone: str):
        self.name, self.last_name, self.phone = name, last_name, phone

    def get_full_name(self):
        return f'{self.name} {self.last_name}'

    def get_info(self):
        print(f'Контакт: {self.get_full_name()}, телефон: {self.phone}')


contact = Phone('John', 'Snow', '+996707707707')
contact.get_info()
