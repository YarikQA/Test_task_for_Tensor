import pytest
from yandex_pages.yandex_page import YandexPage
import keyboard  # для выполнения 5 шага первого тест-кейса


class TestYandexSearchBar:
    def test_tensor_is_on_finded_results(self, browser):
        link = "https://yandex.ru/"
        page = YandexPage(browser, link)
        page.open()
        page.user_should_see_search_bar()
        page.input_to_searchbar("Тензор")
        page.user_should_see_suggest_list()
        keyboard.send("enter")  # имитация нажатия пользователем на Enter

        # проверка 5 url на наличие 'tensor.ru'
        page.tensor_in_first_result_of_search()
        page.tensor_in_second_result_of_search()
        page.tensor_in_third_result_of_search()
        page.tensor_in_fourth_result_of_search()
        page.tensor_in_fifth_result_of_search()
