from locators.order_page_locators import OrderPageLocators as OPL
from locators.base_page_locators import BasePageLocators as BPL
from pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
import allure

class OrderPage(BasePage):


    @allure.step('Кликаем на кнопку заказа из главной страницы')
    def click_to_order_button_home_page(self, order):
       self.click_to_element(order)
       self.wait_to_load_page_order()

    @allure.step('Кликаем на поле метро')
    def click_to_metro_station(self):
        self.click_to_element(OPL.FIELD_METRO_STATION) 

    @allure.step('Заполняем поле имя')
    def set_name(self, name):
        self.fill_element(OPL.FIELD_NAME, name)

    @allure.step('Заполняем поле фамилия')
    def set_surname(self, surname):
        self.fill_element(OPL.FIELD_SURNAME, surname)
     
    @allure.step('Заполняем поле адрес')
    def set_address(self, address):
        self.fill_element(OPL.FIELD_ADDRESS, address)
  
    @allure.step('Заполняем поле телефон')
    def set_phone_number(self, phone_number):
        self.fill_element(OPL.FIELD_PHONE_NUMBER, phone_number)
       

    @allure.step('Скроллим до выбранной станции метро')
    def scroll_to_metro_station(self):
        self.scroll_to_element(OPL.FIELD_SELECT_METRO_STATION)

    @allure.step('Кликаем до выбранную станцию метро')
    def click_select_metro_station(self):
        self.click_to_element(OPL.FIELD_SELECT_METRO_STATION)

    @allure.step('Кликаем на кнопку дальше')
    def click_to_button_further(self):
        self.click_to_element(OPL.BUTTON_FURTHER)




    @allure.step('Указываем дату получения самоката')
    def set_date_scooter(self, data):
        self.fill_element(OPL.FIELD_DATA_BRING_SCOOTER, data)

    @allure.step('Кликаем на список дни аренды')
    def click_to_rental_period(self):
        self.click_to_element(OPL.DROPDOWN_RENTAL_PERIOD)

    @allure.step('Кликаем на выбранное количество дней аренды')
    def click_to_select_rental_period(self):
        self.click_to_element(OPL.SELECT_DROPDOWN_RENTAL_PERIOD)

    @allure.step('Кликаем на чекбокс цвет самоката')
    def click_to_checkbox(self, checkbox):
        self.click_to_element(checkbox)

    @allure.step('Кликаем на кнопку заказать')
    def click_to_order(self):
        self.click_to_element(OPL.BUTTON_ORDER)


    @allure.step('Кликаем на кнопку подтверждения заказа')
    def click_to_confirm_button(self):
        self.click_to_element(OPL.BUTTON_YES)
   
    @allure.step('Получаем текст, что заказ оформлен')
    def text_confirm_order(self):
        return self.find_element(OPL.TITLE_ORDER_CONFIRMED).text

    @allure.step('Кликаем на кнопку посмотреть заказ')    
    def click_button_view_status(self):
        self.click_to_element(OPL.BUTTON_VIEW_STATUS)


    @allure.step('Ждём загрузки логотипа')
    def wait_logo(self, logo):
        self.wait_element(logo)

    @allure.step('Кликаем на логотип')
    def click_to_logo(self, logo):
        self.click_to_element(logo)

    @allure.step('Переходим на последнюю открытую вкладку, ожидаем загрузки новой вкладки')
    def new_tab(self, url_logo):
        self.switch_tab()
        self.wait_new_tab(url_logo)

    
    @allure.step('Ожидаем загрузки страницы, заполняем имя, ' \
    'фамилию, адрес, метро, номер телефона, и кликаем на кнопку дальше')
    def input_personal_data(self, name, surname, address, phone_number):
        self.wait_to_load_page_order()
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_to_metro_station()
        self.scroll_to_metro_station()
        self.click_select_metro_station()        
        self.set_phone_number(phone_number)
        self.click_to_button_further()    

    @allure.step('Ожидаем загрузки страницы, задаем дату получения самоката, ' \
    'выбираем количество дней аренды, цвет самоката, и нажимаем кнопку заказать')
    def input_rental_data(self, date, checkbox):
        self.wait_to_load_page_order()
        self.set_date_scooter(date)
        self.click_to_rental_period()
        self.click_to_select_rental_period()
        self.click_to_checkbox(checkbox)
        self.click_to_order()

