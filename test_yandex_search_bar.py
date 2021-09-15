import pytest
from yandex_pages.yandex_page import YandexPage
import keyboard  # для выполнения 5 шага первого тест-кейса
import time


class TestYandexSearchBar:
    def test_tensor_is_on_find_results(self, browser):
        link = "https://yandex.ru/"
        page = YandexPage(browser, link)
        page.open()
        page.user_should_see_search_bar()
        page.input_to_searchbar("Тензор")
        page.user_should_see_suggest_list()
        keyboard.send("enter")  # имитация нажатия пользователем на Enter
        time.sleep(5)
