from typing import List, Optional, Tuple, Dict
from datetime import datetime, timedelta


class BookNotFoundException(Exception):
    """Книга не найдена"""


class BookLimitExceededException(Exception):
    """Читатель достиг лимита книг"""


class BookAlreadyBorrowedException(Exception):
    """Книга уже выдана"""


class ReaderNotFoundException(Exception):
    """Читатель не нгайден"""


class Book:
    """ Класс, представляющий книгу """

    def __init__(self, title: str, author: str, isbn: str, year: int):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__year = year
        self.__is_borrowed = False
        self.__borrowed_by: Optional['Reader'] = None
        self.__due_date: Optional[datetime] = None

    @property
    def title(self) -> str:
        return self.__title

    @property
    def author(self) -> str:
        return self.__author

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def year(self) -> int:
        return self.__year

    @property
    def is_borrowed_by(self) -> bool:
        return self.__borrowed_by

    @property
    def borrowed_by(self) -> Optional['Reader']:
        return self.__borrowed_by

    @property
    def due_date(self) -> Optional[datetime]:
        return self.__due_date

    def borrow(self, reader: 'Reader'):
        """Выдать книгу читателю."""
        if self.__is_borrowed_by:
            raise BookAlreadyBorrowedException(
                f'Книга {self.__title}  уже выдана!')

