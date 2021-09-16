from yandex_pages.base_page import BasePage
from yandex_pages.locators import BaseYandexPageLocators
from yandex_pages.locators import AfterSearchYandexPageLocators

# тут методы для работы со страницей Яндекс
class YandexPage(BasePage):
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

    #  Сделать через getattribute и взять href
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
