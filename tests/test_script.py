
import pytest
import allure
from main import update_users, update_books, make_json
import os
import json


TEST_USERS_FILE = 'files/test_users.json'
TEST_BOOKS_FILE = 'files/test_books.csv'
TEST_OUTPUT_FILE = 'files/test_reference.json'

@pytest.fixture(scope="module")
def setup():
    pass

@allure.feature('Обработка данных о пользователях')
@allure.story('Обновление данных о пользователях из JSON')
def test_update_users(setup):
    with allure.step("Загрузка и обновление данных о пользователях"):
        users = update_users(TEST_USERS_FILE)
        assert isinstance(users, list), "Данные о пользователях должны быть в виде списка"
        assert len(users) > 0, "Список пользователей не должен быть пустым"

@allure.feature('Обработка данных о книгах')
@allure.story('Обновление данных о книгах из CSV')
def test_update_books(setup):
    with allure.step("Загрузка и обновление данных о книгах"):
        books = update_books(TEST_BOOKS_FILE)
        assert isinstance(books, list), "Данные о книгах должны быть в виде списка"
        assert len(books) > 0, "Список книг не должен быть пустым"

@allure.feature('Генерация JSON')
@allure.story('Генерация объединенного JSON')
def test_make_json(setup):
    with allure.step("Генерация объединенного файла JSON"):
        users = update_users(TEST_USERS_FILE)
        books = update_books(TEST_BOOKS_FILE)
        make_json(users, books, TEST_OUTPUT_FILE)
        assert os.path.exists(TEST_OUTPUT_FILE), "Файл JSON вывода не был создан"

        with open(TEST_OUTPUT_FILE, 'r') as f:
            data = json.load(f)
            assert isinstance(data, list), "Вывод должен быть в виде списка"
            assert len(data) > 0, "Список вывода не должен быть пустым"
