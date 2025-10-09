class Bank:
    def __init__(self, name):
        self.name = name 
        self.customers = {}
    # --------------------------------------------------------------------------------------------------------
    def add_customer(self, customer):
        self.customers[customer.id] = customer
    # --------------------------------------------------------------------------------------------------------
    def create_account(self, customer, currency):
        if customer.id not in self.customers:
            raise ValueError("Клиента нет в списке банка.")
        if currency in customer.accounts:
            print("У клиента уже есть счёт в этой валюте.")
        else:
            account = Account(customer, currency)
            customer.accounts[currency] = account
            return account
    # --------------------------------------------------------------------------------------------------------
    def close_account(self, customer, currency):
        if customer.id not in self.customers:
            print("Клиента нет в списке банка.")
        if currency not in customer.accounts:
            print("Такого счёта у клиента нет.")
        else:
            del customer.accounts[currency]
    # --------------------------------------------------------------------------------------------------------
    def add_to_account(self, customer, currency, amount):
        account = self._get_account(customer, currency)
        account.add(amount)
    # --------------------------------------------------------------------------------------------------------        
    def get_from_account(self, customer, currency, amount):
        account = self._get_account(customer, currency)
        account.get(amount)
    # --------------------------------------------------------------------------------------------------------
    def transfer_to_account(self, from_customer, to_customer, currency, amount):
        from_account = self._get_account(from_customer, currency)
        to_account = self._get_account(to_customer, currency)
        from_account.get(amount)
        to_account.add(amount)
    # --------------------------------------------------------------------------------------------------------        
    def print_customers(self):
        print("Клиенты банка:")
        for customer in self.customers.values():
            print(f"{customer.name} {customer.surname}, {customer.age}")
    # --------------------------------------------------------------------------------------------------------   
    def _get_account(self, customer, currency):
        if customer.id not in self.customers:
            print("Клиента нет в списке банка.")
        if currency not in customer.accounts:
            print("У клиента нет счёта в этой валюте.")
        else:
            return customer.accounts[currency]
# ------------------------------------------------------------------------------------------------------------    
class Account:
    def __init__(self, customer, currency):
        self.customer = customer
        self.currency = currency
        self.sum = 0
    # -------------------------------------------------------------------------------------------    
    def add(self, amount):
        if amount <= 0:
            raise ValueError("Введите положительное число")
        self.sum += amount
    # -------------------------------------------------------------------------------------------
    def get(self, amount):
        if amount <= 0:
            raise ValueError("Введите положительное число")
        if amount > self.sum:
            print("На счету недостаточно средств")
        else:
            self.sum -= amount
# ------------------------------------------------------------------------------------------------------------            
class Customer:
    def __init__(self, id, name, surname, age):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.accounts = {}
    # --------------------------------------------------------------------------------------------------------    
    def print_customer(self):
        print(f"{self.id}. {self.name} {self.surname}, {self.age}")
    # --------------------------------------------------------------------------------------------------------    
    def print_accounts(self):
        if not self.accounts:
            print("Нет открытых счетов.")
        else:
            print(f"Счета клиента {self.name}:")
            for currency in self.accounts.keys():
                print(f"Валюта: {currency}, сумма: {self.accounts[currency].sum}")
# ------------------------------------------------------------------------------------------------------------            
# ------------------------------------------------------------------------------------------------------------            
belarusbank = Bank("Беларусбанк")
customer1 = Customer(0, "Alex", "John", 21)
customer2 = Customer(1, "Sarah", "Brown", 22)

