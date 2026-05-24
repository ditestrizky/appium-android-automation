from pages.product_page import ProductPage
from pages.product_detail_page import ProductDetailPage

def test_product(driver):
	product = ProductPage(driver)
	product.tap_first_product()
	cart = product.is_add_to_cart_visible()
	assert cart == True

