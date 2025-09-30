class Back:
    def __init__(self):
        pass
    
    def create_account():
        pass
    
    def close_account():
        pass
    
    
class Account:
    def __init__(self, sum, currency):
        self.currency = currency
        self.sum = sum
        
    def add(self, amount):
        return self.sum + amount
            
class Customer:
    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname
        