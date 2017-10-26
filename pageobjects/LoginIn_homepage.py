# encoding=utf-8
from base_page import BasePage


class HomePage(BasePage):

    def send_number1(self):
        self.click("LoginPage", "number1")

    def send_number2(self):
        self.click("LoginPage", "number2")
