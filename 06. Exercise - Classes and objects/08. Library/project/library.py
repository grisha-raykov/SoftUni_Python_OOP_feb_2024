from typing import List, Dict

from user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str: List[str]] = {}
        self.rented_books: Dict[User: Dict[str:int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            user.books.append(book_name)

            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}
            return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author: str, user: User, book_name: str):
        pass
