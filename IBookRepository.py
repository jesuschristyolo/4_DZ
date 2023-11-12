from abc import abstractmethod, ABC


class IBookRepository(ABC):

    @abstractmethod
    def find_book_by_id(self, id):
        pass

    @abstractmethod
    def find_all(self):
        pass
