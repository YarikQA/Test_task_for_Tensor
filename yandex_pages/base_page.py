from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

file_name = "base_page.py"


# Тут Базовые методы для работы с веб страницей, которые пригодятся в наследуемых классах
class BasePage:
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_on_page(self, how, what):  # проверка, что на странице есть нужный элемент
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_on_page_with_wait(self, how, what, timeout=5):  # проверка с явным ожиданием, что на странице есть
        # нужный элемент
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            print("Can't find element with Explicit Wait, file={}".format(file_name))
            return False
        return True

    def move_mouse_to(self, how, what):  # метод для наведения мышки на элемент
        element_to_move = self.browser.find_element(how, what)
        hover = ActionChains(self.browser).move_to_element(element_to_move)
        hover.perform()

    def is_url_changed(self, what, timeout=5):  # проверка на изменение url
        try:
            WebDriverWait(self.browser, timeout).until(ec.url_changes(what))
        except TimeoutException:
            print("Url isn't changing, file={}".format(file_name))
            return False
        return True
