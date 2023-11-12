class Descriptor:

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Book:
    # В этом классе проесс инкапсуляции происходит
    # с помощью Дескрипторов - присваиваемые пользователем атрибуты сначала
    # проходят через дескриптор, а затем проходят в конструктор класса Book,
    # это очень удобно когда нужно инкапсулировать
    # большое количество атрибутов чтобы тысячу раз не прописывать декоратор property (в python это очень долго)

    id = Descriptor()
    title = Descriptor()
    author = Descriptor()

    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author


# b = Book(0, 'Norman', 'Xui')
# b.id = 1
# print(b.__dict__)
# print(b.author)
