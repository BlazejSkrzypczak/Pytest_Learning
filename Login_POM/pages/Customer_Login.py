from selenium.webdriver.common.by import By


class Customer_Login:
    def __init__(self, driver):
        self.driver = driver
        self.email_input_field = (By.ID, "email")
        self.password_input_field = (By.ID, "pass")
        self.login_btn = (By.ID, "send2")

    def find_email_input_field(self):
        email_input_field = self.driver.find_element(*self.email_input_field)
        return email_input_field
    def find_password_input_field(self):
        password_input_field = self.driver.find_element(*self.password_input_field)
        return password_input_field
    def find_login_btn(self):
        login_btn = self.driver.find_element(*self.login_btn)
        return login_btn
