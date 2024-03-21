from playwright.sync_api._generated import Locator

from pages.base import Base


class Signup(Base):
    @property
    def userform(self) -> Locator:
        return self.page.locator(".signup")

    @property
    def email_field(self) -> Locator:
        return self.userform.get_by_label("Электронная почта")

    @property
    def submit_register_button(self) -> Locator:
        return self.userform.get_by_role("button", name="Зарегистрироваться")

    @property
    def userform_username(self) -> Locator:
        return self.page.locator(".signup")

    @property
    def username_field(self) -> Locator:
        return self.userform.get_by_label("Имя пользователя")

    @property
    def password_field(self) -> Locator:
        return self.userform.get_by_label("Пароль")

    @property
    def submit_continue_button(self) -> Locator:
         return self.userform.get_by_role("button", name="Продолжить")

    @property
    def userform_phonenumber(self) -> Locator:
        return self.page.locator(".signup")

    @property
    def phonenumber_field(self) -> Locator:
        return self.userform.get_by_label("Номер телефона")

    @property
    def submit_login_button(self) -> Locator:
         return self.userform.get_by_role("button", name="Сохранить и войти")

    def fill_form_email(self, new_user: dict) -> None:
        """Fill out the signup form.

        :param new_user: A user intended for login
        """
        self.email_field.fill(new_user["email"])

    def fill_form_username(self, new_user: dict) -> None:
        """Fill out the signup form.

        :param new_user: A user intended for login
        """
        self.username_field.fill(new_user["userName"])
        self.password_field.fill(new_user["password"])
    def fill_form_phonenumber(self, new_user: dict) -> None:
        """Fill out the signup form.

        :param new_user: A user intended for login
        """
        self.phonenumber_field.fill(new_user["phoneNumber"])

    def navigate(self) -> None:
        """Navigate to the signup page."""
        self.page.goto(f"{self.base_url}/signup")