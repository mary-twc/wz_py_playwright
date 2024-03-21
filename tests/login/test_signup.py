import pytest
import re
from playwright.sync_api import Page, expect


from pages import Login, Signup, Channels


from datetime import datetime

@pytest.mark.authentication
class TestSingup:
    def test_valid_signup(self, page: Page) -> None:
        """Signup with valid credentials.

        :param page: A Playwright browser page.
        """
        page.context.clear_cookies()
        login_page = Login(page)
        signup_page = Signup(page)
        channels_page = Channels(page)

        login_page.navigate()
        login_page.submit_log_reg_button.click()

        signup_page.navigate()
        email = f"qatest{str(datetime.utcnow().timestamp())}@testmail.ru"
        signup_page.fill_form_email({"email": email})
        signup_page.submit_register_button.click()

        signup_page.fill_form_username({"userName": "Маша тест", "password": "qwerty12345"})
        signup_page.submit_continue_button.click()

        signup_page.fill_form_phonenumber({"phoneNumber": "9999999999"})
        signup_page.submit_login_button.click()


        expect(channels_page.username_value_field).to_have_text(re.compile(r"Wazzup: [\d-]+"))

