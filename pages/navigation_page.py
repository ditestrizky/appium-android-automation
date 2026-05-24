from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NavigationPage:
	def __init__(self,driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10)

	def open_menu(self):
		menu = self.wait.until(EC.element_to_be_clickable(
			(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/menuIV")))
		menu.click()

	def go_to_catalog(self):
		m_catalog = self.wait.until(EC.element_to_be_clickable(
			(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.saucelabs.mydemoapp.android:id/itemTV' and @text='Catalog']")))
		m_catalog.click()

	def go_to_webview(self):
		m_webview = self.wait.until(EC.element_to_be_clickable(
			(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.saucelabs.mydemoapp.android:id/itemTV' and @text='WebView']")))
		m_webview.click()

	def go_to_login(self):
		m_login = self.wait.until(EC.element_to_be_clickable(
			(AppiumBy.XPATH, "//android.widget.TextView[@content-desc='Login Menu Item']")))
		m_login.click()