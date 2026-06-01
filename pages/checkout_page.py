from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckOutPage:
	def __init__(self,driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10)

	def enter_fullname(self,fullname):
		enter_fullname = self.wait.until(EC.presence_of_element_located(
			(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/fullNameET")))
		enter_fullname.clear()
		enter_fullname.send_keys(fullname)

	def enter_address1(self,address1):
		enter_address1 = self.wait.until(EC.presence_of_element_located(
			(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/address1ET")))
		enter_address1.clear()
		enter_address1.send_keys(address1)

	def enter_address2(self,address2):
		enter_address2 = self.wait.until(EC.presence_of_element_located(
			(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/address2ET")))
		enter_address2.clear()
		enter_address2.send_keys(address2)

	def enter_city(self,city):
		enter_city = self.wait.until(EC.presence_of_element_located(
			(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/cityET")))
		enter_city.clear()
		enter_city.send_keys(city)

	def enter_state(self,state):
		enter_state = self.wait.until(EC.presence_of_element_located(
			(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/stateET")))
		enter_state.clear()
		enter_state.send_keys(state)

	def enter_zipcode(self,zipcode):
		enter_zip = self.wait.until(EC.presence_of_element_located(
			(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/zipET")))
		enter_zip.clear()
		enter_zip.send_keys(zipcode)

	def enter_country(self,country):
		enter_country = self.wait.until(EC.presence_of_element_located(
			(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/countryET")))
		enter_country.clear()
		enter_country.send_keys(country)

	def click_checkout(self):
		btn = self.wait.until(EC.element_to_be_clickable(
			(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/paymentBtn")))
		btn.click()

	def checkout(self,fullname,address1,address2,city,state,zipcode,country):
		self.enter_fullname(fullname)
		self.address1(address1)
		self.enter_address2(address2)
		self.enter_city(city)
		self.enter_state(state)
		self.enter_zipcode(zipcode)
		self.enter_country(country)
		self.click_checkout()

	

		
