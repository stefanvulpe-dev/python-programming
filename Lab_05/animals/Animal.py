class Animal:
    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight

    def eat(self) -> None:
        print(f"{self.name} is eating")

    def drink_water(self) -> None:
        print(f"{self.name} is drinking water")

    def __str__(self) -> str:
        return f"Animal name: {self.name}, weight: {self.weight}"

    def __repr__(self) -> str:
        return f"Animal(name: {self.name}, weight: {self.weight})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Animal):
            return False
        return self.name == other.name and self.weight == other.weight
