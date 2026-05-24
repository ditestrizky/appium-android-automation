import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="session")
def driver():
	options = UiAutomator2Options()
	options.platform_name="Android"
	options.device_name = "RRCT404DTHY"
	options.app_package = "com.saucelabs.mydemoapp.android"
	options.app_activity = "com.saucelabs.mydemoapp.android.view.activities.MainActivity"
	options.no_reset = True

	driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
	yield driver
	driver.quit()
	