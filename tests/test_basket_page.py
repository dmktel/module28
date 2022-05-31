import time
from pages.basket_page import BasketPage
from data import router, laptop, gpu


# # tests start in CLI wth this command
# python3 -m pytest --driver Chrome --driver-path ./chromedriver tests/test_basket_page.py

# login testing
def test_login(web_browser):
    page = BasketPage(web_browser)
    page.search_field.send_keys(router)
    page.search_button.click()
    # check right item found
    assert 'Keenetic Giant' in page.items_titles[0].text
    page.add_to_basket_link[0].click()
    page.basket_link.click()
    time.sleep(1)
    # check basket page header
    assert page.basket_page_header.get_text() == 'Корзина'
    # check item in the basket
    items_count = page.items_ids.count()
    assert items_count == 1
    # check right item in the basket
    assert page.items_ids[0].text == '384351'
    # check price * amount = sum item in the basket
    price_item_1 = int(page.prices_in_basket[0].text)
    sum_item_1 = int(page.sum_item_basket[0].text)
    total_sum = int(page.all_sum_basket.get_text())
    assert price_item_1 == sum_item_1 == total_sum
    # add second item
    page.search_field.send_keys(laptop)
    page.search_button.click()
    # check right items found
    items_founds_count = page.items_titles.count()
    for i in range(items_founds_count):
        assert 'Huawei MateBook 14S' in page.items_titles[i].text
    page.add_to_basket_link[0].click()
    page.basket_link.click()
    time.sleep(1)
    # check item in the basket
    items_count = page.items_ids.count()
    assert items_count == 2
    # check right item in the basket
    assert page.items_ids[1].text == '414118'
    # check price * amount = sum item in the basket
    price_item_2 = int(page.prices_in_basket[1].text)
    sum_item_2 = int(page.sum_item_basket[1].text)
    total_sum = int(page.all_sum_basket.get_text())
    assert price_item_2 == sum_item_2
    # check total sum right
    assert sum_item_1 + sum_item_2 == total_sum
    # add third item
    page.search_field.send_keys(gpu)
    page.search_button.click()
    # check right items found
    items_founds_count = page.items_titles.count()
    for i in range(items_founds_count):
        assert 'NVIDIA GeForce RTX3050' in page.items_titles[i].text
    page.add_to_basket_link[0].click()
    page.basket_link.click()
    time.sleep(1)
    # check item in the basket
    items_count = page.items_ids.count()
    assert items_count == 3
    # check right item in the basket
    assert page.items_ids[2].text == '418231'
    # check total sum items in the basket
    price_item_3 = int(page.prices_in_basket[2].text)
    sum_item_3 = int(page.sum_item_basket[2].text)
    total_sum = int(page.all_sum_basket.get_text())
    assert price_item_3 == sum_item_3
    # check total sum right
    assert sum_item_1 + sum_item_2 + sum_item_3 == total_sum
    # delete third item
    page.delete_button[2].click()
    items_count = page.items_ids.count()
    # check items in basket
    assert items_count == 2
    total_sum = int(page.all_sum_basket.get_text())
    # check total sum items in the basket
    assert sum_item_1 + sum_item_2 == total_sum
    # delete second item
    page.delete_button[1].click()
    items_count = page.items_ids.count()
    # check items in basket
    assert items_count == 1
    total_sum = int(page.all_sum_basket.get_text())
    # check total sum items in the basket
    assert sum_item_1 == total_sum
    # delete first item
    page.delete_button[0].click()
    # check items in basket
    assert page.empty_basket.get_text() == 'В корзине нет товаров.'










