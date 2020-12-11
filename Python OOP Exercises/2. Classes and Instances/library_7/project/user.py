class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library):
        if book_name in library.books_available[author]:
            if self.username not in library.rented_books:
                # TODO check this here
                library.rented_books[self.username] = {book_name: days_to_return}
            else:
                library.rented_books[self.username][book_name] = days_to_return
            library.books_available[author].remove(book_name)
            self.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        days_until = ""
        for v in library.rented_books.values():
            for book, day in v.items():
                if book_name == book:
                    days_until = day

        return f'The book "{book_name}" is already rented and will be available in {days_until} days!'

    def return_book(self, author: str, book_name: str, library):
        if book_name in self.books:
            library.books_available[author].append(book_name)
            library.rented_books[self.username].pop(book_name)
            self.books.remove(book_name)
        else:
            return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return f"{', '.join(sorted(self.books))}"

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"