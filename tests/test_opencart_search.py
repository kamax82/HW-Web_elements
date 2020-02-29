from page_object import Search, TestInput


def test_searching(browser):
    '''Test of site search functionality'''
    Search(browser) \
        .imput_search_request(TestInput.SEARCH_REQUEST) \
        .check_for_success(TestInput.SEARCH_RESULT)
    browser.quit()
