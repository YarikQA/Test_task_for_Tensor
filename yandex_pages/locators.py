from selenium.webdriver.common.by import By


class YandexBasePageLocators:  # Локаторы для Базовой страницы Яндекс
    SEARCH_BAR = (By.CSS_SELECTOR, "div .home-arrow__search form")
    SEARCH_BAR_FOR_INPUT = (By.CSS_SELECTOR, "span .input__box [tabindex='2']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".home-arrow__search .search2__button")
    # Если понадобится нажимать на кнопку "Найти" вместо Enter, 1 тест-кейс, 5 шаг
    SUGGEST_LIST = (By.CSS_SELECTOR, "[role='listbox']")
    IMAGES_PICTURE = (By.CSS_SELECTOR, "[data-id='images']")


class YandexPageAfterSearchLocators:  # Локаторы для страницы Яндекса после поиска
    FIRST_RESULT_OF_URL = (By.CSS_SELECTOR, "[data-cid='0'] [class='path organic__path'] a")
    SECOND_RESULT_OF_URL = (By.CSS_SELECTOR, "[data-cid='1'] [class='Path Organic-Path path organic__path'] a")
    THIRD_RESULT_OF_URL = (By.CSS_SELECTOR, "[data-cid='3'] [class='Path Organic-Path path organic__path'] a")
    FOURTH_RESULT_OF_URL = (By.CSS_SELECTOR, "[data-cid='4'] [class='Path Organic-Path path organic__path'] a")
    FIFTH_RESULT_OF_URL = (By.CSS_SELECTOR, "[data-cid='5'] [class='Path Organic-Path path organic__path'] a")


class YandexImagesPageLocators:  # Локаторы для страницы Яндекс.Картинки
    FIRST_CATEGORY = (By.CSS_SELECTOR, "[class='PopularRequestList-Item PopularRequestList-Item_pos_0'] a")
    NAME_OF_FIRST_CATEGORY = (By.CSS_SELECTOR, "[class='PopularRequestList-Item PopularRequestList-Item_pos_0'] "
                                               ".PopularRequestList-SearchText")
    TEXT_IN_SEARCH_BAR = (By.CSS_SELECTOR, ".input__box input")
    FIRST_IMAGE = (By.CSS_SELECTOR, ".serp-item__preview")  # такой селектор, т.к. find_element вернет первый подходящий
    OPENED_IMAGE = (By.CSS_SELECTOR, ".MMImage-Origin")
    NEXT_PICTURE_ICON = (By.CSS_SELECTOR, "[class='CircleButton CircleButton_type_next CircleButton_type "
                                          "MediaViewer-Button MediaViewer-Button_hovered "
                                          "MediaViewer_theme_fiji-Button MediaViewer-ButtonNext "
                                          "MediaViewer_theme_fiji-ButtonNext']")

    PREVIOUS_PICTURE_ICON = (By.CSS_SELECTOR, "[class='CircleButton CircleButton_type_prev CircleButton_type "
                                              "MediaViewer-Button MediaViewer_theme_fiji-Button "
                                              "MediaViewer-ButtonPrev MediaViewer_theme_fiji-ButtonPrev']")
