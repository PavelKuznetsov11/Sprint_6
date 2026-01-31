from selenium.webdriver.common.by import By

class HomePageLocators:



    QUESTIONS_ABOUT = [By.XPATH, '//div[contains(@class,"Home_FourPart")]/div']

    FIRST_QUESTION = [By.XPATH, '//div[@class="accordion"]/div[1]//div[@class="accordion__button"]']
    SECOND_QUESTION = [By.XPATH, '//div[@class="accordion"]/div[2]//div[@class="accordion__button"]']
    THIRD_QUESTION = [By.XPATH, '//div[@class="accordion"]/div[3]//div[@class="accordion__button"]']
    FOURTH_QUESTION = [By.XPATH, '//div[@class="accordion"]/div[4]//div[@class="accordion__button"]']
    FIFTH_QUESTION = [By.XPATH, '//div[@class="accordion"]/div[5]//div[@class="accordion__button"]']
    SIXTH_QUESTION = [By.XPATH, '//div[@class="accordion"]/div[6]//div[@class="accordion__button"]']
    SEVENTH_QUESTION = [By.XPATH, '//div[@class="accordion"]/div[7]//div[@class="accordion__button"]']
    EIQGHTH_QUESTION = [By.XPATH, '//div[@class="accordion"]/div[8]//div[@class="accordion__button"]']

    FIRST_ANSWER = [By.XPATH, '//div[@class="accordion"]/div[1]//p']
    SECOND_ANSWER = [By.XPATH, '//div[@class="accordion"]/div[2]//p']
    THIRD_ANSWER = [By.XPATH, '//div[@class="accordion"]/div[3]//p']
    FOURTH_ANSWER = [By.XPATH, '//div[@class="accordion"]/div[4]//p']
    FIFTH_ANSWER = [By.XPATH, '//div[@class="accordion"]/div[5]//p']
    SIXTH_ANSWER = [By.XPATH, '//div[@class="accordion"]/div[6]//p']
    SEVENTH_ANSWER = [By.XPATH, '//div[@class="accordion"]/div[7]//p']
    EIQGHTH_ANSWER = [By.XPATH, '//div[@class="accordion"]/div[8]//p']



