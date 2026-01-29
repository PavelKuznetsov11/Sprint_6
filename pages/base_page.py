from locators.base_page_locators import BasePageLocators as BPL


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class BasePage:


    def __init__(self, driver):
        self.driver = driver


    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)    


    def wait_logo(self, logo):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(tuple(logo)))


    def click_to_logo(self, logo):
        element = self.driver.find_element(*logo)
        self.driver.execute_script("arguments[0].click();", element)


    def new_tab(self):
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])


    def wait_to_load_page_order(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(tuple(BPL.TITLE_HEADER)))

