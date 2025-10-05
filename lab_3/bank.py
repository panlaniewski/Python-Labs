from time import time

class Bank:
    def __init__(self, name):
        self.name = name 
        self.customers = {}
    
    def add_customer(self, customer):
        self.customers[customer.id] = customer
    
    def create_account(self, customer, currency):
        if customer.id not in self.customers:
            raise ValueError("Клиента нет в списке банка.")
        if currency in customer.accounts:
            print("У клиента уже есть счёт в этой валюте.")
        else:
            account = Account(customer, currency)
            customer.accounts[currency] = account
            return account
    
    def close_account(self, customer, currency):
        if customer.id not in self.customers:
            print("Клиента нет в списке банка.")
        if currency not in customer.accounts:
            print("Такого счёта у клиента нет.")
        else:
            del customer.accounts[currency]
    
    def add_to_account(self, customer, currency, amount):
        account = self._get_account(customer, currency)
        account.add(amount)
            
    def get_from_account(self, customer, currency, amount):
        account = self._get_account(customer, currency)
        account.get(amount)
    
    def transfer_to_account(self, from_customer, to_customer, currency, amount):
        from_account = self._get_account(from_customer, currency)
        to_account = self._get_account(to_customer, currency)
        from_account.get(amount)
        to_account.add(amount)
            
    def print_customers(self):
        print("Клиенты банка:")
        for customer in self.customers.values():
            print(f"{customer.name} {customer.surname}, {customer.age}")
       
    def _get_account(self, customer, currency):
        if customer.id not in self.customers:
            print("Клиента нет в списке банка.")
        if currency not in customer.accounts:
            print("У клиента нет счёта в этой валюте.")
        else:
            return customer.accounts[currency]
    
class Account:
    def __init__(self, customer, currency):
        self.customer = customer
        self.currency = currency
        self.sum = 0
        
    def add(self, amount):
        if amount <= 0:
            raise ValueError("Введите положительное число")
        self.sum += amount
    
    def get(self, amount):
        if amount <= 0:
            raise ValueError("Введите положительное число")
        if amount > self.sum:
            print("На счету недостаточно средств")
        else:
            self.sum -= amount
            
class Customer:
    def __init__(self, name, surname, age):
        self.id = time()
        self.name = name
        self.surname = surname
        self.age = age
        self.accounts = {}
        
    def print_customer(self):
        print(f"{self.id}. {self.name} {self.surname}, {self.age}")
        
    def print_accounts(self):
        if not self.accounts:
            print("  Нет открытых счетов.")
        else:
            print(f"Счета клиента {self.name}:")
            for currency in self.accounts.keys():
                print(f"Валюта: {currency}, сумма: {self.accounts[currency].sum}")
            
belarusbank = Bank("Беларусбанк")
customer1 = Customer("Alex", "John", 21)
customer2 = Customer("Sarah", "Brown", 22)

belarusbank.add_customer(customer1)
belarusbank.add_customer(customer2)
belarusbank.print_customers()

belarusbank.create_account(customer1, "BYN")
customer1.print_accounts()

belarusbank.create_account(customer2, "BYN")
customer2.print_accounts()

belarusbank.add_to_account(customer1, "BYN", 100)
customer1.print_accounts()

belarusbank.add_to_account(customer2, "BYN", 200)
customer2.print_accounts()

belarusbank.transfer_to_account(customer1, customer2, "BYN", 50)
print("\nПосле перевода:")
customer1.print_accounts()
customer2.print_accounts()