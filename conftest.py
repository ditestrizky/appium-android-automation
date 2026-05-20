import pytest
from appium import webdriver
from appium.options import UiAutomator2Options

@pytest.fixture(scope="session")
def driver():
	options = UiAutomator2Options()
	options.platrom_name="Android"
	options.device_name = "RRCT404DTHY"
	options.app_package = "com.saucelabs.mydemoapp.android"
	options.app_activity = "com.saucelabs.mydemoapp.android.view.activities.MainActivity"
	options.no_reset = True

	driver = webdriver.Remote("htttp://127.0.0.01:4723", options=options)
	yield webdriver
	driver.quit()
	