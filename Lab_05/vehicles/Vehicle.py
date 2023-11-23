class Vehicle:
    def __init__(self, name: str, model: str, year: int) -> None:
        self.name = name
        self.model = model
        self.year = year
        self.millage_ratio = 0.5

    def get_millage(self) -> float:
        return (2023 - self.year) * 10000 * self.millage_ratio

    def __str__(self) -> str:
        return f"Vehicle name: {self.name}, model: {self.model}, year: {self.year}"

    def __repr__(self) -> str:
        return f"Vehicle(name: {self.name}, model: {self.model}, year: {self.year})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vehicle):
            return False
        return self.name == other.name and self.model == other.model and self.year == other.year
