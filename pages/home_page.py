from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def tap_menu(self):
        smenu = self.wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/menuIV")))
        smenu.click()

    def tap_logout(self):
        btn = self.wait.until(EC.element_to_be_clickable(
            (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='Logout Menu Item']")))
        btn.click()

    def tap_confirm_logout(self):
        btn = self.wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID,"android:id/button1")))
        btn.click()

    def txt_product(self):
        txt_product = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/productTV")))
        return txt_product.text