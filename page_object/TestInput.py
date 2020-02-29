from random import randint as rand


class TestInput:
    '''Class includes different data which then used in tests'''
    PRODUCT_NAME = 'Cool gadget'
    PRODUCT_NAME_MOD = 'Item for delete'
    META_TEG = 'COOL'
    MODEL_NAME = 'Cool gadget 2020'
    XPATH_EDIT = {'xpath': f".//*[text()='{PRODUCT_NAME}']/following-sibling::*[5]"}
    XPATH_CHECKBOX = {'xpath': f".//*[text()='{PRODUCT_NAME_MOD}']/preceding-sibling::*[2]"}
    SEARCH_REQUEST = 'MacBook'
    SEARCH_RESULT = {'xpath': f".//*[text()='{SEARCH_REQUEST}']"}
    TELEPHONE_MOD = '79816314466'

    def registration_form():
        '''Function generate unique email and phone number for user registration test'''
        REGISTRATION_FORM = {'first': 'TestName', 'last': 'TestSurname', 'email': '', 'tel': '', 'password': 'test123',
                             'pwd_confirm': 'test123'}
        email_tel = {}
        var = rand(1000, 9999)
        email_tel['email'] = 'test' + str(var) + '@mail.ru'
        email_tel['tel'] = var
        REGISTRATION_FORM.update(email_tel)
        return REGISTRATION_FORM

    REGISTRATION_FORM = registration_form()