belarusbank.add_customer(customer1)
belarusbank.add_customer(customer2)
# ------------------------------------------------------------------------------------------------------------            
while True:
    print("Банковское приложение\nВыберите действие:")
    print("1. Войти как клиент")
    print("2. Стать новым клиентом")
    print("3. Показать всех клиентов банка")
    print("4. Выход")
    # --------------------------------------------------------------------------------------------------------
    choice = input()
    # --------------------------------------------------------------------------------------------------------
    if choice == "1":
        customer_id = input("Введите ваше ID: ")
        # ----------------------------------------------------------------------------------------------------
        if customer_id.isdigit():
            customer_id = int(customer_id)
            if customer_id in belarusbank.customers:
                login_customer = belarusbank.customers[customer_id]
                # -------------------------------------------------------------------------------------------
                print(f"Добро пожаловать, {login_customer.name}!\nВыберите услугу:")
                while True:
                    print("1. Открыть счёт")
                    print("2. Закрыть счёт")
                    print("3. Пополнить счёт")
                    print("4. Снять со счёта")
                    print("5. Перевести другому клиенту")
                    print("6. Показать мои счета")
                    print("7. Сделать выписку о счетах")
                    print("8. Выйти")
                    # -------------------------------------------------------------------------------------------
                    customers_action = input()
                    # -------------------------------------------------------------------------------------------
                    if customers_action == "1":
                        currency = input("Введите валюту вашего счёта (BYN, USD, EUR и т.д.): ").upper()
                        belarusbank.create_account(login_customer, currency)
                        print("Счёт успешно создан!")
                    # -------------------------------------------------------------------------------------------    
                    elif customers_action == "2":
                        currency = input("Введите валюту вашего счёта (BYN, USD, EUR и т.д.): ").upper()
                        belarusbank.close_account(login_customer, currency)
                        print("Счёт успешно закрыт!")
                    # -------------------------------------------------------------------------------------------    
                    elif customers_action == "3":
                        currency = input("Введите валюту вашего счёта (BYN, USD, EUR и т.д.): ").upper()
                        amount = input("Введите сумму пополнения: ")
                        if amount.isdigit():
                            amount = float(amount)
                            belarusbank.add_to_account(login_customer, currency, max(amount, 0))
                            print(f"Счёт пополнен на {amount} {currency}")
                    # -------------------------------------------------------------------------------------------        
                    elif customers_action == "4":
                        currency = input("Введите валюту вашего счёта (BYN, USD, EUR и т.д.): ").upper()
                        amount = input("Введите сумму пополнения: ")
                        if amount.isdigit():
                            amount = float(amount)
                            belarusbank.get_from_account(login_customer, currency, max(amount, 0))
                            print(f"Со счёта снята сумма в {amount} {currency}")
                    # -------------------------------------------------------------------------------------------
                    elif customers_action == "5":
                        to_id = input("Введите ID получателя: ")
                        amount = input("Введите сумму перевода: ")
                        # -------------------------------------------------------------------------------------------
                        if to_id.isdigit() and amount.isdigit():
                            to_id = int(to_id)
                            amount = float(amount)
                            # -------------------------------------------------------------------------------------------
                            if to_id == login_customer.id:
                                print("Нельзя перевести сумму на свой же счёт")
                                continue
                            # -------------------------------------------------------------------------------------------
                            if to_id not in belarusbank.customers:
                                print("Получатель не найден")
                                continue
                            # -------------------------------------------------------------------------------------------
                            if to_id >= 0:
                                to_customer = belarusbank.customers[to_id]
                                currency = input("Введите валюту вашего счёта (BYN, USD, EUR и т.д.): ").upper()
                                belarusbank.transfer_to_account(login_customer, to_customer, currency, max(amount, 0))
                        # -------------------------------------------------------------------------------------------
                    elif customers_action == "6":
                        login_customer.print_accounts()
                    # -------------------------------------------------------------------------------------------
                    elif customers_action == "7":
                        path = f"Extract_bank_{login_customer.name}.txt"
                        accounts_str = "Выписка по вашим счетам:\n\n"
                        total_sum = 0
                        # -------------------------------------------------------------------------------------------
                        if not login_customer.accounts:
                            accounts_str += "У вас пока нет открытых счетов.\n"
                        else:
                            for currency, account in login_customer.accounts.items():
                                accounts_str += f"Счёт в {currency}: баланс {account.sum:.2f}\n"
                                total_sum += account.sum
                            accounts_str += f"\nОбщая сумма по всем счетам: {total_sum:.2f}"
                        # -------------------------------------------------------------------------------------------
                        with open(path, "w", encoding="utf-8") as file:
                            file.write(accounts_str)
                        # -------------------------------------------------------------------------------------------
                        print(f"Выписка успешно сохранена в файл: {path}\n")
                    # -------------------------------------------------------------------------------------------
                    elif customers_action == "8":
                        break
                    else:
                        print("Вы ввели что-то не то. Попробуйте снова")
            # -------------------------------------------------------------------------------------------
            else:
                print("Такого клиента нет у нашего банка")
                continue
            # -------------------------------------------------------------------------------------------
        else:
            break
    # ------------------------------------------------------------------------------------------------------------
    elif choice == "2":
        print("Введите ваши данные:")
        new_id = input("Введите ID: ")
        name = input("Имя: ")
        surname = input("Фамилия: ")
        age = input("Возраст: ")
        new_customer = Customer(int(new_id), name, surname, age)
        belarusbank.add_customer(new_customer)
        print(f"Отлично, {new_customer.name}! Теперь вы новый клиент нашего банка. Ваш ID = {new_customer.id}.")
        continue
    # ------------------------------------------------------------------------------------------------------------
    elif choice == "3":
        belarusbank.print_customers()
        continue
    # ------------------------------------------------------------------------------------------------------------            
    elif choice == "4":
        print("Спасибо, что воспользовались нашим банком!")
        break