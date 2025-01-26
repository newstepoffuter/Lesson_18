import allure
from selene import browser, have
import requests


class AddProductCart:

    @allure.story('Добавление товара через endpoint')
    def add_product(self, id_product):
        url = 'https://demowebshop.tricentis.com/addproducttocart/catalog/'
        with allure.step('Отправка запроса с указанным id товара'):
            response = requests.post(url + id_product)
        with allure.step('Проверка кода ответа'):
            assert response.status_code == 200
        with allure.step('Получение cookie'):
            self.cookie = response.cookies.get('Nop.customer')
        return self

    @allure.story('Просмотр корзины')
    def show_cart(self):
        with allure.step('Открытие браузера'):
            browser.open('')
        with allure.step('Добавление cookie'):
            browser.driver.add_cookie({"name": "Nop.customer", "value": self.cookie})
        with allure.step('Перезагрузка браузера'):
            browser.driver.refresh()
        return self

    @allure.story('Проверка добавленных товаров в корзине')
    def check_cart_product(self, name_product):
        with allure.step('Проверка наименования товара'):
            browser.element('.product-name').should(have.text(name_product))
        return self


add_product_api = AddProductCart()
