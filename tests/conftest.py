import pytest
from selenium import webdriver
from page_object import AdminPanel

import authorization


def pytest_addoption(parser):
    '''Set a browser and also set default if nothing given'''
    parser.addoption('--browser', '-B', default='firefox', help='A browser which will be launched. Default Chrome')
    parser.addoption('--firefoxdriver', '-F',
                     default='d:\\PycharmProjects\\HW-lesson_selenium\\drivers\\geckodriver.exe')
    parser.addoption('--chromedriver', '-C',
                     default='d:\\PycharmProjects\\HW-lesson_selenium\\drivers\\chromedriver.exe')


@pytest.fixture
def browser(request):
    '''1st fixture handling the command line params and handling the browser choose.'''
    browser_param = request.config.getoption('--browser')
    firefoxdriver = request.config.getoption('--firefoxdriver')
    chromedriver = request.config.getoption('--chromedriver')
    if browser_param == 'chrome':
        driver = webdriver.Chrome(executable_path=chromedriver)
    else:
        driver = webdriver.Firefox(executable_path=firefoxdriver)
    driver.get(authorization.URL)
    return driver


@pytest.fixture
def authorized_user(browser):
    '''2nd fixture Running browser and First step - authorization'''
    browser.get(authorization.URL + 'admin/')
    AdminPanel(browser) \
        .authorization(authorization.LOGIN, authorization.PASSWORD)
    return browser
