from yandex_pages.base_page import BasePage
from yandex_pages.locators import BaseYandexPageLocators, AfterSearchYandexPageLocators, YandexImagesPageLocators


# тут методы для работы с поисковой строкой и страницей Яндекса после поиска
class YandexSearchPage(BasePage):
    def user_should_see_search_bar(self):
        assert self.is_element_on_page(*BaseYandexPageLocators.SEARCH_BAR), "Can't find the Search bar"

    def input_to_searchbar(self, text_to_input):
        search_bar = self.browser.find_element(*BaseYandexPageLocators.SEARCH_BAR_FOR_INPUT)
        search_bar.send_keys(str(text_to_input))

    def click_to_search_button(self):
        search_button = self.browser.find_element(*BaseYandexPageLocators.SEARCH_BUTTON)
        search_button.click()

    def user_should_see_suggest_list(self):
        assert self.is_element_on_page(*BaseYandexPageLocators.SUGGEST_LIST), "Can't find suggest list"

    def tensor_in_first_result_of_search(self):
        self.is_element_on_page_with_wait(*AfterSearchYandexPageLocators.FIRST_RESULT_OF_URL)
        find_url = self.browser.find_element(*AfterSearchYandexPageLocators.FIRST_RESULT_OF_URL)
        result = find_url.get_attribute("href")
        print(result)
        assert "tensor.ru" in result, "The first website has no url with 'tensor.ru' "

    def tensor_in_second_result_of_search(self):
        self.is_element_on_page_with_wait(*AfterSearchYandexPageLocators.SECOND_RESULT_OF_URL)
        find_url = self.browser.find_element(*AfterSearchYandexPageLocators.SECOND_RESULT_OF_URL)
        result = find_url.get_attribute("href")
        print(result)
        assert "tensor.ru" in result, "The second website has no url with 'tensor.ru' "

    def tensor_in_third_result_of_search(self):
        self.is_element_on_page_with_wait(*AfterSearchYandexPageLocators.THIRD_RESULT_OF_URL)
        find_url = self.browser.find_element(*AfterSearchYandexPageLocators.THIRD_RESULT_OF_URL)
        result = find_url.get_attribute("href")
        print(result)
        assert "tensor.ru" in result, "The third website has no url with 'tensor.ru' "

    def tensor_in_fourth_result_of_search(self):
        self.is_element_on_page_with_wait(*AfterSearchYandexPageLocators.FOURTH_RESULT_OF_URL)
        find_url = self.browser.find_element(*AfterSearchYandexPageLocators.FOURTH_RESULT_OF_URL)
        result = find_url.get_attribute("href")
        print(result)
        assert "tensor.ru" in result, "The fourth website has no url with 'tensor.ru' "

    def tensor_in_fifth_result_of_search(self):
        self.is_element_on_page_with_wait(*AfterSearchYandexPageLocators.FIFTH_RESULT_OF_URL)
        find_url = self.browser.find_element(*AfterSearchYandexPageLocators.FIFTH_RESULT_OF_URL)
        result = find_url.get_attribute("href")
        print(result)
        assert "tensor.ru" in result, "The fifth website has no url with 'tensor.ru' "


# Тут методы для работы со страницей Яндекс.Картинки
class YandexImagesPage(BasePage):
    def user_should_see_images(self):
        assert self.is_element_on_page(*BaseYandexPageLocators.IMAGES_PICTURE)

    def click_on_the_images_link(self):
        images_picture = self.browser.find_element(*BaseYandexPageLocators.IMAGES_PICTURE)
        images_picture.click()
        images_site = self.browser.window_handles[1]
        self.browser.switch_to.window(images_site)

    def current_url_is_yandex_images(self):
        current_url = self.browser.current_url
        assert "https://yandex.ru/images/" in current_url

    def click_on_the_first_image(self):
        first_image = self.browser.find_element(*YandexImagesPageLocators.FIRST_IMAGE)
        first_image.click()

    def get_url_of_first_image(self):
        first_image = self.browser.find_element(*YandexImagesPageLocators.FIRST_IMAGE)
        link_of_first_image = first_image.get_attribute("href")
        return link_of_first_image

    def current_page_is_first_image(self, get_url_of_first_image):
        current_url = self.browser.current_url
        assert current_url is get_url_of_first_image()
