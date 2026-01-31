import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators as BPL
from urls import Urls

@pytest.fixture
def create_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture
def home_driver(create_driver):
    create_driver.get(Urls.HOME_PAGE_URL)
    return create_driver
