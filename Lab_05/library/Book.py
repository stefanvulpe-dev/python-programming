from library.LibraryItem import LibraryItem


class Book(LibraryItem):
    def __init__(self, title: str, call_number: str, num_copies: int, author: str, genre: str) -> None:
        super().__init__(title, call_number, num_copies)
        self.author = author
        self.genre = genre

    def get_author(self) -> str:
        return self.author

    def get_genre(self) -> str:
        return self.genre

    def __str__(self) -> str:
        return super().__str__() + f", Author: {self.author}, Genre: {self.genre}"

    def __repr__(self) -> str:
        return super().__repr__() + f", author: {self.author}, genre: {self.genre}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return False
        return super().__eq__(other) and self.author == other.author
