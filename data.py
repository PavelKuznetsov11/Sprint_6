from locators.base_page_locators import BasePageLocators as BPL
from locators.home_page_locators import HomePageLocators as HPL
from locators.order_page_locators import OrderPageLocators as OPL
from urls import Urls

class Data:
    locs = [
    (OPL.ORDER_NAV, OPL.CHECKBOX_BLACK, BPL.LOGO_YANDEX, Urls.DZEN_PAGE_URL, 
         "Игорь", "Петров", "Озёрная улица, 230", "+79304201059", "10.02.2026"),

        (OPL.ORDER_FOOTER, OPL.CHECKBOX_GRAY, BPL.LOGO_SCOOTER, Urls.HOME_PAGE_URL, 
         "Владимир", "Сидоров", "Звёздная улица, 140", "+79852104539", "06.02.2026")
    ]

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