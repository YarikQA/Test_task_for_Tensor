from yandex_pages.base_page import BasePage
from yandex_pages.locators import YandexBasePageLocators, YandexImagesPageLocators

file_name = "yandex_images_page.py"


# Тут дополнительные необходимые методы для работы с 'Яндекс.Картинки'
class YandexImagesPageElements(BasePage):
    def get_name_of_first_category(self):
        name_of_first_category = self.browser.find_element(*YandexImagesPageLocators.NAME_OF_FIRST_CATEGORY).text
        return name_of_first_category

    def get_text_of_category_in_search_bar(self):  # Возвращает текст из поисковой строки, который должен быть равен
        # названию категории
        text_in_search_bar_finder = self.browser.find_element(*YandexImagesPageLocators.TEXT_IN_SEARCH_BAR)
        text_in_search_bar = text_in_search_bar_finder.get_attribute("value")
        return text_in_search_bar

    def click_to_next_image(self):  # открытие следующей картинки по стрелочке 'вперед'
        self.move_mouse_to(*YandexImagesPageLocators.OPENED_IMAGE)
        click_forward_button = self.browser.find_element(*YandexImagesPageLocators.NEXT_PICTURE_ICON)
        click_forward_button.click()

    def click_to_previous_image(self):  # открытие предыдущей картинки по стрелочке 'назад'
        self.move_mouse_to(*YandexImagesPageLocators.OPENED_IMAGE)
        click_behind_button = self.browser.find_element(*YandexImagesPageLocators.PREVIOUS_PICTURE_ICON)
        click_behind_button.click()


# Тут основные методы для работы с 'Яндекс.Картинки'
class YandexImagesPage(YandexImagesPageElements):
    def user_should_see_images_icon(self):
        assert self.is_element_on_page(*YandexBasePageLocators.IMAGES_PICTURE), "Can't find 'images' icon on the " \
                                                                                "page, file={}".format(file_name)

    def click_on_the_images_link(self):  # переход на страницу 'Яндекс.Картинки'
        images_picture = self.browser.find_element(*YandexBasePageLocators.IMAGES_PICTURE)
        images_picture.click()
        images_site = self.browser.window_handles[1]
        self.browser.switch_to.window(images_site)

    def current_url_is_yandex_images(self):
        current_url = self.browser.current_url
        assert "https://yandex.ru/images/" in current_url, "current page isn't Yandex.Image, file={}".format(file_name)

    def click_on_the_first_category(self):  # открытие первой категории в Яндекс.Картинки
        first_image = self.browser.find_element(*YandexImagesPageLocators.FIRST_CATEGORY)
        first_image.click()

    def current_page_is_not_yandex_images(self):
        error_text = "current page is Yandex.Images Base page, should be page of 1st category of Pictures, file={}" \
            .format(file_name)
        current_url = self.browser.current_url
        assert current_url != "https://yandex.ru/images/" and \
               current_url != "https://yandex.ru/images/?utm_source=main_stripe_big", "{}".format(error_text)

    def name_of_category_is_text_in_search_bar(self):
        assert self.get_text_of_category_in_search_bar() == self.get_name_of_first_category(), \
            "Wrong text in the search bar, should be text of first category, file={}".format(file_name)

    def click_on_first_image(self):
        first_image = self.browser.find_element(*YandexImagesPageLocators.FIRST_IMAGE)
        first_image.click()
        assert self.is_element_on_page_with_wait(*YandexImagesPageLocators.OPENED_IMAGE), \
            "The first picture was not opened, file={}".format(file_name)

    def picture_is_changing_after_click_forward_and_behind(self):  # Проверка, что картинка меняется после нажатия
        # стрелочки "вперед" и проверка того, что при нажатии стрелочки "назад" это будет картинка из 1 действия
        old_picture = self.browser.current_url
        self.click_to_next_image()
        self.is_url_changed(old_picture)
        picture_after_click_forward = self.browser.current_url
        if old_picture != picture_after_click_forward:  # Если картинки не равны, то откроет прошлую и сравнит ее с
            # картинкой до кликов
            self.click_to_previous_image()
            self.is_url_changed(picture_after_click_forward)
            picture_after_click_back = self.browser.current_url
            assert old_picture == picture_after_click_back, "Opened picture is not equal to the picture from step 6, " \
                                                            "file={}".format(file_name)
        else:  # Иначе выкинет Assertion Error
            assert old_picture != picture_after_click_forward, "The new image is equal to the previous image, there " \
                                                               "is an error somewhere, file={}".format(file_name)
