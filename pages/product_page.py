from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def tap_first_product(self):
        tap_product = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH, "(//android.widget.ImageView[@content-desc='Product Image'])[1]")))
        tap_product.click()

    def is_add_to_cart_visible(self):
        btn_cart = self.wait.until(EC.presence_of_element_located (
            (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt")))
        return True
        
    def txt_product(self):
        txt_product = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/productTV")))
        return txt_product.text
