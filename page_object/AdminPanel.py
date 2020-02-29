from selenium.webdriver.common.alert import Alert
from .BasePage import BasePage
from .TestInput import TestInput


class AdminPanel(BasePage):
    '''Class includes constance and methods to test admin panel'''
    LOGO = {'css': '#header-logo > a > img'}
    INPUT_USERNAME = {'css': '#input-username'}
    INPUT_PASSWORD = {'css': '#input-password'}
    LOGIN_BUTTON = {'css': '#content > div > div > div > div > div.panel-body > form > div.text-right > button'}
    FORGOTTEN_PASSWORD = {
        'css': '#content > div > div > div > div > div.panel-body > form > div:nth-child(2) > span > a'}
    FOOTER = {'css': '#footer'}
    MAIN_MENU_CATALOG = {'css': '#menu-catalog'}
    MAIN_MENU_CATALOG_PROD = {'css': '#collapse1 > li:nth-child(2) > a:nth-child(1)'}
    CREATION_BUTTON = {'css': '#content > div.page-header > div > div > a'}
    PROD_NAME_INPUT = {'css': '#input-name1'}
    PROD_META_INPUT = {'css': '#input-meta-title1'}
    TAB_DATA = {'css': '#form-product > ul > li:nth-child(2) > a'}
    PROD_MODEL_INPUT = {'css': '#input-model'}
    SAVE_BUTTON = {'css': '#content > div.page-header > div > div > button > i'}
    DELETE_BUTTON = {'css': '#content > div.page-header > div > div > button.btn.btn-danger > i'}
    SUCCESS = {'css': '#content > div.container-fluid > div.alert.alert-success.alert-dismissible'}

    def authorization(self, login, password):
        '''Authorization then used as fixture for admin panel tests'''
        self._input(self.INPUT_USERNAME, login)
        self._input(self.INPUT_PASSWORD, password)
        self._click(self.LOGIN_BUTTON)
        return self

    def navigate_catalog(self):
        '''Click on Catalog'''
        self._click(self.MAIN_MENU_CATALOG)
        return self

    def navigate_product(self):
        '''Click on Product (when Catalog uncollapsed)'''
        self._click(self.MAIN_MENU_CATALOG_PROD)
        return self

    def verify_visibility(self, selector):
        '''Check whether element is available for action'''
        self._wait_until_visible(selector)
        return self

    def create_item(self):
        '''Click on Create item button'''
        self._click(self.CREATION_BUTTON)
        return self

    def fill_item_fields(self, prod_name, meta_tag, model):
        '''Filling required fields in product item form'''
        self._input(self.PROD_NAME_INPUT, prod_name)
        self._input(self.PROD_META_INPUT, meta_tag)
        self._click(self.TAB_DATA)
        self._input(self.PROD_MODEL_INPUT, model)
        self._click(self.SAVE_BUTTON)
        return self

    def edit_item(self):
        '''Click on Edit button in particular product'''
        self._click(TestInput.XPATH_EDIT)
        return self

    def select_item(self):
        '''Select particular product via checkbox element'''
        self._just_click(TestInput.XPATH_CHECKBOX)
        return self

    def delete_item(self, driver):
        '''Click on Delete button which delete selected product and accept alert'''
        self._click(self.DELETE_BUTTON)
        Alert(driver).accept()
        return self

    def check_for_success(self):
        '''Check the result after actions with product items'''
        assert self._get_element_text(self.SUCCESS) == 'Success: You have modified products!\n×'
