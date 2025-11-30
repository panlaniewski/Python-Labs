class BankError(Exception):
    pass

class CustomerNotFoundError(BankError):
    pass

class AccountExistsError(BankError):
    pass

class AccountNotFoundError(BankError):
    pass

class NotEnoughMoneyError(BankError):
    pass

class Bank:
    def __init__(self, name):
        self.name = name 
        self.customers = {}
    # --------------------------------------------------------------------------------------------------------
    def add_customer(self, customer):
        if customer.id in self.customers:
            raise BankError("Клиент с таким ID уже существует.")
        self.customers[customer.id] = customer
    # --------------------------------------------------------------------------------------------------------
    def create_account(self, customer, currency):
        if customer.id not in self.customers:
            raise CustomerNotFoundError("Клиента нет в списке банка.")
        if currency in customer.accounts:
            raise AccountExistsError("У клиента уже есть счёт в этой валюте.")
        account = Account(customer, currency)
        customer.accounts[currency] = account
        return account
    # --------------------------------------------------------------------------------------------------------
    def close_account(self, customer, currency):
        if customer.id not in self.customers:
            raise CustomerNotFoundError("Клиента нет в списке банка.")
        if currency not in customer.accounts:
            raise AccountNotFoundError("Такого счёта у клиента нет.")
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
            raise CustomerNotFoundError("Клиента нет в списке банка.")
        if currency not in customer.accounts:
            raise AccountNotFoundError("У клиента нет счёта в этой валюте.")
        return customer.accounts[currency]
# ------------------------------------------------------------------------------------------------------------    
class Account:
    def __init__(self, customer, currency):
        self.customer = customer
        self.currency = currency
        self.sum = 0
    # -------------------------------------------------------------------------------------------    
    def add(self, amount):
        if not isinstance(amount, float):
            raise TypeError("Введите число!")
        elif amount <= 0:
            raise ValueError("Введите положительное число")
        else:
            self.sum += amount
    # -------------------------------------------------------------------------------------------
    def get(self, amount):
        if amount <= 0:
            raise ValueError("Введите положительное число.")
        if amount > self.sum:
            raise NotEnoughMoneyError("На счету недостаточно средств.")
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
    print("1.Войти как клиент")
    print("2.Стать новым клиентом")
    print("3.Показать всех клиентов банка")
    print("4.Выход")
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
                    print("1.Открыть счёт")
                    print("2.Закрыть счёт")
                    print("3.Пополнить счёт")
                    print("4.Снять со счёта")
                    print("5.Перевести другому клиенту")
                    print("6.Показать мои счета")
                    print("7.Сделать выписку о счетах")
                    print("8.Выйти")
                    # -------------------------------------------------------------------------------------------
                    customers_action = input()
                    try:
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
                            amount = float(input("Введите сумму пополнения: "))
                            belarusbank.add_to_account(login_customer, currency, amount)
                            print(f"Счёт пополнен на {amount} {currency}")
                        # -------------------------------------------------------------------------------------------        
                        elif customers_action == "4":
                            currency = input("Введите валюту вашего счёта (BYN, USD, EUR и т.д.): ").upper()
                            amount = float(input("Введите сумму пополнения: "))
                            belarusbank.get_from_account(login_customer, currency, amount)
                            print(f"Со счёта снята сумма в {amount} {currency}")
                        # -------------------------------------------------------------------------------------------
                        elif customers_action == "5":
                            to_id = input("Введите ID получателя: ")
                            amount = input("Введите сумму перевода: ")
                            # -------------------------------------------------------------------------------------------
                            if to_id.isdigit():
                                to_id = int(to_id)
                                amount = float(amount)
                                # -------------------------------------------------------------------------------------------
                                if to_id == login_customer.id:
                                    raise ValueError("Нельзя перевести сумму на свой же счёт")
                                # -------------------------------------------------------------------------------------------
                                if to_id not in belarusbank.customers:
                                    raise ValueError("Получатель не найден")
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
                    except ValueError as e:
                        print(" Ошибка:", e)
            # -------------------------------------------------------------------------------------------
            else:
                print("Такого клиента нет у нашего банка")
                continue
            # -------------------------------------------------------------------------------------------
        else:
            break
    # ------------------------------------------------------------------------------------------------------------
    elif choice == "2":
        try:
            print("Введите ваши данные:")
            # -------------------------------------------------------------------------------------------
            new_id = input("Введите ID: ")
            if not new_id.isdigit():
                raise ValueError("ID должно быть числом.")
            # -------------------------------------------------------------------------------------------
            new_id = int(new_id)
            if new_id in belarusbank.customers:
                raise BankError("Клиент с таким ID уже существует.")
            # -------------------------------------------------------------------------------------------
            name = input("Имя: ")
            surname = input("Фамилия: ")
            age = input("Возраст: ")
            # -------------------------------------------------------------------------------------------
            if not age.isdigit():
                raise ValueError("Возраст должен быть числом.")
            # -------------------------------------------------------------------------------------------
            new_customer = Customer(new_id, name, surname, int(age))
            belarusbank.add_customer(new_customer)
            print(f"Отлично, {new_customer.name}! Теперь вы клиент нашего банка. Ваш ID = {new_customer.id}.")
        # ------------------------------------------------------------------------------------------------
        except BankError as e:
            print("Ошибка:", e)
        except ValueError as e:
            print("Ошибка:", e)
    # ------------------------------------------------------------------------------------------------------------
    elif choice == "3":
        belarusbank.print_customers()
        continue
    # ------------------------------------------------------------------------------------------------------------            
    elif choice == "4":
        print("Спасибо, что воспользовались нашим банком!")
        break