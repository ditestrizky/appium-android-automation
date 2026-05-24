from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_color_black(self):
        chs_color = self.wait.until(EC.element_to_be_clickable(
            (AppiumBy.XPATH,"//android.widget.ImageView[@content-desc='Black color']")))
        chs_color.click()

    def select_color_blue(self):
        chs_color = self.wait.until(EC.element_to_be_clickable(
            (AppiumBy.XPATH,"//android.widget.ImageView[@content-desc='Blue color']")))
        chs_color.click()

    def select_color_gray(self):
        chs_color = self.wait.until(EC.element_to_be_clickable(
            (AppiumBy.XPATH,"//android.widget.ImageView[@content-desc='Gray color']")))
        chs_color.click()

    def select_color_green(self):
        chs_color = self.wait.until(EC.element_to_be_clickable(
            (AppiumBy.XPATH,"//android.widget.ImageView[@content-desc='Green color']")))
        chs_color.click()

    def is_color_selected(self, color):
        selected = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH, f"//android.view.ViewGroup[.//android.widget.ImageView[@content-desc='Indicates when color is selected'] and .//android.widget.ImageView[@content-desc='{color} color']]")))
        return True

    def tap_add_to_cart(self):
        tap_cart = self.wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/cartBt")))
        tap_cart.click()

    def is_cart_updated(self):
        cart = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/cartTV")))
        return True
        
    def is_add_to_cart_enabled(self):
        btn = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/cartBt")))
        return btn.is_enabled()

    def decrase_quantity(self):
        min_qty = self.wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/minusIV")))
        min_qty.click()

    def increase_quantity(self):
        add_qty =self.wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/plusIV")))
        add_qty.click()

    def get_quantity(self):
        qty = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/noTV")))
        return int(qty.text)

    def get_quantity_cart(self):
        c_qty = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/cartTV")))
        return int(c_qty.text)