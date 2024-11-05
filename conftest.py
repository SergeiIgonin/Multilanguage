"Вариант запуска тестов в разных языковых версиях сайта"

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser = None
    print("\nstart chrome browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
