import decimal

from bank_accounts.Account import Account


class CheckingAccount(Account):
    def __init__(self, name: str, balance: decimal.Decimal) -> None:
        super().__init__(name, balance)

    def __str__(self) -> str:
        return f"Checking Account name: {self.name}, Balance: {self.balance}"

    def __repr__(self) -> str:
        return f"Checking Account(name: {self.name}, balance: {self.balance})"

    def __eq__(self, other) -> bool:
        if isinstance(other, CheckingAccount):
            return self.name == other.name and self.balance == other.balance
        return False

    def __hash__(self) -> int:
        return hash((self.name, self.balance))
