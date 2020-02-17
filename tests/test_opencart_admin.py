from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AdminLogin

PRODUCT_NAME = 'Cool gadget'
PRODUCT_NAME_MOD = 'Item for delete'
META_TEG = 'COOL'
MODEL_NAME = 'Cool gadget 2020'
XPATH_EDIT = (By.XPATH, f".//*[text()='{PRODUCT_NAME}']/following-sibling::*[5]")
XPATH_CHECKBOX = (By.XPATH, f".//*[text()='{PRODUCT_NAME_MOD}']/preceding-sibling::*[2]")


def test_prod_adding(authorized_user):
    '''Navigate and add new product into catalog. Only required fields will be filled'''
    authorized_user.find_element(*AdminLogin.MAIN_MENU_CATALOG).click()  # Navigate to Catalog
    wait = WebDriverWait(authorized_user, 10)  # Wait to be sure that sub menu is available
    wait.until(EC.visibility_of_element_located(tuple(AdminLogin.MAIN_MENU_CATALOG_PROD))).click()  # Navigate to Products sub menu an enter
    authorized_user.find_element(*AdminLogin.CREATION_BUTTON).click()  # Click on Add new product button
    prod_name = authorized_user.find_element(*AdminLogin.PROD_NAME_INPUT)  # Find product name field
    prod_name.clear()  # Clear field to avoid unexpected symbols
    prod_name.send_keys(PRODUCT_NAME)  # Type new product name
    meta_tag = authorized_user.find_element(*AdminLogin.PROD_META_INPUT)  # Find Meta tag field
    meta_tag.clear()  # Clear field to avoid unexpected symbols
    meta_tag.send_keys(META_TEG)  # Type meta tag
    authorized_user.find_element(*AdminLogin.TAB_DATA).click()  # Change form TAB to fill third required field
    model = authorized_user.find_element(*AdminLogin.PROD_MODEL_INPUT)  # Find Model field
    model.clear()  # Clear field to avoid unexpected symbols
    model.send_keys(MODEL_NAME)  # Type model
    authorized_user.find_element(*AdminLogin.SAVE_BUTTON).click()  # Save product information
    wait.until(EC.visibility_of_element_located(tuple(AdminLogin.SUCCESS)))
    success = authorized_user.find_element(*AdminLogin.SUCCESS)
    assert success.text == 'Success: You have modified products!\n×'
    authorized_user.quit()


def test_prod_editing(authorized_user):
    '''Navigate, find the product which was just added and edit it'''
    authorized_user.find_element(*AdminLogin.MAIN_MENU_CATALOG).click()
    wait = WebDriverWait(authorized_user, 10)
    wait.until(EC.visibility_of_element_located(tuple(AdminLogin.MAIN_MENU_CATALOG_PROD))).click()
    authorized_user.find_element(*AdminLogin.MAIN_MENU_CATALOG_PROD).click()
    authorized_user.find_element(*XPATH_EDIT).click()  # Use Edit button for the product which was just added
    prod_name = authorized_user.find_element(*AdminLogin.PROD_NAME_INPUT)  # Find product name field
    prod_name.clear()  # Clear field to avoid unexpected symbols
    prod_name.send_keys(PRODUCT_NAME_MOD)  # Type new product name
    authorized_user.find_element(*AdminLogin.SAVE_BUTTON).click()  # Save changes
    wait.until(EC.visibility_of_element_located(tuple(AdminLogin.SUCCESS)))
    success = authorized_user.find_element(*AdminLogin.SUCCESS)
    assert success.text == 'Success: You have modified products!\n×'
    authorized_user.quit()


def test_prod_deleting(authorized_user):
    '''Navigate, find the product which was just added and delete it'''
    authorized_user.find_element(*AdminLogin.MAIN_MENU_CATALOG).click()
    wait = WebDriverWait(authorized_user, 10)
    wait.until(EC.visibility_of_element_located(tuple(AdminLogin.MAIN_MENU_CATALOG_PROD))).click()
    authorized_user.find_element(*AdminLogin.MAIN_MENU_CATALOG_PROD).click()
    authorized_user.find_element(*XPATH_CHECKBOX).click()  # Use checkbox to opt the product which was just added
    authorized_user.find_element(*AdminLogin.DELETE_BUTTON).click()  # click Trash button to delete the product
    Alert(authorized_user).accept()  # Confirm deletion
    wait.until(EC.visibility_of_element_located(tuple(AdminLogin.SUCCESS)))
    success = authorized_user.find_element(*AdminLogin.SUCCESS)
    assert success.text == 'Success: You have modified products!\n×'
    authorized_user.quit()
