from locators.home_page_locators import HomePageLocators as HPL
from pages.home_page import HomePage
from urls import Urls
from data import Data

import pytest
import allure


class TestQuestionsAboutPage:



    @allure.title('Проверка, что текст ожидаемого ответа совпадает с фактическим результатом')
    @pytest.mark.parametrize("question, answer, expected_answer", Data.check_answers)
    def test_check_text_answer_on_drop_down_list(self, home_driver, question, answer, expected_answer):


        question_about_page = HomePage(home_driver)

    
        text_answer = question_about_page.open_answer(HPL.QUESTIONS_ABOUT, question, answer)
        assert text_answer == expected_answer


