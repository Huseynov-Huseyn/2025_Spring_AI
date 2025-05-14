class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        return f"{self.name} is working."


class Manager(Employee):
    def manage_employees(self):
        return f"{self.name} is managing employees."


class Developer(Employee):
    def write_code(self):
        return f"{self.name} is writing code."


# Test nümunələri
m1 = Manager("Ali")
d1 = Developer("Huseyn")

print(m1.work())              # Ali is working.
print(m1.manage_employees())  # Ali is managing employees.

print(d1.work())              # Huseyn is working.
print(d1.write_code())        # Huseyn is writing code.


from abc import ABC, abstractmethod
import uuid


# Abstract sinif (Abstraction tətbiqi)
class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


# Real bank hesabı sinifi
class BankAccount(Account):
    def __init__(self, name, initial_balance=0):
        self.__name = name                    # encapsulated
        self.__balance = initial_balance      # encapsulated
        self.__account_id = str(uuid.uuid4())  # unikal ID

    # Getter methods
    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def get_account_id(self):
        return self.__account_id

    # Basic banking operations
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} AZN deposited.")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} AZN withdrawn.")
        else:
            print("Insufficient balance or invalid amount.")

    def show_info(self):
        print(f"Name: {self.__name}")
        print(f"Balance: {self.__balance} AZN")
        print(f"Account ID: {self.__account_id}")


# Test nümunəsi
user1 = BankAccount("Huseyn", 100)
user1.show_info()

user1.deposit(50)
user1.withdraw(30)
user1.show_info()
