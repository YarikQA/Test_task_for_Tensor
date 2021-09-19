from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


# Тут Базовые методы для работы с веб страницей, которые пригодятся в наследуемых классах
class BasePage:
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_on_page(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_on_page_with_wait(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            print("Can't find element with Explicit Waits")
            return False
        return True

    def move_mouse_to(self, how, what):  # метод для наведения мышки на элемент
        element_to_move = self.browser.find_element(how, what)
        hover = ActionChains(self.browser).move_to_element(element_to_move)
        hover.perform()

    def save_current_url(self):
        current_url = self.browser.current_url
        return current_url
