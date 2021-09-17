from selenium.webdriver.common.by import By


class BaseYandexPageLocators:
    SEARCH_BAR = (By.CSS_SELECTOR, "div .home-arrow__search form")
    SEARCH_BAR_FOR_INPUT = (By.CSS_SELECTOR, "span .input__box [tabindex='2']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".home-arrow__search .search2__button")
    # Если понадобится нажимать на кнопку "Найти" вместо Enter
    SUGGEST_LIST = (By.CSS_SELECTOR, "[role='listbox']")
    IMAGES_PICTURE = (By.CSS_SELECTOR, "[data-id='images']")


class AfterSearchYandexPageLocators:
    FIRST_RESULT_OF_URL = (By.CSS_SELECTOR, "[data-cid='0'] [class='path organic__path'] a")
    SECOND_RESULT_OF_URL = (By.CSS_SELECTOR, "[data-cid='1'] [class='Path Organic-Path path organic__path'] a")
    THIRD_RESULT_OF_URL = (By.CSS_SELECTOR, "[data-cid='3'] [class='Path Organic-Path path organic__path'] a")
    FOURTH_RESULT_OF_URL = (By.CSS_SELECTOR, "[data-cid='4'] [class='Path Organic-Path path organic__path'] a")
    FIFTH_RESULT_OF_URL = (By.CSS_SELECTOR, "[data-cid='5'] [class='Path Organic-Path path organic__path'] a")


class YandexImagesPageLocators:
    FIRST_IMAGE = (By.CSS_SELECTOR, "[class='PopularRequestList-Item PopularRequestList-Item_pos_0'] a")