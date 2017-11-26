from selenium.webdriver.common.by import By

class SearchPageLocators(object):

 FIND_SELECTOR = (By.ID, 'find_desc')

 NEAR_LOCATION_SELECTOR = (By.ID,'dropperText_Mast')

 RESTAURANT_LOCATORS = (By.CLASS_NAME, "indexed-biz-name")