from library.LibraryItem import LibraryItem


class DVD(LibraryItem):
    def __init__(self, title: str, call_number: str, num_copies: int, release_date: str, region_code: int) -> None:
        super().__init__(title, call_number, num_copies)
        self.release_date = release_date
        self.region_code = region_code

    def __str__(self) -> str:
        return super().__str__() + f", Release Date: {self.release_date}, Region Code: {self.region_code}"

    def __repr__(self) -> str:
        return super().__repr__() + f", release_date: {self.release_date}, region_code: {self.region_code}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, DVD):
            return False
        return super().__eq__(other) and self.release_date == other.release_date and self.region_code == other.region_code

    def check_availability(self) -> bool:
        return super().check_availability() and self.region_code == 0
