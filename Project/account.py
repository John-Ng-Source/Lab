
class Account:
    def __init__(self, name: str) -> None:
        """Constructor to create initial state of account object
           :param name: Person's First or Full Name."""
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """Method to positively increment account balance.
        :param amount: Deposit amount
        :return: Success of Method - True or False"""
        success = True
        if (self.__account_balance <= 0) or (amount <= 0):
            success = False
        else:
            self.__account_balance += amount
        return success

    def withdraw(self, amount: float):
        """Method to negatively increment account balance.
           :param amount: deposit amount.
           :return: Success of Method - True or False"""
        success = True
        if self.__account_balance <= 0:
            success = False
        elif amount > self.__account_balance:
            success = False
        else:
            self.__account_balance -= amount
        return success

    def get_balance(self) -> float:
        """Method to return account balance.
           :return: account balance."""
        return self.__account_balance

    def get_name(self) -> str:
        """Method to return account name.
           :return: account name."""
        return self.__account_name

    
