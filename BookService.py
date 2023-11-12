from IBookRepository import IBookRepository
from Book import Book


# В Python нет интерфейсовБ поэтому пришлось импровизировать -заменил интерфейс абстрактынм классом и унаследовал от него
class BookService(IBookRepository):

    def __init__(self):
        self.books = []

    def add_book(self, *args):
        for i in args:
            if isinstance(i, Book):
                self.books.append(i)

    def find_book_by_id(self, id):
        for i in self.books:
            if i.id == id:
                return i

    def find_all(self):
        return [(i.id, i.title, i.author) for i in self.books]




# bs = BookService()
# bs.add_book(Book(1, 'Ernest', 'Cruzo'), Book(2, 'Jasmine', 'Mushketer'))
#
# print(bs.find_all())
