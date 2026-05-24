from pages.product_detail_page import ProductDetailPage

def test_change_color(driver):
	product_detail = ProductDetailPage(driver)
	product_detail.select_color_gray()
	chnge_color = product_detail.is_color_selected("Gray")
	assert chnge_color == True

def test_add_zero_qty(driver):
	product_detail = ProductDetailPage(driver)
	qty = product_detail.get_quantity()
	for _ in range(qty):
		product_detail.decrase_quantity()
	is_enable = product_detail.is_add_to_cart_enabled()
	assert is_enable == False

def test_increase_quantity(driver):
	product_detail = ProductDetailPage(driver)
	qty_before = product_detail.get_quantity()
	product_detail.increase_quantity()
	qty_after = product_detail.get_quantity()
	assert qty_after == qty_before + 1

def test_decrase_quantity(driver):
	product_detail = ProductDetailPage(driver)
	product_detail.increase_quantity()
	qty_before = product_detail.get_quantity()
	product_detail.decrase_quantity()
	qty_after = product_detail.get_quantity()
	assert qty_after == qty_before - 1

#for cart blank
def test_add_to_cart(driver):
	product_detail = ProductDetailPage(driver)
	qty = product_detail.get_quantity()
	product_detail.tap_add_to_cart()
	c_update = product_detail.is_cart_updated()
	c_qty = product_detail.get_quantity_cart()
	assert c_update != "" and qty == c_qty

#for cart not blank
def test_add_to_cart_existing(driver):
	product_detail = ProductDetailPage(driver)
	qty_cart_b = product_detail.get_quantity_cart()
	qty = product_detail.get_quantity()
	product_detail.tap_add_to_cart()
	qty_cart_a = product_detail.get_quantity_cart()
	assert qty_cart_a == qty_cart_b + qty