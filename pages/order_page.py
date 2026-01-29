from locators.order_page_locators import OrderPageLocators as OPL

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def click_to_order_button_home_page(self, order):
        self.driver.find_element(*order).click()

    def click_to_metro_station(self):
        self.driver.find_element(*OPL.FIELD_METRO_STATION).click()     

    def set_name(self, name):
        self.driver.find_element(*OPL.FIELD_NAME).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*OPL.FIELD_SURNAME).send_keys(surname)        
    
    def set_address(self, address):
        self.driver.find_element(*OPL.FIELD_ADDRESS).send_keys(address)      

    def set_phone_number(self, phone_number):
        self.driver.find_element(*OPL.FIELD_PHONE_NUMBER).send_keys(phone_number)          

    def scroll_to_metro_station(self):
        element = self.driver.find_element(*OPL.FIELD_SELECT_METRO_STATION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_select_metro_station(self):
        self.driver.find_element(*OPL.FIELD_SELECT_METRO_STATION).click()

    def click_to_button_further(self):
        self.driver.find_element(*OPL.BUTTON_FURTHER).click()




    def set_date_scooter(self, data):
        self.driver.find_element(*OPL.FIELD_DATA_BRING_SCOOTER).send_keys(f"{data}")


    def click_to_rental_period(self):
        self.driver.find_element(*OPL.DROPDOWN_RENTAL_PERIOD).click()

    def click_to_select_rental_period(self):
        self.driver.find_element(*OPL.SELECT_DROPDOWN_RENTAL_PERIOD).click()

    def click_to_checkbox(self, checkbox):
        self.driver.find_element(*checkbox).click()

    def click_to_order(self):
        self.driver.find_element(*OPL.BUTTON_ORDER).click()


    def click_to_confirm_button(self):
        self.driver.find_element(*OPL.BUTTON_YES).click()    

    def text_confirm_order(self):
        element = self.driver.find_element(*OPL.TITLE_ORDER_CONFIRMED).text
        return element
    
    def click_button_view_status(self):
        self.driver.find_element(*OPL.BUTTON_VIEW_STATUS)
    

    def input_personal_data(self, name, surname, address, phone_number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_to_metro_station()
        self.scroll_to_metro_station()
        self.click_select_metro_station()        
        self.set_phone_number(phone_number)
        self.click_to_button_further()    

    
    def input_rental_data(self, date, checkbox):
        self.set_date_scooter(date)
        self.click_to_rental_period()
        self.click_to_select_rental_period()
        self.click_to_checkbox(checkbox)
        self.click_to_order()

