import os
import shutil
from pathlib import Path

from selenium.common import WebDriverException
from selenium.webdriver.common.by import By

from data.locators import TestPageLocators
from pages.base_page import BasePage
from tests.base_test import config


class Page(BasePage):
    shutil.rmtree(Path(__file__).parent / "../results")
    os.mkdir(Path(__file__).parent / "../results")

    def __init__(self, driver, wait):
        self.locator = TestPageLocators
        super().__init__(driver, wait)

    def go_to_test_page(self):
        try:
            self.go_to_page(config()['url'])
        except WebDriverException:
            raise WebDriverException('Incorrect url entered')

    def registration(self):
        self.driver.find_element(*self.locator.NAME_INPUT).send_keys(config()['name'])

        self.driver.find_element(*self.locator.LASTNAME_INPUT).send_keys(config()['last_name'])

        gender_parent_element = self.driver.find_element(*self.locator.GENDER_RADIO_PARENT)
        self.driver.execute_script('arguments[0].click();',
                                   gender_parent_element.find_element(By.XPATH,
                                                                      '//input[@value="' + config()['gender'] + '"]'))

        self.driver.find_element(*self.locator.MOBILE_INPUT).send_keys(config()['mobile'])

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*self.locator.SUBMIT_BUTTON).click()
