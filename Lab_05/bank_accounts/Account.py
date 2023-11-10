import decimal


class Account:
    def __init__(self, name: str, balance: decimal.Decimal) -> None:
        self.name = name
        self.balance = balance

    def deposit(self, amount: decimal.Decimal) -> None:
        if amount < 0:
            print("Cannot deposit negative amount")
        else:
            self.balance += amount

    def withdraw(self, amount: decimal.Decimal) -> None:
        if amount < 0:
            print("Cannot withdraw negative amount")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def calculate_interest(self) -> decimal.Decimal:
        return self.balance * decimal.Decimal(0.0005)

    def __str__(self) -> str:
        return f"Account name: {self.name}, Balance: {self.balance}"

    def __repr__(self) -> str:
        return f"Account(name: {self.name}, balance: {self.balance})"

    def __eq__(self, other) -> bool:
        if isinstance(other, Account):
            return self.name == other.name and self.balance == other.balance
        return False

    def __hash__(self) -> int:
        return hash((self.name, self.balance))
