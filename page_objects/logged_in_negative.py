from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoggedInNegative(BasePage):
    __error = (By.ID, 'error')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def is_error_displayed(self) -> bool:
        return super()._is_displayed(self.__error)

    @property
    def get_error_message(self) -> str:
        return super()._get_text(self.__error)
