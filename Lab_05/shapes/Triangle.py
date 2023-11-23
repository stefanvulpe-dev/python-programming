from shapes.Shape import Shape


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self) -> float:
        p = self.calculate_perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def calculate_perimeter(self) -> float:
        return self.a + self.b + self.c

    def __eq__(self, __o) -> bool:
        if isinstance(__o, Triangle):
            return self.a == __o.a and self.b == __o.b and self.c == __o.c
        return False

    def __hash__(self) -> int:
        return hash((self.a, self.b, self.c))

    def __str__(self) -> str:
        return f"Triangle with sides {self.a}, {self.b}, and {self.c}"

    def __repr__(self) -> str:
        return f"Triangle(a: {self.a}, b: {self.b}, c: {self.c})"
