import string

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from browser import Browser
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


def generate_random_word():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(4))
    # '' - cu asta ii spunem ca literele sa nu fie separate
    # join - este folosit pt a concatena toate elementele generate intr-un singur sir de caractere


class My_dashboard(Browser):
    RANDOM_WORD = generate_random_word()
    PROMO = (By.ID, "mfUpgradePromo")
    CLOSE_OFFER = (By.ID, "mfUpgradePromoClose")
    ADD_BUTTON = (By.ID, "mfDesignSpaceadd")
    NAME_SPACE = (By.ID, "mfNewDesignSpaceText")
    CREATE_SPACE = (By.ID, "mfNewDesignSpaceCreateBtn")
    MY_SPACE = (By.ID, "mfSpaceTitleID")
    TOUR = (By.XPATH, '//div[@id="mfProductTourIntroModal"]//button[@class="close mfProductTourClose mfThemeColorTxt"]')
    TOUR_DESIGN = (By.ID, "mfProductTourIntroModal")
    FIRST_CREATE = (By.CSS_SELECTOR, "#mfSpaceThumbItem_mfuidrawing_new")
    WIREFRAME = (By.ID, "newProjectHTML5Title")
    UI = (By.ID, "mfSearchCategoryInput")
    BANK = (By.ID, "mfComponentCategoryItem_Dbef2366b7e258e64d1a41a8af8496ec6")
    NAV_BAR = (By.ID, "mfNavStoreBtn")
    TEMPLATE_BAR = (By.CSS_SELECTOR, '.nav-item:nth-child(4) label[for="mfTypeTemplate"]')
    PACK = (By.XPATH, '//div[@id="mfStoreTemplateListing"]//span[@data-id="Ma7d167d8d5107404758352a79cdf5eda1683205477729"]')
    CHANGES = (By.ID, "mfUnSavedBtn")
    SPACE_SETTINGS = (By.ID, "mfSpaceSettingsIconLink")
    RENAME = (By.ID, "mfRenameSpace")
    RENAME_NAME = (By.ID, "mfRenameSpaceInput")
    RENAME_BUTTON = (By.ID, "mfSpaceRenameBtn")
    SPACE_ANALYTICS = (By.ID, "mfAnalyticsBtn")
    TEXT = (By.CSS_SELECTOR, '.mfSpaceAnalyticsBasicUsersContent p')
    CLICK_BACK = (By.XPATH, '//div[@class="mfSpaceAnalyticsBasicUsers"]/i[@class="mfSpaceAnalyticsCloseIcon mfFontIcon ico-right mfPtr"]')
    BACK_BUTTON = (By.ID, "mfCloseSpaceBtn")
    MY_ACCOUNT_SETTINGS = (By.ID, "mfAccountProfileImg")
    LOG_OUT = (By.ID, "mfAccountMenuLogout")
    WORKPLACE_TEST1 = (By.XPATH, '//*[@class="mfDashCard mfDefaultSpace ui-sortable-handle"]//div[@class="mfDashCardLabel mfOverflowTip mfThemeColorTxt"]')
    DELETE = (By.ID, "mfDeleteDash")
    DELETE_SPACE = (By.ID, "mfDeleteSpacePass")
    DELETE_BTN = (By.ID, "mfSpaceDeleteBtn")

    def i_see_the_offer(self):
        upgrade_offer = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(self.PROMO))
        assert upgrade_offer.is_displayed()
        sleep(1)

    def close_offer(self):
        try:
            offer = self.chrome.find_element(*self.CLOSE_OFFER)
            offer.click()
            sleep(1)
        except Exception as i:
            print(f"An error occurred while closing the offer: {str(i)}")

    def offer_is_closed(self):
        maximum = 3
        attempts = 0
        while attempts < maximum:
            try:
                upgrade_offer = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.PROMO))
                assert not upgrade_offer.is_displayed()
                break
            except Exception as i:
                print(f"Attempt {attempts + 1} failed. Error: {str(i)}")
                attempts += 1

    def add_button(self):
        try:
            new_space = self.chrome.find_element(*self.ADD_BUTTON)
            new_space.click()
            sleep(1)
        except Exception as i:
            print(f"An error occurred while clicking the add button: {str(i)}")

    def name_your_space(self):
        try:
            name_space = self.chrome.find_element(*self.NAME_SPACE)
            name_space.send_keys(f"{self.RANDOM_WORD}")
            sleep(1)
        except Exception as i:
            print(f"An error occurred while naming the space: {str(i)}")

    def create_your_space(self):
        try:
            create_space = self.chrome.find_element(*self.CREATE_SPACE)
            create_space.click()
            sleep(1)
        except Exception as i:
            print(f"An error occurred while creating the space: {str(i)}")

    def my_new_space(self):
        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:
            try:
                my_space = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.MY_SPACE))
                actual_name_space = my_space.text
                assert self.RANDOM_WORD == actual_name_space, f"Error, the message is incorrect. Expected: " \
                                                                f"{self.RANDOM_WORD}, actual {actual_name_space}"
                break
            except Exception as i:
                print(f"Attempt {attempts + 1} failed. Error: {str(i)}")
                attempts += 1

    def i_see_design_tour(self):
        tour_1 = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(self.TOUR_DESIGN))
        assert tour_1.is_displayed()
        sleep(1)

    def close_design_tour(self):
        try:
            tour_element = self.chrome.find_element(*self.TOUR)
            if tour_element.is_displayed():
                tour_element.click()
        except Exception as i:
            print(f"An error occurred while closing the design tour: {str(i)}")

    def design_tour_is_closed(self):
        tour_2 = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.TOUR_DESIGN))
        assert not tour_2.is_displayed()

    def myfirst_create(self):
        try:
            first_create = self.chrome.find_element(*self.FIRST_CREATE)
            if first_create.is_displayed():
                first_create.click()
                sleep(1)
        except Exception as i:
            print(f"An error occurred while performing UI drawing: {str(i)}")

    def wireframe_name(self):
        try:
            wireframe_1 = self.chrome.find_element(*self.WIREFRAME)
            wireframe_1.send_keys(f"{self.RANDOM_WORD}")
            sleep(1)
        except Exception as i:
            print(f"An error occurred while setting the wireframe name: {str(i)}")

    def ui_pack(self):
        try:
            ui = self.chrome.find_element(*self.UI)
            bank_pack = self.chrome.find_element(*self.BANK)
            if ui and bank_pack:
                ui.send_keys("Bank UI pack")
                bank_pack.click()
                sleep(1)
            else:
                raise AssertionError("UI or bank pack elements not found.")
        except Exception as i:
            print(f"An error occurred while selecting the UI pack: {str(i)}")

    def my_new_wireframe(self):
        new_tab = self.chrome.window_handles
        self.chrome.switch_to.window(new_tab[-1])
        current_url = self.chrome.current_url
        partial_url = "https://wireframepro.mockflow.com/editor.jsp?editor=on&publicid="
        assert partial_url in current_url, f"the current url {current_url} does not contain {partial_url} "
        sleep(2)

    def store_icon(self):
        nav_bar = self.chrome.find_element(*self.NAV_BAR)
        if nav_bar:
            nav_bar.click()
            sleep(1)
        else:
            raise AssertionError("Navigation bar not found.")

    def template_tab(self):
        template_bar = self.chrome.find_element(*self.TEMPLATE_BAR)
        if template_bar:
            template_bar.click()
            sleep(1)
        else:
            raise AssertionError("Template tab not found.")

    def marketing_pack_email(self):
        max_trys = 3
        attempts = 0
        while attempts < max_trys:
            try:
                pack = WebDriverWait(self.chrome, 3).until(EC.visibility_of_element_located(self.PACK))
                if pack:
                    pack.click()
                    sleep(1)
                    break
                else:
                    raise AssertionError("Pack element not found.")
            except Exception as i:
                print(f"Attempt {attempts + 1} failed. Error: {str(i)}")
                attempts += 1

    def save_changes(self):
        try:
            changes = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.CHANGES))
            changes.click()
            sleep(1)
            self.chrome.close()
            self.chrome.switch_to.window(self.chrome.window_handles[0])
            sleep(2)
        except Exception as i:
            print(f"An error occurred while saving changes: {str(i)}")

    def settings_in_wireframe(self):
        space_settings = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.SPACE_SETTINGS))
        if space_settings:
            space_settings.click()
            rename_option = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.RENAME))
            if rename_option:
                rename_option.click()
                sleep(1)
            else:
                raise AssertionError("Rename option not found.")
        else:
            raise AssertionError("Space settings not found.")

    def rename_name(self):
        try:
            old_name = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.RENAME_NAME))
            new_name = "Test1"
            old_name.clear()
            old_name.send_keys(new_name)
            sleep(1)
        except Exception as i:
            print(f"An error occurred while renaming the name: {str(i)}")

    def confirm_rename(self):
        try:
            confirm_button = self.chrome.find_element(*self.RENAME_BUTTON)
            confirm_button.click()
            sleep(1)
        except Exception as i:
            print(f"An error occurred while confirming the rename: {str(i)}")

    def check_the_rename(self):
        maxim = 3
        attempts = 0
        while attempts < maxim:
            try:
                renamed_wireframe = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.MY_SPACE))
                assert renamed_wireframe.text == "Test1"
                break
            except Exception as i:
                print(f"Attempt {attempts + 1} failed. Error: {str(i)}")
                attempts += 1
                sleep(1)

    def space_analytics(self):
        try:
            analytics = self.chrome.find_element(*self.SPACE_ANALYTICS)
            analytics.click()
            sleep(1)
        except Exception as i:
            print(f"An error occurred while i click the space analytics: {str(i)}")

    def analytics_message(self):
        text_element = self.chrome.find_element(*self.TEXT)
        message = text_element.text
        expected_text = "Space analytics is available"
        try:
            assert message == expected_text
            print("Message text is correct: '{}'".format(message))
        except AssertionError:
            print("Message text is incorrect. Expected: '{}'. Actual: '{}'".format(expected_text, message))

    def click_back_button(self):
        try:
            click_back = self.chrome.find_element(*self.CLICK_BACK)
            click_back.click()
            sleep(1)
            print("Clicked on the back button")
        except Exception as i:
            print("Failed to click on the back button:", str(i))

    def back_in_my_workspace(self):
        current_url = self.chrome.current_url
        partial_url = "https://wireframepro.mockflow.com/#/space/"
        assert partial_url in current_url, f"the current url {current_url} does not contain {partial_url} "
        sleep(1)

    def escape_workspace(self):
        try:
            escape = self.chrome.find_element(*self.BACK_BUTTON)
            escape.click()
            sleep(1)
            print("Clicked on the back button")
        except Exception as i:
            print("Failed to click on the back button:", str(i))

    def back_in_my_home_page(self):
        current_url = self.chrome.current_url.rstrip('/')   # Elimină caracterul '/' de la sfârșit, dacă există
        expected = "https://wireframepro.mockflow.com"
        assert expected == current_url, f"the current url {current_url} is not as expected {expected} "

    def click_on_my_test1(self):
        name_element = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.WORKPLACE_TEST1))
        the_name = name_element.text
        expected_name = "Test1"
        try:
            assert the_name == expected_name
            print("Message text is correct: '{}'".format(the_name))
            name_element.click()
            sleep(1)
        except AssertionError:
            print("Message text is incorrect. Expected: '{}'. Actual: '{}'".format(expected_name, the_name))

    def settings_in_wireframe2(self):
        space_settings = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.SPACE_SETTINGS))
        if space_settings:
            space_settings.click()
            delete_option = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.DELETE))
            if delete_option:
                delete_option.click()
                sleep(1)
            else:
                raise AssertionError("Delete option not found.")
        else:
            raise AssertionError("Space settings not found.")

    def delete_message(self):
        delete_message = self.chrome.find_element(*self.DELETE_SPACE)
        delete_button = self.chrome.find_element(*self.DELETE_BTN)
        delete1 = "delete"
        while True:
            try:
               delete_message.send_keys(delete1)
               delete_button.click()
               alerta1 = self.chrome.switch_to.alert
               alerta1.accept()
               sleep(1)
               break
            except Exception as i:
                print("Exception occurred: {}".format(str(i)))

    def workplace_is_deleted(self):
        maximum = 3
        attempts = 0
        while attempts < maximum:
            try:
                deleted = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.WORKPLACE_TEST1))
                assert not deleted.is_displayed()
                break
            except Exception as i:
                print(f"Attempt {attempts + 1} failed. Error: {str(i)}")
                attempts += 1

    def settings_and_log_out(self):
        try:
            settings = self.chrome.find_element(*self.MY_ACCOUNT_SETTINGS)
            settings.click()
            sleep(1)
        except NoSuchElementException:
            print("Settings item not found.")
        try:
            log_out = self.chrome.find_element(*self.LOG_OUT)
            log_out.click()
            sleep(1)
        except NoSuchElementException:
            print("Log out button was not found.")

    def goodbye(self):
        current_link = self.chrome.current_url.rstrip('/')
        expected_link = "https://mockflow.com"
        assert expected_link == current_link, f"the current url {current_link} is not as expected {expected_link} "
