import json
from pathlib import Path
from json.decoder import JSONDecodeError
from dataclasses import dataclass, asdict, field


@dataclass
class Book:
    title: str
    author: str
    category: str
    publish_date: str = field(default="0000")
    def __post_init__(self):
        self.books = self.load_file()

    """def __init__(self, title: str, author: str, publish_date: str, category: str):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.category = category

        self.books = self.load_file()
    """

    def create_book(self):
        self.books.append(self._dict_())
        self.save(self.books)

    @staticmethod
    def save(books):
        with open("books.json", "w") as file:
            json.dump(books, file)

    def _dict_(self):
        return {
            "title": self.title,
            "author": self.author,
            "publish_date": self.publish_date,
            "category": self.category,
        }

    @staticmethod
    def load_file():
        try:
            with open(f"books.json", "r") as file:
                books = json.load(file)

        except (JSONDecodeError, FileNotFoundError) as exc:
            # if type(exc) is JSONDecodeError:
            return []

        return books

    @classmethod
    def delete_book(cls, title):
        books = cls.load_file()

        if len(books) > 0:
            for i, book in enumerate(books):
                if book["title"] == title:
                    books.pop(i)
                    cls.save(books)
                    break


if __name__ == "__main__":
    """book = Book("Cisne Negro", "Nassim T.", "1950", "Desenvolvimento Pessoal")
    book.create_book()
    book.delete_book("O Principe")"""
    book = Book(
        **{
            "title": "Cisne Negro",
            "author": "Nassim T.",
            "publish_date": "1950",
            "category": "Desenvolvimento Pessoal",
        }
    )
    print(asdict(book))
