from animals.Animal import Animal


class Bird(Animal):
    def __init__(self, name: str, weight: float) -> None:
        super().__init__(name, weight)

    def fly(self) -> None:
        print(f"{self.name} is flying")

    def __str__(self) -> str:
        return f"Bird name: {self.name, self.weight}"

    def __repr__(self) -> str:
        return f"Bird(name: {self.name, self.weight})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Bird):
            return False
        return super().__eq__(other)