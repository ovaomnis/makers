import datetime


class SmartPhones:
    def __init__(self, name, color, memory, battery=0):
        self.name = name
        self.color = color
        self.memory = memory
        self.battery = battery

    def charge(self, amount):
        self.battery += amount

    def __str__(self):
        return f'{self.name} {self.memory}'


class Iphone(SmartPhones):
    def __init__(self, name, color, memory, ios, battery=0):
        super().__init__(name, color, memory, battery)
        self.ios = ios

    def send_imessage(self, text):
        return f'sending {text} from {self}'


class Samsung(SmartPhones):
    def __init__(self, name, color, memory, android, battery=0):
        super().__init__(name, color, memory, battery)
        self.android = android

    def show_time(self):
        return datetime.datetime.now().time()


phone = SmartPhones('generic', 'blue', '128GB')
print(phone)
print(phone.battery)
phone.charge(20)
print(phone.battery)
iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3')
print(iphone7)
print(iphone7.send_imessage('hello'))
samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo')
print(samsung21.show_time())

