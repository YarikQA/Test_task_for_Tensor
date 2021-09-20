from yandex_pages.base_page import BasePage
from yandex_pages.locators import YandexBasePageLocators, YandexPageAfterSearchLocators

file_name = "yandex_search_page.py"


# тут методы для работы с поисковой строкой и страницей Яндекса после поиска
class YandexSearchPage(BasePage):
    def user_should_see_search_bar(self):
        assert self.is_element_on_page(*YandexBasePageLocators.SEARCH_BAR), "Can't find the Search bar, file={}"\
            .format(file_name)

    def input_to_searchbar(self, text_to_input):
        search_bar = self.browser.find_element(*YandexBasePageLocators.SEARCH_BAR_FOR_INPUT)
        search_bar.send_keys(str(text_to_input))

    def click_to_search_button(self):
        search_button = self.browser.find_element(*YandexBasePageLocators.SEARCH_BUTTON)
        search_button.click()

    def user_should_see_suggest_list(self):
        assert self.is_element_on_page(*YandexBasePageLocators.SUGGEST_LIST), "Can't find suggest list, file={}"\
            .format(file_name)

    def tensor_in_first_result_of_search(self):
        self.is_element_on_page_with_wait(*YandexPageAfterSearchLocators.FIRST_RESULT_OF_URL)
        find_url = self.browser.find_element(*YandexPageAfterSearchLocators.FIRST_RESULT_OF_URL)
        result = find_url.get_attribute("href")
        assert "tensor.ru" in result, "The first website has no url with 'tensor.ru', file={}".format(file_name)

    def tensor_in_second_result_of_search(self):
        self.is_element_on_page_with_wait(*YandexPageAfterSearchLocators.SECOND_RESULT_OF_URL)
        find_url = self.browser.find_element(*YandexPageAfterSearchLocators.SECOND_RESULT_OF_URL)
        result = find_url.get_attribute("href")
        assert "tensor.ru" in result, "The second website has no url with 'tensor.ru', file={}".format(file_name)

    def tensor_in_third_result_of_search(self):
        self.is_element_on_page_with_wait(*YandexPageAfterSearchLocators.THIRD_RESULT_OF_URL)
        find_url = self.browser.find_element(*YandexPageAfterSearchLocators.THIRD_RESULT_OF_URL)
        result = find_url.get_attribute("href")
        assert "tensor.ru" in result, "The third website has no url with 'tensor.ru', file={}".format(file_name)

    def tensor_in_fourth_result_of_search(self):
        self.is_element_on_page_with_wait(*YandexPageAfterSearchLocators.FOURTH_RESULT_OF_URL)
        find_url = self.browser.find_element(*YandexPageAfterSearchLocators.FOURTH_RESULT_OF_URL)
        result = find_url.get_attribute("href")
        assert "tensor.ru" in result, "The fourth website has no url with 'tensor.ru', file={}".format(file_name)

    def tensor_in_fifth_result_of_search(self):
        self.is_element_on_page_with_wait(*YandexPageAfterSearchLocators.FIFTH_RESULT_OF_URL)
        find_url = self.browser.find_element(*YandexPageAfterSearchLocators.FIFTH_RESULT_OF_URL)
        result = find_url.get_attribute("href")
        assert "tensor.ru" in result, "The fifth website has no url with 'tensor.ru', file={}".format(file_name)
