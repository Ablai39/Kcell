from selenium.webdriver.common.by import By


class TestPageLocators:
    NAME_INPUT = (By.XPATH, '//*[@id="firstName"]')
    LASTNAME_INPUT = (By.XPATH, '//*[@id="lastName"]')
    GENDER_RADIO_PARENT = (By.XPATH, '//*[@id="genterWrapper"]/div[2]')
    MOBILE_INPUT = (By.XPATH, '//*[@id="userNumber"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="submit"]')
