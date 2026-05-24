from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_login_valid(driver):
    login = LoginPage(driver)
    login.login("bob@example.com", "10203040")
    home = HomePage(driver)
    cek_login = home.txt_product()
    assert cek_login !=""
    driver.save_screenshot("screenshots/test_login_valid.png")
    home.tap_menu()
    home.tap_logout()
    home.tap_confirm_logout()

def test_login_invalid(driver):
    login = LoginPage(driver)
    login.login("alice@example.com (locked out)","10203040")
    error = login.get_error_message()
    assert error != ""
    driver.save_screenshot("screenshots/test_login_invalid.png")

def test_login_blank_username(driver):
    login = LoginPage(driver)
    login.login("","asd")
    error = login.get_error_message_blank_username()
    assert error != ""
    driver.save_screenshot("screenshots/test_login_blank_username.png")

def test_login_blank_password(driver):
    login = LoginPage(driver)
    login.login("bob@example.com", "")
    error = login.get_error_message_blank_password()
    assert error != ""
    driver.save_screenshot("screenshots/test_login_blank_password.png")



