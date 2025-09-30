class Bank:
    def __init__(self, name):
        self.name = name 
    
    def create_account(self, customer, sum, currency):
        customer.account.append(Account(sum, currency))
    
    def close_account(self, customer):
        customer.account = "Нет действующего счёта"
    
    def transfer_account(self, account1, account2, amount):
        if amount > account1.sum or amount > account2.sum:
            print("На одном из счетов недостаточно средств")
        else: 
            account1.sum - amount
            account2.sum + amount
    
class Account:
    def __init__(self, sum, currency):
        self.currency = currency
        self.sum = sum
        
    def add(self, amount):
        self.sum + amount
    
    def get(self, amount):
        if amount > self.sum:
            print("На счету недостаточно средств")
        else:
            self.sum - amount
            
class Customer:
    def __init__(self, id, name, surname, age):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.account = []

belarusbank = Bank("Беларусбанк")        
new_customer = Customer("0", "Alex", "John", 21)
print(f"{new_customer.id}. {new_customer.name} {new_customer.surname}")
belarusbank.create_account(new_customer, 100, "рубль")
print(belarusbank.name)
print(new_customer.account[0].sum) 
new_customer.account[0].add(20)
print(new_customer.account[0].sum) 
belarusbank.create_account(new_customer, 100, "евро")
print(new_customer.account[1].currency) 