import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages import main_page

class ConverterTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.oanda.com/currency/converter/")

    def test_converter_elements_exists(self):

        page = main_page.ConverterPage(self.driver)

        assert page.is_title_matches()
        assert page.get_quote_currency_selector()
     #   assert page.get_base_currency_selector()


    def test_currency_inputs(self):

        page = main_page.ConverterPage(self.driver)

        page.get_quote_currency_input().clear()
        page.get_quote_currency_input().send_keys("USD")
        page.get_quote_currency_input().send_keys(Keys.ENTER)


        page.get_base_currency_input().clear()
        page.get_base_currency_input().send_keys("INR")
        page.get_base_currency_input().send_keys(Keys.ENTER)


        assert page.get_quote_currency_input().get_attribute('value') == 'US Dollar'
        assert page.get_base_currency_input().get_attribute('value') == 'Indian Rupee'


    def test_currency_amounts(self):

        page = main_page.ConverterPage(self.driver)

        page.get_quote_amount_input().clear()
        page.get_quote_amount_input().send_keys(100)
        page.get_quote_amount_input().send_keys(Keys.ENTER)

        print(page.get_quote_amount_input().get_attribute('value'))
        assert float(page.get_quote_amount_input().get_attribute('value')) == 100.0


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()