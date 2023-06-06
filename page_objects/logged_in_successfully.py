from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoggedInSuccessfully(BasePage):
    __url = 'https://practicetestautomation.com/logged-in-successfully/'
    __header = (By.CSS_SELECTOR, 'h1')
    __logout_btn = (By.LINK_TEXT, 'Log out')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def header(self) -> str:
        return super()._get_text(self.__header)

    def is_logout_btn_displayed(self) -> bool:
        return super()._is_displayed(self.__logout_btn)

