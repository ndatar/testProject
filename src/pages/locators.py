from selenium.webdriver.common.by import By

class ConverterPageLocators(object):
    GO_BUTTON = (By.ID, 'submit')

    SEARCH_BOX = (By.ID , 'id-search-field')

    QUOTE_CURRENCY_SELECTOR = (By.ID, 'quote_currency_selector')

    BASE_CURRENCY_SELECTOR = (By.ID, 'base_currency_selector')

    QUOTE_CURRENCY_INPUT = (By.ID, 'quote_currency_input')

    BASE_CURRENCY_INPUT = (By.ID, 'base_currency_input')

    QUOTE_AMOUNT_INPUT = (By.ID, 'quote_amount_input')

