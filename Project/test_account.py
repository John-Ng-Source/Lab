from account import *


class Test:
    def setup_method(self):
        self.a1 = Account('Jane')
        self.a2 = Account('John')

    def teardown_method(self):
        del self.a1
        del self.a2

    def test_init(self):
        assert self.a1.get_name() == 'Jane'
        assert self.a1.get_balance() == 0
        assert self.a2.get_name() == 'John'
        assert self.a2.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(-2) is False
        assert self.a1.get_balance() == 0
        assert self.a1.deposit(5.0) is True
        assert self.a1.get_balance() == 5.0
        assert self.a1.deposit(5) is True
        assert self.a1.get_balance() == 10.0

    def test_withdraw(self):
        assert self.a2.withdraw(-10) is False
        assert self.a2.get_balance() == 0
        assert self.a1.withdraw(5) is True
        assert self.a1.get_balance() == 5.0
        assert self.a1.withdraw(2.0) is True
        assert self.a1.get_balance() == 3.0
