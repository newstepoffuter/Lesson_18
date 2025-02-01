import allure
from test_webshop.pages.cart_page import add_product_api
from test_webshop.test_data.data import ID_1, PRODUCT_1, ID_2, PRODUCT_2


@allure.story('Добавление товара и проверка наличия в корзине')
def test_add_product_book():
    add_product_api.add_product(ID_1).show_cart().check_cart_product(PRODUCT_1)


@allure.story('Добавление товара и проверка наличия в корзине')
def test_add_product_laptop():
    add_product_api.add_product(ID_2).show_cart().check_cart_product(PRODUCT_2)
