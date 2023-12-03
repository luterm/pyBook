import unittest
from book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Wiedzmin", "Sapkowski", 2000)

    def test_get_info(self):
        text_correct = "Książka: Wiedzmin Autor: Sapkowski Rok:2000"
        text_result = self.book.get_info()
        self.assertEqual(text_correct, text_result)

    def test_change_title(self):
        self.book.change_title("Ogniem i mieczami")
        self.assertEqual("ogniem i mieczami", self.book.title)

    def test_change_author(self):
        self.book.change_author("Marian z Bydgoszczy")
        self.assertEqual("Marian z Bydgoszczy", self.book.author)

    def test_change_year(self):
        self.book.change_year(2828)
        self.assertEqual(2000, self.book.year)


if __name__ == '__main__':
    unittest.main()
