from selenium.webdriver.common.by import By


class BaseYandexPageLocators:
    SEARCH_BAR = (By.CSS_SELECTOR, "div .home-arrow__search form")
    SEARCH_BAR_FOR_INPUT = (By.CSS_SELECTOR, "span .input__box [tabindex='2']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".home-arrow__search .search2__button")
    # Если понадобится нажимать на кнопку "Найти" вместо Enter
    SUGGEST_LIST = (By.CSS_SELECTOR, "[role='listbox']")

