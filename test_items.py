import time

print("Hello")


def test_should_be_button_add_to_basket(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    add_to_basket_button = browser.find_element("xpath", "//button[contains(@class, 'add-to-basket')]")
    assert add_to_basket_button.is_displayed(), "Отсутствует кнопка добавления в корзину"
    time.sleep(5)