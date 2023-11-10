from vehicles.Vehicle import Vehicle


class Truck(Vehicle):
    def __init__(self, name: str, model: str, year: int, color: str, max_speed: int, towing_capacity: int) -> None:
        super().__init__(name, model, year)
        self.color = color
        self.max_speed = max_speed
        self.towing_capacity = towing_capacity

    def get_millage(self) -> float:
        return (2023 - self.year) * 10000 * self.millage_ratio * 1.5

    def get_towing_capacity(self) -> int:
        return self.towing_capacity

    def __str__(self) -> str:
        return (f"Vehicle name: {self.name}, model: {self.model}, year: {self.year}, "
                f"color: {self.color}, max_speed: {self.max_speed}, capacity: {self.towing_capacity}")

    def __repr__(self) -> str:
        return (f"Vehicle(name: {self.name}, model: {self.model}, year: {self.year}, "
                f"color: {self.color}, max_speed: {self.max_speed}, capacity: {self.towing_capacity})")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Truck):
            return False
        return (self.name == other.name and self.model == other.model and
                self.year == other.year and self.color == other.color and
                self.max_speed == other.max_speed and self.towing_capacity == other.towing_capacity)
