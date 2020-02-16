import pytest
from selenium import webdriver
from locators import AdminLogin
from drivers import Path


def pytest_addoption(parser):
    '''Set a browser and also set default if nothing given'''
    parser.addoption('--browser', default='Firefox', help='A browser which will be launched. Default Chrome')


@pytest.fixture
def request_params(request):
    '''1st fixture handling the command line params'''
    param = {}
    param['browser'] = request.config.getoption('--browser')
    return param


@pytest.fixture
def browser(request_params):
    '''2nd fixture handling the browser choose. Running browser and First step - authorization'''
    if request_params['browser'] == 'Chrome':
        browser = webdriver.Chrome(executable_path=Path.CHROME)
    else:
        browser = webdriver.Firefox(executable_path=Path.FIREFOX)
    browser.get('http://127.0.0.1/admin/')
    username = browser.find_element_by_css_selector(AdminLogin.INPUT_USERNAME)  # Find username field
    username.clear()  # Clear field to avoid unexpected symbols
    username.send_keys('admin')  # Enter username
    password = browser.find_element_by_css_selector(AdminLogin.INPUT_PASSWORD)  # Find password field
    password.clear()  # Clear field to avoid unexpected symbols
    password.send_keys('kamax')  # Enter password
    browser.find_element_by_css_selector(AdminLogin.LOGIN_BUTTON).click()  # confirm authorization
    return browser