from playwright.sync_api._generated import Locator

from pages.private import PrivatePage


class Channels(PrivatePage):
    @property
    def username_value_field(self) -> Locator:
        username_value = self.page.locator(".drawer-header")
        username_value.wait_for(state="visible")
        return username_value

    @property
    def channels_list(self) -> Locator:
        return self.page.locator(".channels-list")

    @property
    def add_channel_dialog(self) -> Locator:
        # диалоговое окно с выбором типа канала
        return self.page.get_by_role("dialog").filter(has_text="Добавление канала")

    @property
    def add_channel_button(self):
        return self.page.get_by_role("button", name="Добавить канал")

    def navigate(self) -> None:
        self.page.goto(f"{self.base_url}/settings/channels")

    def add_channel(self, channel_type):
        self.add_channel_button.click()
        channel_button = self.add_channel_dialog.locator(".channel-card", has_text=channel_type)
        channel_button.click()