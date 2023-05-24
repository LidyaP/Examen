import string

from selenium.webdriver.common.by import By
from browser import Browser
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


def generate_random_word():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(3))
    # '' - cu asta ii spunem ca literele sa nu fie separate
    # join - este folosit pt a concatena toate elementele generate intr-un singur sir de caractere


class My_dashboard(Browser):
    RANDOM_WORD = generate_random_word()
    PROMO = (By.ID, "mfUpgradePromo")
    TOUR = (By.XPATH, '//div[@id="mfProductTourIntroModal"]//button[@class="close mfProductTourClose mfThemeColorTxt"]')
    TOUR_DESIGN = (By.ID, "mfProductTourIntroModal")

    def i_see_the_offer(self):
        upgrade_offer = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(self.PROMO))
        assert upgrade_offer.is_displayed()
        sleep(1)

    def close_offer(self):
        offer = self.chrome.find_element(By.ID, "mfUpgradePromoClose")
        offer.click()
        sleep(1)

    def offer_is_closed(self):
        upgrade_offer = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.PROMO))
        assert not upgrade_offer.is_displayed()

    def add_button(self):
        new_space = self.chrome.find_element(By.ID, "mfDesignSpaceadd")
        new_space.click()
        sleep(1)

    def name_your_space(self):
        name_space = self.chrome.find_element(By.ID, "mfNewDesignSpaceText")
        name_space.send_keys(f"{self.RANDOM_WORD}")
        sleep(1)

    def create_your_space(self):
        create_space = self.chrome.find_element(By.ID, "mfNewDesignSpaceCreateBtn")
        create_space.click()
        sleep(1)

    def my_new_space(self):
        my_space = self.chrome.find_element(By.ID, "mfSpaceTitleID")
        actual_name_space = my_space.text
        assert self.RANDOM_WORD == actual_name_space, f"Error, the message is incorrect. Expected: " \
                                                      f"{self.RANDOM_WORD}, actual {actual_name_space}"
        sleep(1)

    def i_see_design_tour(self):
        tour_1 = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(self.TOUR_DESIGN))
        assert tour_1.is_displayed()
        sleep(1)

    def close_design_tour(self):
        self.chrome.find_element(*self.TOUR).click()

    def design_tour_is_closed(self):
        tour_2 = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.TOUR_DESIGN))
        assert not tour_2.is_displayed()

    def myfirst_create(self):
        first_create = self.chrome.find_element(By.CSS_SELECTOR, "#mfSpaceThumbItem_mfuidrawing_new")
        first_create.click()
        sleep(1)

    def wireframe_name(self):
        wireframe_1 = self.chrome.find_element(By.ID, "newProjectHTML5Title")
        wireframe_1.send_keys(f"{self.RANDOM_WORD}")
        sleep(1)

    def ui_pack(self):
        ui = self.chrome.find_element(By.ID, "mfSearchCategoryInput")
        bank_pack = self.chrome.find_element(By.ID, "mfComponentCategoryItem_Dbef2366b7e258e64d1a41a8af8496ec6")
        ui.send_keys("Bank UI pack")
        bank_pack.click()
        sleep(1)

    def my_new_wireframe(self):
        new_tab = self.chrome.window_handles
        self.chrome.switch_to.window(new_tab[-1])
        current_url = self.chrome.current_url
        partial_url = "https://wireframepro.mockflow.com/editor.jsp?editor=on&publicid="
        assert partial_url in current_url, f"the current url {current_url} does not contain {partial_url} "
        sleep(2)
        self.chrome.close()
        self.chrome.switch_to.window(self.chrome.window_handles[0])
        sleep(2)

    def settings_in_wireframe(self):
        space_settings = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located
                                                         ((By.ID, "mfSpaceSettingsIconLink")))
        space_settings.click()
        rename_option = WebDriverWait(self.chrome, 2).until(
            EC.presence_of_element_located((By.ID, "mfRenameSpace"))
        )
        rename_option.click()
        sleep(1)

    def rename_name(self):
        old_name = WebDriverWait(self.chrome, 1).until(EC.presence_of_element_located((By.ID, "mfRenameSpaceInput")))
        new_name = "Test1"
        old_name.clear()
        old_name.send_keys(new_name)
        sleep(1)

    def confirm_rename(self):
        confirm_button = self.chrome.find_element(By.ID, "mfSpaceRenameBtn")
        confirm_button.click()
        sleep(1)

    def check_the_rename(self):
        renamed_wireframe = WebDriverWait(self.chrome, 3).until(
            EC.presence_of_element_located((By.ID, "mfSpaceTitleID"))
        )
        assert renamed_wireframe.text == "Test1"
        sleep(1)



