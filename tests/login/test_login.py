import pytest
from playwright.sync_api import Page, expect

from pages import Login, Channels


@pytest.mark.authentication
class TestLogin:
    def test_valid_login(self, page: Page) -> None:
        """Login with valid credentials.

        :param page: A Playwright browser page.
        """
        page.context.clear_cookies()
        login_page = Login(page)
        channels_page = Channels(page)

        login_page.navigate()
        login_page.fill_form({"userName": "marytwc09@gmail.com", "password": "qwerty12345"})
        login_page.submit_button.click()

        expect(channels_page.username_value_field).to_have_text("Wazzup: 9496-6880")
