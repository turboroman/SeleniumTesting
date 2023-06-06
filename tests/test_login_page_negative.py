import pytest

from page_objects.logged_in_negative import LoggedInNegative
from page_objects.login_page import LoginPage


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [('incorrectUser', 'Password123', 'Your username is invalid!'),
                              ('student', 'incorrectPassword', 'Your password is invalid!')])
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username=username, password=password)

        logged_in_negative = LoggedInNegative(driver)
        assert logged_in_negative.is_error_displayed(), 'Error is not displayed'
        assert expected_error_message == logged_in_negative.get_error_message, 'Error message is not correct'
