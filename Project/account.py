
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
        success = False
        if self.__account_balance <= 0:
            return success
        else:
            self.__account_balance += amount
            success = True
            return success

    def withdraw(self, amount: float):
        success = False
        """Method to negatively increment account balance.
           :param amount: deposit amount.
           :return: Success of Method - True or False"""
        if self.__account_balance <= 0:
            return success
        else:
            self.__account_balance -= amount
            success = True
            return success

    def get_balance(self) -> float:
        """Method to return account balance.
           :return: account balance."""
        return self.__account_balance

    def get_name(self) -> str:
        """Method to return account name.
           :return: account name."""
        return self.__account_name

    
