from locators.base_page_locators import BasePageLocators as BPL
from urls import Urls


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import allure

class BasePage:

    @allure.step('Создаем обьект driver')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скроллим до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)    

    @allure.step('Ожиданием элемент')
    def wait_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(tuple(locator)))

    @allure.step('Ожидание новой вкладки')
    def wait_new_tab(self, logo):
        WebDriverWait(self.driver, 15).until(EC.url_contains(logo))

    @allure.step('Находим элемента')
    def find_element(self, locator):
        element = self.driver.find_element(*locator)
        return element
    
    @allure.step('Находим текст элемента')
    def get_text_element(self, locator):
        element = self.find_element(locator)
        return element.text

    @allure.step('Нажимаем на элемент')
    def click_to_element(self, locator):   
        self.driver.find_element(*locator).click()   

    @allure.step('Заполняем поле')
    def fill_element(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('Переходим на последнюю открытую вкладку')
    def switch_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])



    @allure.step('Ожидаем загрузки страницы заказа')
    def wait_to_load_page_order(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(tuple(BPL.TITLE_HEADER)))

