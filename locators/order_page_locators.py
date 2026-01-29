from selenium.webdriver.common.by import By

class OrderPageLocators:

    ORDER_NAV = [By.XPATH, '//div[contains(@class, "Header_Nav")]/button[contains(@class, "Button")]']
    ORDER_FOOTER = [By.XPATH, '//button[contains(@class, "Middle") and contains(text(), "Заказать")]']

    FIELD_NAME = [By.XPATH, '//input[contains(@placeholder, "Имя")]']
    FIELD_SURNAME = [By.XPATH, '//input[contains(@placeholder, "Фамилия")]']
    FIELD_ADDRESS = [By.XPATH, '//input[contains(@placeholder, "Адрес")]']
    FIELD_METRO_STATION = [By.XPATH, '//input[contains(@placeholder, "метро")]']
    FIELD_SELECT_METRO_STATION = [By.XPATH, 
                                  '//div[contains(text(), "Румянцево")]']
    FIELD_PHONE_NUMBER = [By.XPATH, '//input[contains(@placeholder, "Телефон")]']
    BUTTON_FURTHER = [By.XPATH, '//button[contains(text(), "Далее")]']

    FIELD_DATA_BRING_SCOOTER = [By.XPATH, '//input[contains(@placeholder, "Когда привезти самокат")]']
    DROPDOWN_RENTAL_PERIOD = [By.CLASS_NAME, 'Dropdown-arrow']
    SELECT_DROPDOWN_RENTAL_PERIOD = [By.XPATH, '//div[@class="Dropdown-option" and contains(text(), "сутки")]']
    CHECKBOX_BLACK = [By.ID, 'black']
    CHECKBOX_GRAY = [By.ID, 'grey']
    BUTTON_ORDER = [By.XPATH, '//button[contains(@class, "Middle") and contains(text(), "Заказать")]']
    BUTTON_YES = [By.XPATH, '//button[contains(text(), "Да")]']

    TITLE_ORDER_CONFIRMED = [By.XPATH, 
                             '//div[contains(@class, "Order_ModalHeader") and contains(text(), "Заказ оформлен")]']
    BUTTON_VIEW_STATUS = [By.XPATH, '//button[contains(text(), "Посмотреть статус")]']

    