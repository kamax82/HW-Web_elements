from .BasePage import BasePage


class Search(BasePage):
    '''Class includes constance and methods to test search function'''
    SEARCH_FIELD = {'css': '#search > input'}
    SEARCH_BUTTON = {'css': '#search > span > button'}
    SEARCH_RESULT = {'css': '# content > div:nth-child(8)'}
    CATEGORIES_SELECTOR = '#content > div:nth-child(3) > div:nth-child(2) > select'
    SEARCH_MODIFICATOR = '#content > div:nth-child(3) > div:nth-child(3) > label > input[type=checkbox]'
    TO_CART_1 = '#content > div:nth-child(8) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(1) > span'
    TO_WISH_LIST_1 = '#content > div:nth-child(8) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(2) > i'
    TO_COMPARE_BUTTON_1 = '#content > div:nth-child(8) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(3)'

    def imput_search_request(self, request):
        '''Input request which will be searched'''
        self._input(self.SEARCH_FIELD, request)
        self._click(self.SEARCH_BUTTON)
        return self

    def check_for_success(self, selector):
        '''Check whether search was success'''
        assert self._find_element(selector)
