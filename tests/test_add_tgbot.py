import pytest
from playwright.sync_api import Page, expect

from pages import Login, Channels, TelegramChannelAddition


@pytest.mark.authentication
class TestChannel:
    def test_add_tgbot(self, page: Page) -> None:
        page.context.clear_cookies()
        login_page = Login(page)
        channels_page = Channels(page)
        telegram_channel_addition = TelegramChannelAddition(page)

        login_page.login({"userName": "marytwc09@gmail.com", "password": "qwerty12345"})
        expect(channels_page.username_value_field).to_have_text("Wazzup: 9496-6880")

        channels_page.add_channel("Telegram")

        telegram_channel_addition.add_tgbot("7075597043:AAEGAYWoS6XJzDoM43rI4l55vaJJT3cuEb4")
        telegram_channel_addition.submit_tgbot_add_button.click()

        expect(channels_page.page.get_by_text("mashatestwz_bot")).to_be_visible()

