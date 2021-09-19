import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Выбор браузера для работы
def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome',
                     help="Choose chrome browser for work")


# Фикстура для открытия браузера
@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\n\t Working with Chrome...")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("-- You should choose chrome browser for work")
    yield browser
    print("\n\t Work is done...")
    browser.quit()
