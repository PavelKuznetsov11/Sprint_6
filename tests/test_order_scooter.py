from locators.home_page_locators import HomePageLocators as HPL
from locators.base_page_locators import BasePageLocators as BPL
from locators.order_page_locators import OrderPageLocators as OPL

from pages.home_page import HomePage
from pages.base_page import BasePage
from pages.order_page import OrderPage

from urls import Urls

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestOrderScooter:
    driver = None

    locs = [
        (OPL.ORDER_NAV, OPL.CHECKBOX_BLACK, BPL.LOGO_YANDEX, Urls.DZEN_PAGE_URL, 
         "Игорь", "Петров", "Озёрная улица, 230", "+79304201059", "10.02.2026"),

        (OPL.ORDER_FOOTER, OPL.CHECKBOX_GRAY, BPL.LOGO_SCOOTER, Urls.HOME_PAGE_URL, 
         "Владимир", "Сидоров", "Звёздная улица, 140", "+79852104539", "06.02.2026")
    ]

    @classmethod
    def setup_class(cls):

        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @pytest.mark.parametrize("order, checkbox, logo, url_logo, name, surname, address, phone_number, date", locs)
    def test_success_order_scooter(self, order, checkbox, logo, url_logo, name, surname, address, phone_number, date):

        self.driver.get(Urls.HOME_PAGE_URL)
        
        order_page = OrderPage(self.driver)
        base_page = BasePage(self.driver)

        base_page.scroll_to_element(order)

        order_page.click_to_order_button_home_page(order)

        base_page.wait_to_load_page_order()

        order_page.input_personal_data(name, surname, address, phone_number)
        base_page.wait_to_load_page_order()

        order_page.input_rental_data(date, checkbox)

        base_page.wait_to_load_page_order()

        order_page.click_to_confirm_button()

        base_page.wait_to_load_page_order()

        assert "Заказ оформлен" in order_page.text_confirm_order()

        base_page.wait_to_load_page_order()

        order_page.click_button_view_status()

        base_page.wait_logo(logo)
        base_page.click_to_logo(logo)
        base_page.new_tab()

        assert url_logo in self.driver.current_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


