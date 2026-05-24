from pages.navigation_page import NavigationPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage

def test_move_to_catalog(driver):
	nav_page = NavigationPage(driver)
	product = ProductPage(driver)
	nav_page.open_menu()
	nav_page.go_to_catalog()
	result = product.txt_product()
	assert result != ""

def test_move_login(driver):
	nav_page = NavigationPage(driver)
	login = LoginPage(driver)
	nav_page.open_menu()
	nav_page.go_to_login()
	result = login.txt_login()
	assert result !=""

