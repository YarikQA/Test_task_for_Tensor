import pytest
from yandex_pages.yandex_search_page import YandexSearchPage
from yandex_pages.yandex_images_page import YandexImagesPage
import keyboard  # для выполнения 5 шага первого тест-кейса
import time


@pytest.mark.search
@pytest.mark.xfail
class TestYandexSearchBar:  # Тесты поисковой строки
    def test_tensor_is_on_finded_results(self, browser):
        link = "https://yandex.ru/"
        page = YandexSearchPage(browser, link)
        page.open()
        page.user_should_see_search_bar()
        page.input_to_searchbar("Тензор")
        page.user_should_see_suggest_list()
        keyboard.send("enter")  # имитация нажатия пользователем на Enter

        # проверка 5 url(результатов поиска) на наличие 'tensor.ru'
        page.tensor_in_first_result_of_search()
        page.tensor_in_second_result_of_search()
        page.tensor_in_third_result_of_search()
        page.tensor_in_fourth_result_of_search()
        page.tensor_in_fifth_result_of_search()


@pytest.mark.images
class TestYandexImages:  # Тесты страницы Яндекс.Картинки
    def test_yandex_images(self, browser):
        link = "https://yandex.ru/"
        page = YandexImagesPage(browser, link)
        page.open()
        page.user_should_see_images_icon()
        page.click_on_the_images_link()
        page.current_url_is_yandex_images()

        page.click_on_the_first_category()
        page.current_page_is_not_yandex_images()  # Если открыта НЕ базовая страница, значит открылся url 1 категории
        page.get_text_of_category_in_search_bar()
        page.name_of_category_is_text_in_search_bar()
        page.click_on_first_image()
        page.picture_is_changing_after_click_forward_and_behind()

