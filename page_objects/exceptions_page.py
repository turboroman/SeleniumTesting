from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    __url = 'https://practicetestautomation.com/practice-test-exceptions/'
    __add_btn = (By.ID, 'add_btn')
    __edit_btn = (By.ID, 'edit_btn')
    __confirmation = (By.ID, 'confirmation')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def click_add_btn(self):
        super()._click(self.__add_btn)

    def click_edit_btn(self):
        super()._click(self.__edit_btn)

    def edit_row(self, row_number: int, text: str) -> str:
        self.click_edit_btn()
        input_field_locator = (By.CSS_SELECTOR, f'#row{row_number} input')
        super()._type(locator=input_field_locator, text=text)

    def get_row_value(self, row_number: int) -> str:
        input_field_locator = (By.CSS_SELECTOR, f'#row{row_number} input')
        input_field = super()._find(input_field_locator)
        return input_field.get_attribute('value')

    def is_row_displayed(self, row_number: int) -> bool:
        row_locator = (By.ID, f'row{row_number}')
        return super()._is_displayed(row_locator)

    def write_to_row(self, row_number: int, message: str):
        input_locator = (By.CSS_SELECTOR, f'#row{row_number} input')
        super()._find(input_locator).send_keys(message)

    def save_row(self, row_number: int):
        save_btn = (By.CSS_SELECTOR, f'#row{row_number} #save_btn')
        super()._click(save_btn)

    def get_confirmation_text(self) -> str:
        return super()._get_text(self.__confirmation)
