class TestInput:

    PRODUCT_NAME = 'Cool gadget'
    PRODUCT_NAME_MOD = 'Item for delete'
    META_TEG = 'COOL'
    MODEL_NAME = 'Cool gadget 2020'
    XPATH_EDIT = {'xpath': f".//*[text()='{PRODUCT_NAME}']/following-sibling::*[5]"}
    XPATH_CHECKBOX = {'xpath': f".//*[text()='{PRODUCT_NAME_MOD}']/preceding-sibling::*[2]"}
