import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize('name_book', ['А', 'Алиса в стране чуда', 'Невероятная грустная история о Эренндире'])
    def test_add_new_book_add_one_book_with_different_lenght_name(self, name_book):
        collector = BooksCollector()
        collector.add_new_book(name_book)
        expected_result = {name_book: ''}
        actual_result = collector.get_books_genre()
        assert actual_result == expected_result

    @pytest.mark.parametrize('name_book', ['', 'Удивительное путешествие Нильса Хольгерсона'])
    def test_add_new_book_not_to_add_book_with_too_long_name_without_name(self, name_book):
        collector = BooksCollector()
        collector.add_new_book(name_book)
        expected_result = {}
        actual_result = collector.get_books_genre()
        assert actual_result == expected_result

    def test_set_book_genre_add_genre_from_list_genre(self):
        collector = BooksCollector()
        name_book = 'Семь ликов страха'
        genre_book = 'Ужасы'
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre_book)
        result = collector.get_book_genre(name_book)
        assert result == genre_book

    @pytest.mark.parametrize('name_book, genre_book', [['Фауст', 'Комедии'],
                                                       ['Алиса в стране чуда', 'Мультфильмы'],
                                                       ['Четвёртое крыло', 'Фантастика'],
                                                       ['Я знаю, что видел', 'Детективы'],
                                                       ['Семь ликов страха', 'Ужасы']])
    def test_get_book_genre_get_right_genre_of_book_by_name_book(self, name_book, genre_book):
        collector = BooksCollector()
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre_book)
        result = collector.get_book_genre(name_book)
        assert result == genre_book

    def test_get_books_with_specific_genre_get_list_of_books_with_one_genre(self):
        collector = BooksCollector()
        name_book_1 = 'Семь ликов страха'
        name_book_2 = 'Шкатулка'
        name_book_3 = 'Я знаю, что видел'
        genre_book_horror = 'Ужасы'
        genre_book_detective = 'Детективы'
        collector.add_new_book(name_book_1)
        collector.set_book_genre(name_book_1, genre_book_horror)
        collector.add_new_book(name_book_2)
        collector.set_book_genre(name_book_2, genre_book_horror)
        collector.add_new_book(name_book_3)
        collector.set_book_genre(name_book_3, genre_book_detective)
        result = collector.get_books_with_specific_genre(genre_book_horror)
        assert result == [name_book_1, name_book_2]

    def test_get_books_genre_return_current_books_genre(self):
        collector = BooksCollector()
        name_book = 'Семь ликов страха'
        genre_book = 'Ужасы'
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre_book)
        expected_result = {name_book: genre_book}
        actual_result = collector.get_books_genre()
        assert actual_result == expected_result

    def test_get_books_for_children_get_books_without_rating(self):
        collector = BooksCollector()
        name_book_1 = 'Семь ликов страха'
        name_book_2 = 'Четвёртое крыло'
        genre_book_horror = 'Ужасы'
        genre_book_fantasy = 'Фантастика'
        collector.add_new_book(name_book_1)
        collector.set_book_genre(name_book_1, genre_book_horror)
        collector.add_new_book(name_book_2)
        collector.set_book_genre(name_book_2, genre_book_fantasy)
        expected_result = [name_book_2]
        actual_result = collector.get_books_for_children()
        assert actual_result == expected_result

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        name_book = 'Семь ликов страха'
        collector.add_new_book(name_book)
        collector.add_book_in_favorites(name_book)
        collector.delete_book_from_favorites(name_book)
        expected_result = []
        actual_result = collector.get_list_of_favorites_books()
        assert actual_result == expected_result and len(actual_result) == 0

    def test_add_book_in_favorites_add_book_from_books_genre(self):
        collector = BooksCollector()
        name_book = 'Семь ликов страха'
        collector.add_new_book(name_book)
        collector.add_book_in_favorites(name_book)
        expected_result = [name_book]
        actual_result = collector.get_list_of_favorites_books()
        assert actual_result == expected_result and len(actual_result) == 1

    def test_get_list_of_favorites_books_get_whole_list_books_from_favorites(self):
        collector = BooksCollector()
        name_book_1 = 'Семь ликов страха'
        name_book_2 = 'Я знаю, что видел'
        collector.add_new_book(name_book_1)
        collector.add_new_book(name_book_2)
        collector.add_book_in_favorites(name_book_1)
        collector.add_book_in_favorites(name_book_2)
        expected_result = [name_book_1, name_book_2]
        actual_result = collector.get_list_of_favorites_books()
        assert actual_result == expected_result and len(actual_result) == 2
