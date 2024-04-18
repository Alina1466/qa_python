# qa_python - Sprint_4

2 теста для метода add_new_book:

1 тест: test_add_new_book_add_one_book_with_different_lenght_name - параметризованный тест. Проверяю добавление в словарь books_genre книг с разной длиной наименования: в 1 символ, в 19 символов и в 40 символов - в пределах разрешенного диапазона длины наименования

2 тест: test_add_new_book_not_to_add_book_with_too_long_name_without_name - параметризованный тест. Проверяем, что добавить в словарь books_genre книг длина названия которых: 0 символов и более 40 символов - за пределами разрешенного диапазона длины наименования

Метод set_book_genre:
 - test_set_book_genre_add_genre_from_list_genre - проверяем добавление жанра для книги, который есть в списке жанров genre.

Метод get_book_genre:
- test_get_book_genre_get_right_genre_of_book_by_name_book - параметризованный тест. Проверяем соответствие выводимого жанра книги по её имени

Метод get_books_with_specific_genre:
- test_get_books_with_specific_genre_get_list_of_books_with_one_genre - проверяем правильность вывода списка книг имеющих один и тот же жанр

Метод get_books_genre:
- test_get_books_genre_return_current_books_genre - проверяем правильный вывод из словаря books_genre, который получаем методом get_books_genre содержание словаря books_genre.

Метод get_books_for_children:
- test_get_books_for_children_get_books_without_rating - проверяем, что метод не выводит в список книг для детей, которые им подходят. У жанра книги не должно быть возрастного рейтинга, который присутствует в списке genre_age_rating.

Метод add_book_in_favorites:
- test_add_book_in_favorites_add_book_from_books_genre - проверяем добавление книги, находящейся в словаре books_genre, в список favorites

Метод delete_book_from_favorites:
- test_delete_book_from_favorites_delete_one_book - проверяем удаляются ли книги, которые были добавлены в список favorites

Метод get_list_of_favorites_books:
- test_get_list_of_favorites_books_get_whole_list_books_from_favorites - проверяем соответствие списка, получаемого методом get_list_of_favorites_books в список favorites