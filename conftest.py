import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome',
                     help="Choose browser for work: Chrome of Firefox")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    fp = webdriver.FirefoxProfile
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\n\t Working with Chrome...")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\n\t Working with Chrome...")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("-- You should choose browser for work: Chrome or Firefox")
    yield browser
    print("\n\t Work is done...")
    browser.quit()


