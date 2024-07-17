from selenium.webdriver.common.by import By

from Login_POM.pages.Customer_Login import Customer_Login
import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_customer_login(driver):
    driver.get("http://demo-store.seleniumacademy.com/")
    driver.set_window_size(1800, 933)
    driver.find_element(By.XPATH, "//*[@id='header']/div/div[2]/div/a/span[2]").click()
    driver.find_element(By.XPATH, "//*[@id='header-account']/div/ul/li[6]/a").click()
    customer_login_page = Customer_Login(driver)
    email_input_field = customer_login_page.find_email_input_field()
    password_input_field = customer_login_page.find_password_input_field()
    login_btn = customer_login_page.find_login_btn()

    email_input_field.send_keys("user@seleniumacademy.com")
    password_input_field.send_keys("tester")
    login_btn.click()
    assert driver.title == "My Account"
