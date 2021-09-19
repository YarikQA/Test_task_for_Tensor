from yandex_pages.base_page import BasePage
from yandex_pages.locators import YandexBasePageLocators, YandexImagesPageLocators


# Тут дополнительные необходимые методы для работы с 'Яндекс.Картинки'
class YandexImagesPageElements(BasePage):
    def get_name_of_first_category(self):
        name_of_first_category = self.browser.find_element(*YandexImagesPageLocators.NAME_OF_FIRST_CATEGORY).text
        return name_of_first_category

    def get_text_of_category_in_search_bar(self):
        text_in_search_bar_finder = self.browser.find_element(*YandexImagesPageLocators.TEXT_IN_SEARCH_BAR)
        text_in_search_bar = text_in_search_bar_finder.get_attribute("value")
        return text_in_search_bar

    def get_current_url(self):
        current_url = self.browser.current_url
        return current_url

    def click_to_next_image(self):
        self.move_mouse_to(*YandexImagesPageLocators.OPENED_IMAGE)
        click_forward_button = self.browser.find_element(*YandexImagesPageLocators.NEXT_PICTURE_ICON)
        click_forward_button.click()

    def click_to_previous_image(self):
        self.move_mouse_to(*YandexImagesPageLocators.OPENED_IMAGE)
        click_behind_button = self.browser.find_element(*YandexImagesPageLocators.PREVIOUS_PICTURE_ICON)
        click_behind_button.click()

    def get_picture(self):
        picture = self.browser.find_element(*YandexImagesPageLocators.OPENED_IMAGE)
        picture = picture.get_attribute("src")
        return picture


# Тут основные методы для работы с 'Яндекс.Картинки'
class YandexImagesPage(YandexImagesPageElements):
    def user_should_see_images_icon(self):
        assert self.is_element_on_page(*YandexBasePageLocators.IMAGES_PICTURE), "Can't find 'images' picture on the " \
                                                                                "page "

    def click_on_the_images_link(self):  # переход на страницу 'Яндекс.Картинки'
        images_picture = self.browser.find_element(*YandexBasePageLocators.IMAGES_PICTURE)
        images_picture.click()
        images_site = self.browser.window_handles[1]
        self.browser.switch_to.window(images_site)

    def current_url_is_yandex_images(self):
        current_url = self.browser.current_url
        assert "https://yandex.ru/images/" in current_url, "current page isn't Yandex.Image"

    def click_on_the_first_category(self):
        first_image = self.browser.find_element(*YandexImagesPageLocators.FIRST_CATEGORY)
        first_image.click()

    def current_page_is_not_yandex_images(self):
        error_text = "current url is Yandex.Images Base page, should be url of 1st category of Pictures"
        current_url = self.browser.current_url
        assert current_url != "https://yandex.ru/images/" and \
               current_url != "https://yandex.ru/images/?utm_source=main_stripe_big", "{}".format(error_text)

    def name_of_category_is_text_in_search_bar(self):
        assert self.get_text_of_category_in_search_bar() == self.get_name_of_first_category(), \
            "Wrong text in the search bar, should be text of first category"

    def click_on_first_image(self):
        first_image = self.browser.find_element(*YandexImagesPageLocators.FIRST_IMAGE)
        first_image.click()

    # def first_picture_was_open(self): Сделать проверку, что открыта нужная картинка

    def picture_is_changing_after_click_forward_and_behind(self):
        old_picture = self.get_picture()
        self.click_to_next_image()
        self.is_element_on_page_with_wait(*YandexImagesPageLocators.OPENED_IMAGE)
        new_picture = self.get_picture()
        if old_picture != new_picture:  # Если картинки не равны, то откроет прошлую и сравнит ее с картинкой из 6 шага
            self.click_to_previous_image()
            self.is_element_on_page_with_wait(*YandexImagesPageLocators.OPENED_IMAGE)
            new_old_picture = self.get_picture()
            assert new_old_picture == old_picture, "This picture is not equal to the picture from step 6"
        else:  # Иначе выкинет Assertion Error
            assert old_picture != new_picture, "The new image is equal to the old image, there is an error somewhere"

# а еще, я не придумал, как достать old_picture из 1 строчки функции, чтобы сделать эту проверку в 2 разных теста
