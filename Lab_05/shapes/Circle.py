from shapes.Shape import Shape


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calculate_area(self) -> float:
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self) -> float:
        return 2 * 3.14 * self.radius

    def __eq__(self, __o) -> bool:
        if isinstance(__o, Circle):
            return self.radius == __o.radius
        return False

    def __hash__(self) -> int:
        return hash(self.radius)

    def __str__(self) -> str:
        return f"Circle with radius {self.radius}"

    def __repr__(self) -> str:
        return f"Circle(radius: {self.radius})"
