from locators import ConverterPageLocators

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class ConverterPage(BasePage):

    def is_title_matches(self):

        return "Currency Converter" in self.driver.title

    def is_title_matches(self):

        return "Currency Converter" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*ConverterPageLocators.GO_BUTTON)
        element.click()

    def get_search_box(self):
        return self.driver.find_element(*ConverterPageLocators.SEARCH_BOX)

    def get_quote_currency_selector(self):
        return self.driver.find_element(*ConverterPageLocators.QUOTE_CURRENCY_SELECTOR)


    def get_base_currency_input(self):
        return self.driver.find_element(*ConverterPageLocators.BASE_CURRENCY_INPUT)

    def get_quote_currency_input(self):
        return self.driver.find_element(*ConverterPageLocators.QUOTE_CURRENCY_INPUT)

    def get_quote_amount_input(self):
        return self.driver.find_element(*ConverterPageLocators.QUOTE_AMOUNT_INPUT)
