from locators.home_page_locators import HomePageLocators as HPL
from locators.base_page_locators import BasePageLocators as BPL
from locators.order_page_locators import OrderPageLocators as OPL

from pages.home_page import HomePage
from pages.base_page import BasePage
from pages.order_page import OrderPage

from urls import Urls
from data import Data

import pytest
import allure


class TestOrderScooter:

    @allure.title('Успешный заказ самоката')
    @pytest.mark.parametrize("order, checkbox, logo, url_logo, name, surname, address, phone_number, date", Data.locs)
    def test_success_order_scooter(self, home_driver, order, checkbox, logo, url_logo, name, surname, address, phone_number, date):
        
        order_page = OrderPage(home_driver)

        order_page.scroll_to_element(order)

        order_page.click_to_order_button_home_page(order)


        order_page.input_personal_data( name, surname, address, phone_number)


        order_page.input_rental_data(date, checkbox)

        order_page.click_to_confirm_button()

        assert "Заказ оформлен" in order_page.text_confirm_order()

        order_page.click_button_view_status()

        order_page.wait_logo(logo)
        order_page.click_to_logo(logo)

        order_page.switch_tab()
        order_page.new_tab(url_logo)

    
        assert url_logo in home_driver.current_url



