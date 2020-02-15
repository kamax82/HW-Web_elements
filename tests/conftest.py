import pytest
from selenium import webdriver


@pytest.fixture
def chrome():
    chrome = webdriver.Chrome(executable_path='d:\\PycharmProjects\\HW-Web_elements\\drivers\\chromedriver.exe')
    return chrome

@pytest.fixture
def firefox():
    firefox = webdriver.Firefox(executable_path='d:\\PycharmProjects\\HW-Web_elements\\drivers\\geckodriver.exe')
    return firefox
