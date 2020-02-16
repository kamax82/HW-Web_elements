from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AdminLogin

PRODUCT_NAME = 'Cool gadget'
PRODUCT_NAME_MOD = 'Item for delete'
META_TEG = 'COOL'
MODEL_NAME = 'Cool gadget 2020'
XPATH_EDIT = f".//*[text()='{PRODUCT_NAME}']/following-sibling::*[5]"
XPATH_CHECKBOX = f".//*[text()='{PRODUCT_NAME_MOD}']/preceding-sibling::*[2]"


def test_prod_adding(browser):
    '''Navigate and add new product into catalog. Only required fields will be filled'''
    browser.find_element(By.CSS_SELECTOR, AdminLogin.MAIN_MENU_CATALOG).click()  # Navigate to Catalog
    wait = WebDriverWait(browser, 10)  # Wait to be sure that sub menu is available
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, AdminLogin.MAIN_MENU_CATALOG_PROD))).click()  # Navigate to Products sub menu an enter
    browser.find_element(By.CSS_SELECTOR, AdminLogin.CREATION_BUTTON).click()  # Click on Add new product button
    prod_name = browser.find_element(By.CSS_SELECTOR, AdminLogin.PROD_NAME_INPUT)  # Find product name field
    prod_name.clear()  # Clear field to avoid unexpected symbols
    prod_name.send_keys(PRODUCT_NAME)  # Type new product name
    meta_tag = browser.find_element(By.CSS_SELECTOR, AdminLogin.PROD_META_INPUT)  # Find Meta tag field
    meta_tag.clear()  # Clear field to avoid unexpected symbols
    meta_tag.send_keys(META_TEG)  # Type meta tag
    browser.find_element(By.CSS_SELECTOR, AdminLogin.TAB_DATA).click()  # Change form TAB to fill third required field
    model = browser.find_element(By.CSS_SELECTOR, AdminLogin.PROD_MODEL_INPUT)  # Find Model field
    model.clear()  # Clear field to avoid unexpected symbols
    model.send_keys(MODEL_NAME)  # Type model
    browser.find_element(By.CSS_SELECTOR, AdminLogin.SAVE_BUTTON).click()  # Save product information
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, AdminLogin.SUCCESS)))
    success = browser.find_element_by_css_selector(AdminLogin.SUCCESS)
    assert success.text == 'Success: You have modified products!\n×'
    # browser.quit()


def test_prod_editing(browser):
    '''Navigate, find the product which was just added and edit it'''
    browser.find_element(By.CSS_SELECTOR, AdminLogin.MAIN_MENU_CATALOG).click()
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, AdminLogin.MAIN_MENU_CATALOG_PROD))).click()
    browser.find_element(By.CSS_SELECTOR, AdminLogin.MAIN_MENU_CATALOG_PROD).click()
    browser.find_element(By.XPATH, XPATH_EDIT).click()  # Use Edit button for the product which was just added
    prod_name = browser.find_element(By.CSS_SELECTOR, AdminLogin.PROD_NAME_INPUT)  # Find product name field
    prod_name.clear()  # Clear field to avoid unexpected symbols
    prod_name.send_keys(PRODUCT_NAME_MOD)  # Type new product name
    browser.find_element(By.CSS_SELECTOR, AdminLogin.SAVE_BUTTON).click()  # Save changes
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, AdminLogin.SUCCESS)))
    success = browser.find_element_by_css_selector(AdminLogin.SUCCESS)
    assert success.text == 'Success: You have modified products!\n×'

    # browser.quit()


def test_prod_deleting(browser):
    '''Navigate, find the product which was just added and delete it'''
    browser.find_element(By.CSS_SELECTOR, AdminLogin.MAIN_MENU_CATALOG).click()
    wait = WebDriverWait(browser, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, AdminLogin.MAIN_MENU_CATALOG_PROD))).click()
    browser.find_element(By.CSS_SELECTOR, AdminLogin.MAIN_MENU_CATALOG_PROD).click()
    browser.find_element(By.XPATH, XPATH_CHECKBOX).click()  # Use checkbox to opt the product which was just added
    browser.find_element(By.CSS_SELECTOR, AdminLogin.DELETE_BUTTON).click()  # click Trash button to delete the product
    Alert(browser).accept()  # Confirm deletion
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, AdminLogin.SUCCESS)))
    success = browser.find_element_by_css_selector(AdminLogin.SUCCESS)
    assert success.text == 'Success: You have modified products!\n×'
    # browser.quit()
