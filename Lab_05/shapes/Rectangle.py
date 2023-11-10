from shapes.Shape import Shape


class Rectangle(Shape):
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        return self.length * self.width

    def calculate_perimeter(self) -> float:
        return 2 * (self.length + self.width)

    def __eq__(self, __o) -> bool:
        if isinstance(__o, Rectangle):
            return self.length == __o.length and self.width == __o.width
        return False

    def __hash__(self) -> int:
        return hash((self.length, self.width))

    def __str__(self) -> str:
        return f"Rectangle with length {self.length} and width {self.width}"

    def __repr__(self) -> str:
        return f"Rectangle(length: {self.length}, width: {self.width})"
