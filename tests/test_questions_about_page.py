from locators.home_page_locators import HomePageLocators as HPL
from pages.home_page import HomePage
from urls import Urls

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestQuestionsAboutPage:
    driver = None

    check_answers = [
        (HPL.FIRST_QUESTION, HPL.FIRST_ANSWER, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (HPL.SECOND_QUESTION, HPL.SECOND_ANSWER, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (HPL.THIRD_QUESTION, HPL.THIRD_ANSWER, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (HPL.FOURTH_QUESTION, HPL.FOURTH_ANSWER, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (HPL.FIFTH_QUESTION, HPL.FIFTH_ANSWER, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (HPL.SIXTH_QUESTION, HPL.SIXTH_ANSWER, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (HPL.SEVENTH_QUESTION, HPL.SEVENTH_ANSWER, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (HPL.EIQGHTH_QUESTION, HPL.EIQGHTH_ANSWER, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ]

    @classmethod
    def setup_class(cls):

        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @pytest.mark.parametrize("question, answer, expected_answer", check_answers)
    def test_check_text_answer_on_drop_down_list(self, question, answer, expected_answer):
        
        self.driver.get(Urls.HOME_PAGE_URL)

        question_about_page = HomePage(self.driver)

        question_about_page.open_answer(question)
        question_about_page.wait_to_appear_answer(answer)

        text_answer = question_about_page.text_answer(answer)
        assert text_answer == expected_answer

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()