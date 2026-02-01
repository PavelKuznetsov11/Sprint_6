from selenium.webdriver.common.by import By

class HomePageLocators:



    QUESTIONS_ABOUT = [By.XPATH, '//div[contains(@class,"Home_FourPart")]/div']

    FIRST_QUESTION = [By.XPATH, '''//div[@class="accordion__button" and
    contains(text(),"Сколько это стоит? И как оплатить?")]''']
    SECOND_QUESTION = [By.XPATH, '''//div[@class="accordion__button" and
    contains(text(),"Хочу сразу несколько самокатов! Так можно?")]''']
    THIRD_QUESTION = [By.XPATH, '''//div[@class="accordion__button" and
    contains(text(),"Как рассчитывается время аренды?")]''']
    FOURTH_QUESTION = [By.XPATH, '''//div[@class="accordion__button" and
    contains(text(),"Можно ли заказать самокат прямо на сегодня?")]''']
    FIFTH_QUESTION = [By.XPATH, '''//div[@class="accordion__button" and
    contains(text(),"Можно ли продлить заказ или вернуть самокат раньше?")]''']
    SIXTH_QUESTION = [By.XPATH, '''//div[@class="accordion__button" and
    contains(text(),"Вы привозите зарядку вместе с самокатом?")]''']
    SEVENTH_QUESTION = [By.XPATH, '''//div[@class="accordion__button" and
    contains(text(),"Можно ли отменить заказ?")]''']
    EIQGHTH_QUESTION = [By.XPATH, '''//div[@class="accordion__button" and
    contains(text(),"Я жизу за МКАДом, привезёте?")]''']

    FIRST_ANSWER = [By.XPATH, '''//p[contains(text(),
    "Сутки — 400 рублей. Оплата курьеру — наличными или картой.")]''']
    SECOND_ANSWER = [By.XPATH, '''//p[contains(text(),
    "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями")]''']
    THIRD_ANSWER = [By.XPATH, '''//p[contains(text(),
    "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня.")]''']
    FOURTH_ANSWER = [By.XPATH, '''//p[contains(text(),
    "Только начиная с завтрашнего дня. Но скоро станем расторопнее.")]''']
    FIFTH_ANSWER = [By.XPATH, '''//p[contains(text(),
    "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку")]''']
    SIXTH_ANSWER = [By.XPATH, '''//p[contains(text(),
    "Самокат приезжает к вам с полной зарядкой.")]''']
    SEVENTH_ANSWER = [By.XPATH, '''//p[contains(text(),
    "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим.")]''']
    EIQGHTH_ANSWER = [By.XPATH, '''//p[contains(text(),
    "Да, обязательно. Всем самокатов! И Москве, и Московской области.")]''']



