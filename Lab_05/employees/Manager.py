from employees.Employee import Employee


class Manager(Employee):
    def __init__(self, name: str, age: int, salary: float, bonus: float, department: str) -> None:
        super().__init__(name, age, salary)
        self.bonus = bonus
        self.department = department

    def get_bonus(self) -> float:
        return self.bonus

    def get_department(self) -> str:
        return self.department

    def __str__(self) -> str:
        return f"Manager name: {self.name}, age: {self.age}, salary: {self.salary}, bonus: {self.bonus}"

    def __repr__(self) -> str:
        return f"Manager(name: {self.name}, age: {self.age}, salary: {self.salary}, bonus: {self.bonus})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Manager):
            return False
        return super().__eq__(other) and self.bonus == other.bonus
