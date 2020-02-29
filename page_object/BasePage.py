from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    '''Base class and parent for other page objects classes which provide basic actions which element'''

    def __init__(self, driver):
        '''Driver initiation'''
        self.driver = driver

    def __element(self, selector):
        '''Determine which type of selector will be used'''
        by = None
        if 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        elif 'xpath' in selector.keys():
            by = By.XPATH
            selector = selector['xpath']
        return self.driver.find_element(by, selector)

    def _find_element(self, selector):
        '''Search for given element'''
        return self.__element(selector)

    def _click(self, selector):
        '''Click on given element using mouse imitation'''
        ActionChains(self.driver).move_to_element(self.__element(selector)).click().perform()

    def _just_click(self, selector):
        '''Simple click on given element (without mouse imitation)'''
        self.__element(selector).click()

    def _input(self, selector, value):
        '''Input data into a particular field'''
        element = self.__element(selector)
        element.clear()
        element.send_keys(value)

    def _wait_until_visible(self, selector, wait=10):
        '''Check whether element is available for action'''
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector)))

    def _get_element_text(self, selector):
        '''Call method .text in particular element'''
        return self.__element(selector).text
