from animals.Animal import Animal


class Mammal(Animal):
    def __init__(self, name: str, weight: float) -> None:
        super().__init__(name, weight)

    def walk(self) -> None:
        print(f"{self.name} is walking")

    def get_milk_amount(self):
        return self.weight * 0.13

    def __str__(self) -> str:
        return f"Mammal name: {self.name, self.weight}"

    def __repr__(self) -> str:
        return f"Mammal(name: {self.name, self.weight})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Mammal):
            return False
        return super().__eq__(other)
