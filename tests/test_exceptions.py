import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.exceptions_page import ExceptionsPage


class TestExceptions:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.click_add_btn()
        assert exceptions_page.is_row_displayed(row_number=2)

    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.click_add_btn()
        exceptions_page.write_to_row(row_number=2, message='some text')
        exceptions_page.save_row(row_number=2)
        assert exceptions_page.get_confirmation_text() == 'Row 2 was saved'

    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.edit_row(row_number=1, text='new thing')
        exceptions_page.save_row(row_number=1)

        assert exceptions_page.get_row_value(row_number=1) == 'new thing'
        assert exceptions_page.get_confirmation_text() == 'Row 1 was saved'

    @pytest.mark.exceptions
    def test_timeout_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()
        exceptions_page.click_add_btn()

        assert exceptions_page.is_row_displayed(row_number=2)
