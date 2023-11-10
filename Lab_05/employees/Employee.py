class Employee:
    def __init__(self, name: str, age: int, salary: float) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def get_salary(self) -> float:
        return self.salary

    def __str__(self) -> str:
        return f"Employee name: {self.name}, age: {self.age}, salary: {self.salary}"

    def __repr__(self) -> str:
        return f"Employee(name: {self.name}, age: {self.age}, salary: {self.salary})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Employee):
            return False
        return self.name == other.name and self.age == other.age and self.salary == other.salary


