from selenium.webdriver.common.by import By

class BasePageLocators:
    TITLE_HEADER = [By.XPATH, '//div[contains(@class, "Order") and contains(@class, "Header")]']
    LOGO_YANDEX = [By.XPATH, '//a[contains(@class, "Header_LogoYandex")]']
    LOGO_SCOOTER = [By.XPATH, '//a[contains(@class, "Header_LogoScooter")]']

    