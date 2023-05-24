from selenium.webdriver.common.by import By
from browser import Browser
from time import sleep
from selenium.common.exceptions import NoAlertPresentException


class Home_page(Browser):

    def open_home_page(self):
        self.chrome.get('https://www.mockflow.com/')

    def click_login_button(self):
        login_button = self.chrome.find_element(By.ID, "mfHeaderLoginBtn")
        login_button.click()
        sleep(1)

    def insert_email(self):
        user_email = self.chrome.find_element(By.ID, "logusername")
        user_email.send_keys("rapunzell2000@yahoo.com")
        sleep(1)

    def insert_password(self):
        user_password = self.chrome.find_element(By.ID, "logpassword")
        user_password.send_keys("Ianuarie_01")
        sleep(2)

    def insert_invalid_password(self):
        user_password = self.chrome.find_element(By.ID, "logpassword")
        user_password.send_keys("alabalaportocala")
        sleep(2)

    def click_singin_button(self):
        singin_button = self.chrome.find_element(By.ID, "login_btn")
        singin_button.click()
        sleep(2)

    def my_account_page(self):
        account_url = "https://wireframepro.mockflow.com/"
        assert self.chrome.current_url == account_url
        sleep(2)

    def login_failed(self):  # Folosesc metoda switch_to.alert pentru a interacționa cu fereastra de alertă și a confirma sau a închide mesajul de eroare.
        try:
            alerta = self.chrome.switch_to.alert
            alerta_text = alerta.text  # ca sa scot textul din alerta
            assert "Authentication Failed" in alerta_text
            alerta.accept()   # accept alerta
        except NoAlertPresentException:
            assert False, "Expected alert not found"
        sleep(2)
