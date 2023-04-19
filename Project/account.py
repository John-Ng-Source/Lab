
class Account:
    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        success = False
        if self.__account_balance <= 0:
            return success
        else:
            self.__account_balance += amount
            success = True
            return success

    def withdraw(self, amount):
        success = False
        if self.__account_balance <= 0:
            return success
        else:
            self.__account_balance -= amount
            success = True
            return success

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name

    
