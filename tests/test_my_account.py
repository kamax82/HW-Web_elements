from page_object import TopPanel, TestInput, UserAuthorization, UserRegistration, UserAccount, UserAccountEdit
import authorization


def user_authorization(browser):
    '''User authorization function which then used in tests'''
    TopPanel(browser) \
        .navigate_my_account() \
        .navigate_login()
    browser.implicitly_wait(1)
    UserAuthorization(browser) \
        .authorization(authorization.LOGIN_USER, authorization.PASSWORD_USER)
    return browser


def test_user_authorization(browser):
    '''User authorization test'''
    user_authorization(browser)
    UserAccount(browser) \
        .check_for_login_success()
    browser.quit()


def test_user_registration(browser):
    '''User registration test'''
    TopPanel(browser) \
        .navigate_my_account() \
        .navigate_register()
    browser.implicitly_wait(1)
    UserRegistration(browser) \
        .registration(UserRegistration.REGISTRATION_FORM)
    browser.implicitly_wait(3)
    UserRegistration(browser) \
        .continue_success()
    UserAccount(browser) \
        .check_for_login_success()
    browser.quit()


def test_user_logout(browser):
    '''User account logout test'''
    user_authorization(browser)
    TopPanel(browser) \
        .navigate_my_account()
    UserAccount(browser) \
        .navigate_logout() \
        .check_for_logout_success()
    browser.quit()


def test_user_editing(browser):
    '''User info edit test'''
    user_authorization(browser)
    UserAccount(browser) \
        .navigate_edit_account()
    UserAccountEdit(browser) \
        .account_editing(TestInput.TELEPHONE_MOD)
    UserAccount(browser) \
        .check_for_edit_success()
    browser.quit()
