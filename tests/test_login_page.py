import pytest

from page_objects.logged_in_successfully import LoggedInSuccessfully
from page_objects.login_page import LoginPage


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login('student', 'Password123')

        login_success = LoggedInSuccessfully(driver)
        assert login_success.expected_url == login_success.current_url, 'URL address is not expected'
        assert login_success.header == 'Logged In Successfully', 'Header is not expected'
        assert login_success.is_logout_btn_displayed(), 'Logout button should be visible'
