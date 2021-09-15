from yandex_pages.base_page import BasePage
from yandex_pages.locators import BaseYandexPageLocators


class YandexPage(BasePage):
    def user_should_see_search_bar(self):
        assert self.is_element_on_page(*BaseYandexPageLocators.SEARCH_BAR), "Can't find the Search bar"

    def input_to_searchbar(self, text_to_input):
        search_bar = self.browser.find_element(*BaseYandexPageLocators.SEARCH_BAR_FOR_INPUT)
        search_bar.send_keys(str(text_to_input))
        #assert isinstance(text_to_input, str)

    def click_to_search_button(self):
        search_button = self.browser.find_element(*BaseYandexPageLocators.SEARCH_BUTTON)
        search_button.click()

    def user_should_see_suggest_list(self):
        assert self.is_element_on_page(*BaseYandexPageLocators.SUGGEST_LIST), "Can't find suggest list"
