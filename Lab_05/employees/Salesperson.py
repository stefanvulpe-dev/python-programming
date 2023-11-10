from employees.Employee import Employee


class Salesperson(Employee):
    def __init__(self, name, salary, commission):
        super().__init__(name, salary)
        self.commission = commission

    def get_salary(self):
        return super().get_salary() + self.commission

    def __str__(self) -> str:
        return f"Salesperson name: {self.name}, salary: {self.salary}, commission: {self.commission}"

    def __repr__(self) -> str:
        return f"Salesperson(name: {self.name}, salary: {self.salary}, commission: {self.commission})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Salesperson):
            return False
        return super().__eq__(other) and self.commission == other.commission
