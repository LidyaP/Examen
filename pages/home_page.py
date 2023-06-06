from selenium.webdriver.common.by import By
from browser import Browser
from time import sleep
from selenium.common.exceptions import NoAlertPresentException


class Home_page(Browser):
    LOGIN_BUTTON = (By.ID, "mfHeaderLoginBtn")
    EMAIL = (By.ID, "logusername")
    PASSWORD = (By.ID, "logpassword")
    SIGN_IN = (By.ID, "login_btn")

    def open_home_page(self):
        self.chrome.get('https://www.mockflow.com/')

    def click_login_button(self):
        max_try = 3
        attempts = 0
        while attempts < max_try:
            try:
                login_button = self.chrome.find_element(*self.LOGIN_BUTTON)
                if login_button:
                    login_button.click()
                    sleep(1)
                    break
                else:
                    raise AssertionError("Login button element not found.")
            except Exception as i:
                print(f"An error occurred while clicking the login button: {str(i)}")
                attempts += 1

    def insert_email(self):
        try:
            user_email = self.chrome.find_element(*self.EMAIL)
            user_email.send_keys("rapunzell2000@yahoo.com")
            sleep(1)
        except Exception as i:
            print(f"An error occurred while inserting the email: {str(i)}")

    def insert_password(self):
        try:
            user_password = self.chrome.find_element(*self.PASSWORD)
            user_password.send_keys("Ianuarie_01")
            sleep(1)
        except Exception as i:
            print(f"An error occurred while inserting the password: {str(i)}")

    def insert_invalid_password(self, password):
        try:
            user_password = self.chrome.find_element(*self.PASSWORD)
            user_password.send_keys(password)
            sleep(1)
        except Exception as i:
            print(f"An error occurred while inserting the invalid password: {str(i)}")

    def click_signin_button(self):
        try:
            signin_button = self.chrome.find_element(*self.SIGN_IN)
            signin_button.click()
            sleep(1)
        except Exception as i:
            print(f"An error occurred while clicking the signin button: {str(i)}")

    def my_account_page(self):
        account_url = "https://wireframepro.mockflow.com/"
        assert self.chrome.current_url == account_url
        sleep(1)

    def login_failed(self, error_message):
        try:
            alerta = self.chrome.switch_to.alert
            alerta_text = alerta.text
            assert error_message in alerta_text
            alerta.accept()
        except NoAlertPresentException:
            assert False, "Expected alert not found"
        sleep(1)
