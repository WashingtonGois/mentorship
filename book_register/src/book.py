import json


class Book:
    def __init__(self, title: str, author: str, publish_date: str, category: str):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.category = category

    def save(self):
        with open("books.json", "w") as file:
            json.dump(self._dict_(), file)

    def _dict_(self):
        return {
            "title": self.title,
            "author": self.author,
            "publish_date": self.publish_date,
            "category": self.category,
        }
