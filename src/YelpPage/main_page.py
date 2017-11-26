from locators import SearchPageLocators

class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

class SearchPage(BasePage):

    def is_title_matches(self):

        return "San Jose Restaurants, Dentists, Bars, Beauty Salons, Doctors - Yelp" in self.driver.title

    def get_find_selector_input(self):

        return self.driver.find_element(*SearchPageLocators.FIND_SELECTOR)

    def get_near_location_search_input(self):

        return self.driver.find_element(*SearchPageLocators.NEAR_LOCATION_SELECTOR)

    def get_restaurant_lists(self):

        return self.driver.find_elements(*SearchPageLocators.RESTAURANT_LOCATORS)





