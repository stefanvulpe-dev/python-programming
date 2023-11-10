from animals.Animal import Animal


class Fish(Animal):
    def __init__(self, name: str, weight: float) -> None:
        super().__init__(name, weight)

    def swim(self) -> None:
        print(f"{self.name} is swimming")

    def __str__(self) -> str:
        return f"Fish name: {self.name, self.weight}"

    def __repr__(self) -> str:
        return f"Fish(name: {self.name, self.weight})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Fish):
            return False
        return super().__eq__(other)