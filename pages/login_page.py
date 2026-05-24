from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def txt_login(self):
        txt_login = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginTV")))
        return txt_login.text
        
    def enter_username(self, username):
        field = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")))
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET")))
        field.clear()
        field.send_keys(password)

    def tap_login(self):
        btn = self.wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn")))
        btn.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.tap_login()

    def get_error_message(self):
        err_msg =self.wait.until(EC.presence_of_element_located(
            (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/passwordErrorTV")))
        return err_msg.text

    def get_error_message_blank_username(self):
        err_msg_blank_username = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/nameErrorTV")))
        return err_msg_blank_username.text

    def get_error_message_blank_password(self):
        err_msg_blank_password = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/passwordErrorTV")))
        return err_msg_blank_password.text

    