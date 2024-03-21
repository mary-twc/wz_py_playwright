from playwright.sync_api import Locator

from pages.wazzup.channels import Channels


class TelegramChannelAddition(Channels):
    @property
    def tgbot_token_field(self) -> Locator:
        return self.add_channel_dialog.get_by_label("Токен чат-бота")

    @property
    def submit_tgbot_add_button(self) -> Locator:
        return self.add_channel_dialog.locator("button:has-text('Добавить')")

    def add_tgbot(self, token:str):
        tg_bot_button = self.add_channel_dialog.locator(".channel-card", has_text="Telegram Bot")
        tg_bot_button.click()
        self.tgbot_token_field.fill(token)

