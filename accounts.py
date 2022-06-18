# Inheritence
from customer_implementation import CustomerImpl


class SavingsAccount(CustomerImpl):
    def __init__(self, name: str, nid: str, address: str, age: int, account_num: str, opening_balance: int):
        super().__init__(name, nid, address, age)
        self.__account_num = account_num
        self.__opening_balance = opening_balance
        self.is_account_opened = False
        self.__total_amount = self.__opening_balance

    def account_status(self, name, nid, opening_balance):

        if opening_balance >= 500 and name == self.get_name() and nid == self.get_nid():
            self.is_account_opened = True
            return "Your account is successfully opened"
        else:
            return "Account is not opened yet"

    def get_account_num(self):
        return self.__account_num

    def deposit(self, deposit_amount):

        print(deposit_amount)
        self.__total_amount +=  deposit_amount
        return self.__total_amount

    def withdraw(self, withdraw_amount):

        if self.__total_amount >= withdraw_amount:
            self.__total_amount -= withdraw_amount
            return self.__total_amount
        else:
            return "Withdraw is not possible"

    def updated_balance(self):

        return self.__total_amount

    def __str__(self):
        return f"Name: {self.get_name()}, NID: {self.get_nid()}, Address: {self.get_address()}, Age: {self.get_age()}, Acc-No: {self.get_account_num()}, Balance: {self.updated_balance()} "


account = SavingsAccount("Zuheb", "48955", "Khilgaon", 26, "a1889", 500)
# account.deposit(1900)
# account.withdraw(600)
print(account.deposit(700))
# print(account.account_status("Zuheb","48955", 500))

