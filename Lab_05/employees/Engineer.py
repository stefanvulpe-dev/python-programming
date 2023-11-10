from employees.Employee import Employee


class Engineer(Employee):
    def __init__(self, name: str, age: int, salary: float, bonus: float, skill: str) -> None:
        super().__init__(name, age, salary)
        self.bonus = bonus
        self.skill = skill

    def get_bonus(self) -> float:
        return self.bonus

    def get_skill(self) -> str:
        return self.skill

    def __str__(self) -> str:
        return f"Engineer name: {self.name}, age: {self.age}, salary: {self.salary}, bonus: {self.bonus}"

    def __repr__(self) -> str:
        return f"Engineer(name: {self.name}, age: {self.age}, salary: {self.salary}, bonus: {self.bonus})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Engineer):
            return False
        return super().__eq__(other) and self.bonus == other.bonus and self.skill == other.skill
