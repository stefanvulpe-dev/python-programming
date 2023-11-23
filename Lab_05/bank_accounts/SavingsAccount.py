import decimal

from bank_accounts.Account import Account


class SavingsAccount(Account):
    def __init__(self, name: str, balance: decimal.Decimal, minimum_balance: decimal.Decimal) -> None:
        self.minimum_balance = minimum_balance
        super().__init__(name, balance)

    def withdraw(self, amount: decimal.Decimal) -> None:
        if amount < 0:
            print("Cannot withdraw negative amount")
        elif self.balance < self.minimum_balance:
            print("Must maintain a minimum balance of $150")
        else:
            self.balance -= amount

    def __str__(self) -> str:
        return f"Savings Account name: {self.name}, Balance: {self.balance}"

    def __repr__(self) -> str:
        return f"Savings Account(name: {self.name}, balance: {self.balance})"

    def __eq__(self, other) -> bool:
        if isinstance(other, SavingsAccount):
            return self.name == other.name and self.balance == other.balance
        return False

    def __hash__(self) -> int:
        return hash((self.name, self.balance))