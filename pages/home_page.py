from locators.home_page_locators import HomePageLocators as HPL
from pages.base_page import BasePage

import allure

class HomePage(BasePage):
    


    @allure.step('Нажимаем на выбранный вопрос')
    def click_to_question(self, question):
        self.click_to_element(question)

    @allure.step('Ждём появления ответа')
    def wait_to_appear_answer(self, answer):
        self.wait_element(answer)

    @allure.step('Возвращаем текст ответа')
    def get_text_answer(self, answer):
        return self.get_text_element(answer)


    @allure.step(
        'На главной странице скролл до раздела вопросы о важном,' \
        ' нажатие на вопрос и получение текста ответа')
    def open_answer(self, section, question, answer):
        self.scroll_to_element(section)
        self.click_to_question(question)
        self.wait_to_appear_answer(answer)
        return self.get_text_answer(answer)

