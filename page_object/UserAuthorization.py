from .BasePage import BasePage


class UserAuthorization(BasePage):
    '''Class provides user authorization'''
    E_MAIL = {'css': '#input-email'}
    PASSWORD = {'css': '#input-password'}
    LOGIN_BUTTON = {'css': '#content > div > div:nth-child(2) > div > form > input'}

    def authorization(self, login, password):
        '''Authorization function which fill the form and submit it'''
        self._input(self.E_MAIL, login)
        self._input(self.PASSWORD, password)
        self._click(self.LOGIN_BUTTON)
        return self
