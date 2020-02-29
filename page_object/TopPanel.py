from .BasePage import BasePage


class TopPanel(BasePage):
    '''Class includes elements and methods to test top panel'''
    MY_ACCOUNT = {'xpath': './/*[text()="My Account"]'}
    LOGIN = {'xpath': './/*[text()="Login"]'}
    REGISTER = {'xpath': './/*[text()="Register"]'}
    LOGOUT = {'xpath': './/*[text()="Logout"]'}

    def navigate_my_account(self):
        '''Click on My Account menu'''
        self._just_click(self.MY_ACCOUNT)
        return self

    def navigate_login(self):
        '''Click on Login option in My Account menu'to log in'''
        self._just_click(self.LOGIN)
        return self

    def navigate_register(self):
        '''Click on Register to create new user (customer)'''
        self._just_click(self.REGISTER)
        return self

    def navigate_logout(self):
        '''Click on Logout in My Account  option to log out'''
        self._just_click(self.LOGOUT)
        return self
