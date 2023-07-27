class BankAccount:
    balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        print(f'Ваш баланс: {self.balance} сом ')

    def deposit(self, amount):
        self.balance += amount
        print(f'Ваш баланс: {self.balance} сом ')