from selenium.webdriver.common.by import By


class AdminLogin:
    LOGO = (By.CSS_SELECTOR, '#header-logo > a > img')
    INPUT_USERNAME = (By.CSS_SELECTOR, '#input-username')
    INPUT_PASSWORD = (By.CSS_SELECTOR, '#input-password')
    FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, '#content > div > div > div > div > div.panel-body > form > div:nth-child(2) > span > a')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#content > div > div > div > div > div.panel-body > form > div.text-right > button')
    FOOTER = (By.CSS_SELECTOR, '#footer')
    MAIN_MENU_CATALOG = (By.CSS_SELECTOR, '#menu-catalog')
    MAIN_MENU_CATALOG_PROD = (By.CSS_SELECTOR, '#collapse1 > li:nth-child(2) > a')
    CREATION_BUTTON = (By.CSS_SELECTOR, '#content > div.page-header > div > div > a')
    PROD_NAME_INPUT = (By.CSS_SELECTOR, '#input-name1')
    PROD_META_INPUT = (By.CSS_SELECTOR, '#input-meta-title1')
    TAB_DATA = (By.CSS_SELECTOR, '#form-product > ul > li:nth-child(2) > a')
    PROD_MODEL_INPUT = (By.CSS_SELECTOR, '#input-model')
    SAVE_BUTTON = (By.CSS_SELECTOR, '#content > div.page-header > div > div > button > i')
    DELETE_BUTTON = (By.CSS_SELECTOR, '#content > div.page-header > div > div > button.btn.btn-danger > i')
    SUCCESS = (By.CSS_SELECTOR, '#content > div.container-fluid > div.alert.alert-success.alert-dismissible')


