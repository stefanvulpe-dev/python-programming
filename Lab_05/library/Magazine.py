from library.LibraryItem import LibraryItem


class Magazine(LibraryItem):
    def __init__(self, title: str, call_number: str, num_copies: int, issue_number: int) -> None:
        super().__init__(title, call_number, num_copies)
        self.issue_number = issue_number

    def __str__(self) -> str:
        return super().__str__() + f", Issue Number: {self.issue_number}"

    def __repr__(self) -> str:
        return super().__repr__() + f", issue_number: {self.issue_number}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Magazine):
            return False
        return super().__eq__(other) and self.issue_number == other.issue_number

    def check_availability(self) -> bool:
        return super().check_availability() and self.issue_number == 0
