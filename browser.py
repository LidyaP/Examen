from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Browser:
    s = Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=s)
    chrome.maximize_window()

    def maximise_window(self):
        self.chrome.maximize_window()

    def close_browser(self):
        self.chrome.quit()
