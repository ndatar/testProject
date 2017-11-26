import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from YelpPage import main_page

class RestaurantTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.yelp.com")

    def test_yelp_page_elements_exists(self):

        page = main_page.SearchPage(self.driver)

        assert page.is_title_matches(), "San Jose Restaurants, Dentists, Bars, Beauty Salons, Doctors - Yelp"
        assert page.get_find_selector_input()
        assert page.get_near_location_search_input()

    def test_find_inputs(self):

        page = main_page.SearchPage(self.driver)

        page.get_find_selector_input().clear()
        page.get_find_selector_input().send_keys("Restaurants")
        page.get_find_selector_input().send_keys(Keys.ENTER)

        page.get_near_location_search_input().clear()
        page.get_near_location_search_input().send_keys("San Jose")
        page.get_near_location_search_input().send_keys(Keys.ENTER)

        print(page.get_find_selector_input().get_attribute('value'))
        assert page.get_find_selector_input().get_attribute('value') == 'Restaurants'
        assert page.get_near_location_search_input().get_attribute('value') == 'San Jose'

         #print(page.get_restaurant_lists())

        for item in page.get_restaurant_lists():
            item1 = item.find_element_by_tag_name("span")
            print item1.text

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()