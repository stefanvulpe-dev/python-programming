class LibraryItem:
    def __init__(self, title: str, call_number: str, num_copies: int) -> None:
        self.title = title
        self.call_number = call_number
        self.num_copies = num_copies

    def __str__(self) -> str:
        return f"Title: {self.title}, Call Number: {self.call_number}, Number of Copies: {self.num_copies}"

    def __repr__(self) -> str:
        return f"LibraryItem(title: {self.title}, call_number: {self.call_number}, num_copies: {self.num_copies})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, LibraryItem):
            return False
        return self.title == other.title and self.call_number == other.call_number and self.num_copies == other.num_copies

    def check_availability(self) -> bool:
        return self.num_copies > 0

    def checkout(self):
        if self.check_availability():
            self.num_copies -= 1
            return True
        return False
