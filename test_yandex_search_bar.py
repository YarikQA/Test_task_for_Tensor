import pytest
from yandex_pages.yandex_page import YandexSearchPage
from yandex_pages.yandex_page import YandexImagesPage
import keyboard  # для выполнения 5 шага первого тест-кейса
import time


@pytest.mark.skip
class TestYandexSearchBar:
    def test_tensor_is_on_finded_results(self, browser):
        link = "https://yandex.ru/"
        page = YandexSearchPage(browser, link)
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


@pytest.mark.images
class TestYandexImages:
    def test_yandex_images(self, browser):
        link = "https://yandex.ru/"
        page = YandexImagesPage(browser, link)
        page.open()
        page.user_should_see_images()
        page.click_on_the_images_link()
        time.sleep(3)
        page.current_url_is_yandex_images()
        page.click_on_the_first_image()
        page.current_page_is_first_image()


