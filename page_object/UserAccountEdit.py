from .BasePage import BasePage


class UserAccountEdit(BasePage):
    '''Class which describe main information for edit page in user account'''
    FIRST_NAME = {'css': '#input-firstname'}
    LAST_NAME = {'css': '#input-lastname'}
    E_MAIL = {'css': '#input-email'}
    PHONE = {'css': '#input-telephone'}
    CONTINUE = {'css': 'input.btn'}

    def account_editing(self, tel):
        '''Method to change user phone number'''
        self._input(self.PHONE, tel)
        self._click(self.CONTINUE)
        return self
