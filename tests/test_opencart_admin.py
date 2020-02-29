from page_object import AdminPanel, TestInput



def test_prod_adding(authorized_user):
    '''Navigate and add new product into catalog. Only required fields will be filled'''
    authorized_user.implicitly_wait(3)
    AdminPanel(authorized_user)\
        .navigate_catalog()\
        .verify_visibility(AdminPanel.MAIN_MENU_CATALOG_PROD)\
        .navigate_product()
    authorized_user.implicitly_wait(3)
    AdminPanel(authorized_user)\
        .create_item()\
        .fill_item_fields(TestInput.PRODUCT_NAME, TestInput.META_TEG, TestInput.MODEL_NAME) \
        .check_for_success()
    authorized_user.quit()


def test_prod_editing(authorized_user):
    '''Navigate, find the product which was just added and edit it'''
    authorized_user.implicitly_wait(3)
    AdminPanel(authorized_user)\
        .navigate_catalog()\
        .verify_visibility(AdminPanel.MAIN_MENU_CATALOG_PROD)\
        .navigate_product()
    authorized_user.implicitly_wait(3)
    AdminPanel(authorized_user)\
        .edit_item()\
        .fill_item_fields(TestInput.PRODUCT_NAME_MOD, TestInput.META_TEG, TestInput.MODEL_NAME) \
        .check_for_success()
    authorized_user.quit()


def test_prod_deleting(authorized_user):
    '''Navigate, find the product which was just added and delete it'''
    authorized_user.implicitly_wait(3)
    AdminPanel(authorized_user)\
        .navigate_catalog()\
        .verify_visibility(AdminPanel.MAIN_MENU_CATALOG_PROD)\
        .navigate_product()
    authorized_user.implicitly_wait(3)
    AdminPanel(authorized_user)\
        .select_item()\
        .delete_item(authorized_user)\
        .check_for_success()
    authorized_user.quit()
