import pytest
from selenium import webdriver
from locators import AdminLogin


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

    return driver


@pytest.fixture
def authorized_user(browser):
    '''2nd fixture Running browser and First step - authorization'''
    browser.get('http://127.0.0.1/admin/')
    username = browser.find_element(*AdminLogin.INPUT_USERNAME)  # Find username field
    username.clear()  # Clear field to avoid unexpected symbols
    username.send_keys('admin')  # Enter username
    password = browser.find_element(*AdminLogin.INPUT_PASSWORD)  # Find password field
    password.clear()  # Clear field to avoid unexpected symbols
    password.send_keys('kamax')  # Enter password
    browser.find_element(*AdminLogin.LOGIN_BUTTON).click()  # confirm authorization
    return browser
