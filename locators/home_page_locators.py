from selenium.webdriver.common.by import By

class HomePageLocators:



    QUESTIONS_ABOUT = [By.XPATH, '//div[contains(@class,"Home_FourPart")]/div']

    FIRST_QUESTION = [By.ID, 'accordion__heading-0']
    SECOND_QUESTION = [By.ID, 'accordion__heading-1']
    THIRD_QUESTION = [By.ID, 'accordion__heading-2']
    FOURTH_QUESTION = [By.ID, 'accordion__heading-3']
    FIFTH_QUESTION = [By.ID, 'accordion__heading-4']
    SIXTH_QUESTION = [By.ID, 'accordion__heading-5']
    SEVENTH_QUESTION = [By.ID, 'accordion__heading-6']
    EIQGHTH_QUESTION = [By.ID, 'accordion__heading-7']

    FIRST_ANSWER = [By.XPATH, '//div[@id="accordion__panel-0"]/p']
    SECOND_ANSWER = [By.XPATH, '//div[@id="accordion__panel-1"]/p']
    THIRD_ANSWER = [By.XPATH, '//div[@id="accordion__panel-2"]/p']
    FOURTH_ANSWER = [By.XPATH, '//div[@id="accordion__panel-3"]/p']
    FIFTH_ANSWER = [By.XPATH, '//div[@id="accordion__panel-4"]/p']
    SIXTH_ANSWER = [By.XPATH, '//div[@id="accordion__panel-5"]/p']
    SEVENTH_ANSWER = [By.XPATH, '//div[@id="accordion__panel-6"]/p']
    EIQGHTH_ANSWER = [By.XPATH, '//div[@id="accordion__panel-7"]/p']
