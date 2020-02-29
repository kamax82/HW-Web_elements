from .BasePage import BasePage


class UserAccount(BasePage):
    '''Class includes elements and methods to test on User account page'''
    LOGIN = {'css': 'a.list-group-item:nth-child(1)'}
    EDIT_ACCOUNT = {'xpath': './/*[text()="Edit Account"]'}
    LOGOUT = {'css': '#column-right > div > a:nth-child(13)'}
    LOGIN_SUCCESS = {'css': '#content > h2:nth-child(1)'}
    LOGOUT_SUCCESS = {'css': '.breadcrumb > li:nth-child(3) > a:nth-child(1)'}
    EDIT_SUCCESS = {'css': '.alert'}

    def navigate_logout(self):
        '''Click on Logout option to log out'''
        self._click(self.LOGOUT)
        return self

    def navigate_edit_account(self):
        '''Click on Edit account to change user information'''
        self._click(self.EDIT_ACCOUNT)
        return self

    def check_for_login_success(self):
        '''Check whether login in system was success'''
        assert self._get_element_text(self.LOGIN_SUCCESS) == 'My Account'

    def check_for_logout_success(self):
        '''Check whether logout from system was success'''
        self._just_click(self.LOGIN)
        return self

    def check_for_edit_success(self):
        '''Check whether editing user information was success'''
        assert self._get_element_text(self.EDIT_SUCCESS) == 'Success: Your account has been successfully updated.'
