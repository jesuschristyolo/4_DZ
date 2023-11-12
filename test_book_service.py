import unittest

from BookService import BookService
from Book import Book
from unittest.mock import patch, Mock


class TestBookService(unittest.TestCase):
    def setUp(self) -> None:
        self.bs = BookService()

    def test_add_book(self):
        self.bs.add_book(Book(1, 'Ernest', 'Cruzo'), Book(2, 'Jasmine', 'Mushketer'))
        self.assertEqual(len(self.bs.books), 2)

        self.bs.add_book(123)
        self.assertEqual(len(self.bs.books), 2)

    def test_find_all(self):
        self.bs.add_book(Book(1, 'Ernest', 'Cruzo'), Book(2, 'Jasmine', 'Mushketer'))
        self.assertEqual(self.bs.find_all(), [(1, 'Ernest', 'Cruzo'), (2, 'Jasmine', 'Mushketer')])

    @patch('BookService.BookService.find_book_by_id', return_value=1)
    def test_find_book_by_id(self, mock_find_book_by_id):
        self.assertEqual(mock_find_book_by_id(1), 1)
        mock_find_book_by_id.assert_called_once()


if __name__ == '__main__':
    unittest.main()
