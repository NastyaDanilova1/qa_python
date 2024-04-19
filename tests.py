import pytest
from main import BooksCollector
from test_book_list import names_and_genres_of_books


class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book("Синий трактор")
        collector.add_new_book("Властелин колец - Две башни")
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
        "name", ["", "Легенды о короле Артуре и рыцарях Круглого Стола"]
    )
    def test_add_new_book_with_long_name_not_added(self, name, books_collector):
        books_collector.add_new_book(name)
        assert name not in books_collector.get_books_genre()

    def test_get_book_genre_return_genre_by_name(self, books_collector):
        name = "Синий трактор"
        books_collector.add_new_book(name)
        assert books_collector.get_book_genre(name) == ""

    def test_set_book_genre_add_genre(self, books_collector):
        name = "Кошмар на улице вязов"
        genre = "Ужасы"
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_by_genre(self, books_collector):
        name = "Дневник Бриджит Джонс"
        genre = "Комедии"
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert books_collector.get_books_with_specific_genre(genre) == [name]

    def test_get_books_genre_dict_books_genre_returned(
            self, books_collector, add_books, set_genre
    ):
        returned_books_genre_dict = books_collector.get_books_genre()
        expected_books_genre_dict = names_and_genres_of_books
        assert returned_books_genre_dict == expected_books_genre_dict

    def test_get_books_for_children_return_non_rating_books(
            self, books_collector, add_books, set_genre
    ):
        expected_books = [
            "Властелин колец - Две башни",
            "Синий трактор",
            "Дневник Бриджит Джонс",
        ]
        returned_books = books_collector.get_books_for_children()
        assert returned_books == expected_books

    def test_add_book_in_favorites_not_added_book_twice_in_favorite_book(
            self, books_collector
    ):
        books_collector.add_new_book("Дневник Бриджит Джонс")
        books_collector.add_book_in_favorites("Дневник Бриджит Джонс")
        books_collector.add_book_in_favorites("Дневник Бриджит Джонс")
        favorite_books = books_collector.get_list_of_favorites_books()
        assert len(favorite_books) == 1

    def test_add_book_in_favorite_one_added_book(self, books_collector):
        book = "Властелин колец - Две башни"
        books_collector.add_new_book(book)
        books_collector.add_book_in_favorites(book)
        favorite_books = books_collector.get_list_of_favorites_books()
        assert len(favorite_books) == 1 and favorite_books[0] == book

    def test_delete_book_from_favorites_not_deleted_book_if_book_not_in_favorite_books(
            self, books_collector
    ):
        books_collector.add_new_book("Дневник Бриджит Джонс")
        books_collector.add_book_in_favorites("Дневник Бриджит Джонс")
        books_collector.delete_book_from_favorites("Синий трактор")
        favorite_books = books_collector.get_list_of_favorites_books()
        assert len(favorite_books) == 1

    def test_delete_book_from_favorite_book_deleted(self, books_collector):
        books_collector.add_new_book("Дневник Бриджит Джонс")
        books_collector.add_book_in_favorites("Дневник Бриджит Джонс")
        books_collector.delete_book_from_favorites("Дневник Бриджит Джонс")
        favorite_books = books_collector.get_list_of_favorites_books()
        assert len(favorite_books) == 0

    def test_get_list_of_favorites_books_returned_list(
            self, books_collector, add_books
    ):
        for book in books_collector.get_books_genre():
            books_collector.add_book_in_favorites(book)
        returned_list = books_collector.get_list_of_favorites_books()
        expected_list = list(books_collector.get_books_genre())
        assert returned_list == expected_list
