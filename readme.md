Homework for lesson 10-11: Elements wait and Webelement
home_work folder contains the followings:
- locators - represents locator classes and init file for admin interface
- tests - represents simple fixture and two test files (for Firefox and Chrome) which of those start 3 tests for adding, 
editing and deleting product item. Being launched in a row these tests provide CRUD cycle.


=========================Updated===================================================

Homework for Page Object lesson (12) based on previous lessons 10-11 refactor code in Page Object
pattern an add some new tests

home_work folder contains the followings:
- page_object (instead of locators) - represents classes whith constants and methods discribed opencart shop pages
- tests - represents^ 
    - 2 fixture (conftest.py) 
    - 3 units with tests:
        - test_my_account.py - 4 tests
        - test_opencart_search.py - 1 test
        - test_opencart_admin.py - 3 test which was refactor into page object paradigm
        

For authorization you need to add authorization.py in project root with variables:
URL = 'http://target address '
LOGIN = 'your admin login"
PASSWORD = 'your admin password"
LOGIN_USER = 'your user(customer) login'
PASSWORD_USER = ''your user(customer) password'