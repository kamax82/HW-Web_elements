from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AdminLogin


def test_authorization(firefox):
    '''First step - authorization'''
    firefox.get('http://127.0.0.1/admin/')
    username = firefox.find_element(By.CSS_SELECTOR, AdminLogin.INPUT_USERNAME)  # Find username field
    username.clear()  # Clear field to avoid unexpected symbols
    username.send_keys(AdminLogin.ADMIN)  # Enter username
    password = firefox.find_element(By.CSS_SELECTOR, AdminLogin.INPUT_PASSWORD)  # Find password field
    password.clear()  # Clear field to avoid unexpected symbols
    password.send_keys(AdminLogin.PASSWORD)  # Enter password
    firefox.find_element(By.CSS_SELECTOR, AdminLogin.LOGIN_BUTTON).click()  # confirm authorization
    firefox.quit()


def test_prod_adding(firefox):
    '''Navigate and add new product into catalog. Only required fields will be filled'''
    test_authorization(firefox)  # authorization
    firefox.find_element(By.CSS_SELECTOR, AdminLogin.MAIN_MENU_CATALOG).click()  # Navigate to Catalog
    wait = WebDriverWait(firefox, 10)  # Wait to be sure that sub menu is available
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, AdminLogin.MAIN_MENU_CATALOG_PROD))).click()  # Navigate to Products sub menu an enter
    firefox.find_element(By.CSS_SELECTOR, AdminLogin.CREATION_BUTTON).click()  # Click on Add new product button
    prod_name = firefox.find_element(By.CSS_SELECTOR, AdminLogin.PROD_NAME_INPUT)  # Find product name field
    prod_name.clear()  # Clear field to avoid unexpected symbols
    prod_name.send_keys(AdminLogin.PRODUCT_NAME)  # Type new product name
    meta_tag = firefox.find_element(By.CSS_SELECTOR, AdminLogin.PROD_META_INPUT)  # Find Meta tag field
    meta_tag.clear()  # Clear field to avoid unexpected symbols
    meta_tag.send_keys(AdminLogin.META_TEG)  # Type meta tag
    firefox.find_element(By.CSS_SELECTOR, AdminLogin.TAB_DATA).click()  # Change form TAB to fill third required field
    model = firefox.find_element(By.CSS_SELECTOR, AdminLogin.PROD_MODEL_INPUT)  # Find Model field
    model.clear()  # Clear field to avoid unexpected symbols
    model.send_keys(AdminLogin.MODEL_NAME)  # Type model
    firefox.find_element(By.CSS_SELECTOR, AdminLogin.SAVE_BUTTON).click()  # Save product information
    firefox.quit()


def test_prod_editing(firefox):
    '''Navigate, find the product which was just added and edit it'''
    test_authorization(firefox)
    firefox.find_element(By.CSS_SELECTOR, AdminLogin.MAIN_MENU_CATALOG).click()
    wait = WebDriverWait(firefox, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, AdminLogin.MAIN_MENU_CATALOG_PROD))).click()
    firefox.find_element(By.CSS_SELECTOR, AdminLogin.MAIN_MENU_CATALOG_PROD).click()
    firefox.find_element(By.XPATH,
                         AdminLogin.XPATH_EDIT).click()  # Use Edit button for the product which was just added
    prod_name = firefox.find_element(By.CSS_SELECTOR, AdminLogin.PROD_NAME_INPUT)  # Find product name field
    prod_name.clear()  # Clear field to avoid unexpected symbols
    prod_name.send_keys(AdminLogin.PRODUCT_NAME_MOD)  # Type new product name
    firefox.find_element(By.CSS_SELECTOR, AdminLogin.SAVE_BUTTON).click()  # Save changes
    firefox.quit()


def test_prod_deleting(firefox):
    '''Navigate, find the product which was just added and delete it'''
    test_authorization(firefox)
    firefox.find_element(By.CSS_SELECTOR, AdminLogin.MAIN_MENU_CATALOG).click()
    wait = WebDriverWait(firefox, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, AdminLogin.MAIN_MENU_CATALOG_PROD))).click()
    firefox.find_element(By.CSS_SELECTOR, AdminLogin.MAIN_MENU_CATALOG_PROD).click()
    firefox.find_element(By.XPATH,
                         AdminLogin.XPATH_CHECKBOX).click()  # Use checkbox to opt the product which was just added
    firefox.find_element(By.CSS_SELECTOR, AdminLogin.DELETE_BUTTON).click()  # click Trash button to delete the product
    Alert(firefox).accept()  # Confirm deletion
    firefox.quit()
