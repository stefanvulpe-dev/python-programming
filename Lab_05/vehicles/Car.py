from vehicles.Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, name: str, model: str, year: int, color: str, max_speed: int) -> None:
        super().__init__(name, model, year)
        self.color = color
        self.max_speed = max_speed

    def __str__(self) -> str:
        return (f"Vehicle name: {self.name}, model: {self.model}, year: {self.year}, "
                f"color: {self.color}, max_speed: {self.max_speed}")

    def __repr__(self) -> str:
        return (f"Vehicle(name: {self.name}, model: {self.model}, year: {self.year}, "
                f"color: {self.color}, max_speed: {self.max_speed})")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Car):
            return False
        return (self.name == other.name and self.model == other.model and
                self.year == other.year and self.color == other.color and self.max_speed == other.max_speed)
