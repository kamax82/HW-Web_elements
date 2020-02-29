from .BasePage import BasePage
from .TestInput import TestInput


class UserRegistration(BasePage):
    '''Class provides new user registration'''
    E_MAIL = {'css': '#input-email'}
    PASSWORD = {'css': '#input-password'}
    FIRST_NAME = {'css': '#input-firstname'}
    LAST_NAME = {'css': '#input-lastname'}
    PHONE = {'css': '#input-telephone'}
    PWD_CONFIRM = {'css': '#input-confirm'}
    PRIVACY = {'css': '#content > form > div > div > input[type=checkbox]:nth-child(2)'}
    CONTINUE = {'css': '#content > form > div > div > input.btn.btn-primary'}
    CONTINUE_SUCCESS = {'css': 'a.btn'}
    REGISTRATION_FORM = TestInput.REGISTRATION_FORM
    SUCCESS = {'css': '#content > p:nth-child(2)'}

    def registration(self, REGISTRATION_FORM):
        '''Registration function which fill the form and submit it'''
        self._input(self.FIRST_NAME, REGISTRATION_FORM['first'])
        self._input(self.LAST_NAME, REGISTRATION_FORM['last'])
        self._input(self.E_MAIL, REGISTRATION_FORM['email'])
        self._input(self.PHONE, REGISTRATION_FORM['tel'])
        self._input(self.PASSWORD, REGISTRATION_FORM['password'])
        self._input(self.PWD_CONFIRM, REGISTRATION_FORM['pwd_confirm'])
        self._click(self.PRIVACY)
        self._click(self.CONTINUE)
        return self

    def continue_success(self):
        '''Click on additional button to check a success'''
        self._click(self.CONTINUE_SUCCESS)
        return self
