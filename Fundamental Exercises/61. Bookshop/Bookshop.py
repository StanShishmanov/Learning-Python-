class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = float(price)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if len(title) < 3:
            raise Exception("Title not valid!")
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        author_name = author.split()
        if len(author_name) > 1:
            second_name = author.split()[1]
            if second_name[0].isdigit():
                raise Exception("Author not valid!")
        self.__author = author

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise Exception("Price not valid!")
        self.__price = price

    def __str__(self):
        return f'Type: Book\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}'


class GoldenEditionBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author, price)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise Exception("Price not valid!")
        self.__price = price + price * 0.3

    def __str__(self):
        return f'Type: GoldenEditionBook\nTitle: {self.title}\nAuthor: {self.author}\nPrice: {self.price:.2f}'


try:
    title = input()
    author = input()
    price = input()

    book = Book( author, title, price)
    golden_edition_book = GoldenEditionBook(author, title, price)

    print(book)
    print()
    print(golden_edition_book)

except Exception as exc:
    print(exc)