from typing import List


class Book:
    def __init__(self, title: str, author: str, issued: int, copies: int):
        self._title = title
        self._author = author
        self._issued = issued
        self._copies = copies

    def __str__(self):
        return f'Title: "{self.title}", Author: "{self.author}"'

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        if value:
            self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value: str):
        if value:
            self._author = value

    @property
    def copies(self):
        return self._copies

    @copies.setter
    def copies(self, value: str):
        if value >= 0:
            self._copies = value


class Library():
    def __init__(self, books: List[Book] = []):
        self.books = books

    def __str__(self):
        return '\n'.join([x.__str__() for x in self.books])

    def add_book(self, book: Book):
        self.books.append(book)

    def delete_book(self, title: str):
        found = [x for x in self.books if x.title == title]
        if found:
            self.books.remove(found[0])

    def search_book(self, contains: str):
        found = [x for x in self.books if x.title.lower() == contains.lower()]
        if found:
            return found[0]


if __name__ == "__main__":
    lib = Library([Book('abc', 'abc', 2000, 1000), Book('abcd', 'abcd', 1950, 1500)])
    lib.add_book(Book('X', 'Mono', 2020, 5000))
    lib.delete_book('abcd')
    print(lib)
    print(lib.search_book('abc'))
