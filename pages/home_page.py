from locators.home_page_locators import HomePageLocators as HPL
from pages.base_page import BasePage


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

class HomePage(BasePage):
    
    @allure.step('Сохраняем driver в обьект класса')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем на выбранный вопрос')
    def click_to_question(self, question):
        self.driver.find_element(*question).click()

    @allure.step('Ждём появления ответа')
    def wait_to_appear_answer(self, answer):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(tuple(answer)))

    @allure.step('Возвращаем текст ответа')
    def text_answer(self, answer):
        element = self.driver.find_element(*answer).text
        return element

    @allure.title('Открытие вопроса в разделе вопросы о важном')
    @allure.description('На главной странице скролл до раздела вопросы о важном и нажатие на вопрос')
    def open_answer(self, question):
        self.scroll_to_element(HPL.QUESTIONS_ABOUT)
        self.click_to_question(question)

