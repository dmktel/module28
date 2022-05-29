import pytest
import time
from pages.main_page import MainPage
from data import valid_email_1, valid_password


# python3 -m pytest --driver Chrome --driver-path ./chromedriver tests/test_main_page.py
# python3 -m pytest --driver Firefox --driver-path ./geckodriver tests/test_main_page.py

# page access test
# def test_access_to_main_page(web_browser):
#     # Check that page is accessible
#     page = MainPage(web_browser)
#     assert "https://www.regard.ru/" in page.get_current_url()
#     time.sleep(1)


# login testing
# def test_login(web_browser):
#     page = MainPage(web_browser)
#     page.login_button.click()
#     page.field_email.send_keys(valid_email_1)
#     page.field_password.send_keys(valid_password)
#     page.enter_btn.click()
#
#
#     assert "https://www.regard.ru/" in page.get_current_url()

# about page link testing
# def test_about_page_link(web_browser):
#     page = MainPage(web_browser)
#     page.submenu_click()
#
#     assert page.about_page.get_text() == 'Общая информация'

# pc configuration page link testing
# def test_pc_configuration_page_link(web_browser):
#     page = MainPage(web_browser)
#     page.pc_configuration_page_link.click()
#
#     assert page.pc_configuration_page_header.get_text() == 'Конфигуратор ПК'


# paid page testing
# def test_paid_page_link(web_browser):
#     page = MainPage(web_browser)
#     page.paid_page_link.click()
#
#     assert page.paid_page_header.get_text() == 'Оплата'


# delivery page testing
# def test_delivery_page_link(web_browser):
#     page = MainPage(web_browser)
#     page.delivery_page_link.click()
#
#     assert page.delivery_page_header.get_text() == 'Доставка'


# pickup page testing
# def test_pickup_page_link(web_browser):
#     page = MainPage(web_browser)
#     page.pickup_page_link.click()
#
#     assert page.pickup_page_header.get_text() == 'Самовывоз / Пункты выдачи заказов'


# warranty page testing
# def test_warranty_page_link(web_browser):
#     page = MainPage(web_browser)
#     page.warranty_page_link.click()
#
#     assert page.warranty_page_header.get_text() == 'Гарантия и возврат товара'

# catalog by brends testing
# def test_catalog_by_brends_link(web_browser):
#     page = MainPage(web_browser)
#     page.catalog_by_brends.click()
#
#     assert page.first_brend.get_text() == '1MORE'

# catalog by types testing
# def test_catalog_by_types_link(web_browser):
#     page = MainPage(web_browser)
#     page.catalog_by_brends.click()
#     page.catalog_by_types.click()
#
#     assert page.first_type.get_text() == 'БЛОКИ ПИТАНИЯ'

# chargers page testing
# def test_chargers_page(web_browser):
#     page = MainPage(web_browser)
#     page.charges_link.click()
#     page.all_chargers_link.click()
#     page.wait_page_loaded(3)
#     assert page.page_chargers_header.get_text() == 'Блоки питания'

# def test_selling_page(web_browser):
#     page = MainPage(web_browser)
#     page.selling_link.click()
#     page.wait_page_loaded(3)
#
#     assert page.selling_page_header.get_text() == 'Распродажа (новые товары по сниженным ценам)'

# next page selling testing
# def test_selling_page(web_browser):
#     page = MainPage(web_browser)
#     page.selling_link.click()
#     page.wait_page_loaded(3)
#     page.scroll_down()
#     page.page2_link.click()
#     page.wait_page_loaded(3)
#     assert "https://www.regard.ru/sale?page=2" in page.get_current_url()
#     page.scroll_down()
#     page.page3_link.click()
#     page.wait_page_loaded(3)
#     assert "https://www.regard.ru/sale?page=3" in page.get_current_url()

# climate stuff page testing
# def test_climate_stuff_page(web_browser):
#     page = MainPage(web_browser)
#     page.appliance_link.click()
#     page.climates_stuff_link.click()
#     page.wait_page_loaded(3)
#     page.fan_staff_link.click()
#     page.wait_page_loaded(3)
#     page.scroll_down()
#     page.up_button_link.click()
#     page.wait_page_loaded(3)
#     assert page.fan_page_header.get_text() == 'Вентиляторы'
#     page.waterheater_stuff_link.click()
#     page.wait_page_loaded(3)
#     assert page.waterheater_page_header.get_text() == 'Водонагреватели'
#     page.weatherstations_stuff_link.click()
#     page.wait_page_loaded(3)
#     assert page.weatherstation_page_header.get_text() == 'Метеостанции'
#     page.mobile_conditions_stuff_link.click()
#     page.wait_page_loaded(3)
#     assert page.mobile_conditions_page_header.get_text() == 'Мобильные кондиционеры'
#     page.heaters_stuff_link.click()
#     page.wait_page_loaded(3)
#     assert page.heaters_page_header.get_text() == 'Обогреватели, конвекторы, тепловентиляторы'


# home stuff page testing
# def test_home_stuff_page(web_browser):
#     page = MainPage(web_browser)
#     page.appliance_link.click()
#     page.home_stuff_link.click()
#     page.overlocks_stuff_link.click()
#     page.wait_page_loaded(3)
#     assert page.overlocks_page_header.get_text() == 'Оверлоки'
#     page.steam_cleaners_stuff_link.click()
#     page.all_steam_cleaners_link.click()
#     page.wait_page_loaded(3)
#     assert page.all_steam_cleaner_header.get_text() == 'Пароочистители, отпариватели'
#     page.hoovers_stuff_link.click()
#     page.all_hoovers_stuff_link.click()
#     page.wait_page_loaded(3)
#     assert page.all_hoovers_header.get_text() == 'Пылесосы'
#     page.irons_stuff_link.click()
#     page.wait_page_loaded(3)
#     assert page.irons_page_header.get_text() == 'Утюги'
#     page.sewing_stuff_link.click()
#     page.wait_page_loaded(3)
#     assert page.sewing_page_header.get_text() == 'Швейные машины'


# GPUs page test
# def test_gpu_page(web_browser):
#     page = MainPage(web_browser)
#     page.gpus_link.click()
#     page.amd_radeon_link.click()
#     page.wait_page_loaded(3)
#     assert page.amd_radeon_header.get_text() == 'Видеокарты AMD Radeon'
#     page.amd_radeon_pro_link.click()
#     page.wait_page_loaded(3)
#     assert page.amd_radeon_pro_header.get_text() == 'Видеокарты AMD Radeon Pro'
#     page.nvidia_geforce_link.click()
#     page.wait_page_loaded(3)
#     assert page.nvidia_geforce_header.get_text() == 'Видеокарты NVIDIA GeForce'
#     page.nvidia_quadro_link.click()
#     page.wait_page_loaded(3)
#     assert page.nvidia_quadro_header.get_text() == 'Видеокарты NVIDIA Quadro'

# GPU AMD Radeon content testing
# def test_amd_radeon_page_content(web_browser):
#     page = MainPage(web_browser)
#     page.gpus_link.click()
#     page.amd_radeon_link.click()
#     page.wait_page_loaded(3)
#     # desktop acer page content exist testing
#     count_titles = page.items_titles.count()
#     assert count_titles > 0
#     for i in range(count_titles):
#         # desktop acer page all titles exist testing
#         assert page.items_titles[i].text != ''
#
#     count_images = page.items_images.count()
#     # desktop acer page images exist testing
#     assert count_images > 0
#     for i in range(count_images):
#         # desktop acer page all images exist testing
#         assert page.items_images[i].get_attribute('src') != ''


# HDD 2.5" page testing
# def test_hdd_2_page(web_browser):
#     page = MainPage(web_browser)
#     page.hdd_link.click()
#     page.hdd_2_link.click()
#     page.hdd_2_seagate_link.click()
#     page.wait_page_loaded(3)
#     assert page.hdd_2_seagate_page_header.get_text() == 'Жёсткие диски (HDD) SEAGATE (2.5")'
#     page.hdd_2_toshiba_link.click()
#     page.wait_page_loaded(3)
#     assert page.hdd_2_toshiba_page_header.get_text() == 'Жёсткие диски (HDD) TOSHIBA (2.5")'
#     page.hdd_2_western_digital_link.click()
#     page.wait_page_loaded(3)
#     page.hdd_2_western_digital_page_header.get_text() == 'Жёсткие диски (HDD) WESTERN DIGITAL (2.5")'


# HDD 3.5" page testing
# def test_hdd_3_page(web_browser):
#     page = MainPage(web_browser)
#     page.hdd_link.click()
#     page.hdd_3_link.click()
#     page.hdd_3_seagate_link.click()
#     page.wait_page_loaded(3)
#     assert page.hdd_3_seagate_page_header.get_text() == 'Жёсткие диски (HDD) SEAGATE (3.5")'
#     page.hdd_3_toshiba_link.click()
#     page.wait_page_loaded(3)
#     assert page.hdd_3_toshiba_page_header.get_text() == 'Жёсткие диски (HDD) TOSHIBA (3.5")'
#     page.hdd_3_western_digital_link.click()
#     page.wait_page_loaded(3)
#     page.hdd_3_western_digital_page_header.get_text() == 'Жёсткие диски (HDD) WESTERN DIGITAL (3.5")'

# motherboards page testing
# def test_motherboards_page(web_browser):
#     page = MainPage(web_browser)
#     page.motherboards_link.click()
#     page.mb_amd_am4_link.click()
#     page.wait_page_loaded(3)
#     assert page.mb_amd_am4_page_header.get_text() == 'Материнские платы AMD Socket AM4'
#     page.mb_amd_fm2_link.click()
#     page.wait_page_loaded(3)
#     assert page.mb_amd_fm2_page_header.get_text() == 'Материнские платы AMD Socket FM2+'
#     page.mb_amd_strx4_link.click()
#     page.wait_page_loaded(3)
#     assert page.mb_amd_strx4_page_header.get_text() == 'Материнские платы AMD Socket sTRX4'
#     page.mb_intel_1151_V2_link.click()
#     page.wait_page_loaded(3)
#     assert page.mb_intel_1151_V2_page_header.get_text() == 'Материнские платы Intel Socket 1151 v2'
#     page.mb_intel_1200_link.click()
#     page.wait_page_loaded(3)
#     assert page.mb_intel_1200_page_header.get_text() == 'Материнские платы Intel Socket 1200'
#     page.mb_intel_1700_link.click()
#     page.wait_page_loaded(3)
#     assert page.mb_intel_1700_page_header.get_text() == 'Материнские платы Intel Socket 1700'
#     page.mb_intel_2066_link.click()
#     page.wait_page_loaded(3)
#     assert page.mb_intel_2066_page_header.get_text() == 'Материнские платы Intel Socket 2066'
#     page.mb_intel_775_link.click()
#     page.wait_page_loaded(3)
#     assert page.mb_intel_775_page_header.get_text() == 'Материнские платы Intel Socket 775'
#     page.mb_cpu_link.click()
#     page.wait_page_loaded(3)
#     assert page.mb_cpu_page_header.get_text() == 'Материнские платы с установленным процессором'

# Intel 1151 V2 Socket Motherboards sorting by price
# def test_motherboard_sort_by_price(web_browser):
#     page = MainPage(web_browser)
#     page.motherboards_link.click()
#     page.intel_1151_V2_link.click()
#     page.price_sorting.click()
#     min_price = page.min_price.get_text().replace(' ', '')
#     second_price = page.other_price.get_text().replace(' ', '')
#     min_price_number = int(min_price)
#     second_price_number = int(second_price)
#     assert min_price_number == second_price_number

# desktop page testing
# def test_desktop_page(web_browser):
#     page = MainPage(web_browser)
#     page.desktops_link.click()
#     page.desktops_acer_link.click()
#     page.wait_page_loaded(3)
#     assert page.desktops_acer_page_header.get_text() == 'Настольные компьютеры (ПК) Acer'
#     page.desktops_asus_link.click()
#     page.wait_page_loaded(3)
#     assert page.desktops_asus_page_header.get_text() == 'Настольные компьютеры (ПК) ASUS'
#     page.desktops_dell_link.click()
#     page.wait_page_loaded(3)
#     assert page.desktops_dell_page_header.get_text() == 'Настольные компьютеры (ПК) DELL'
#     page.desktops_fujitsu_link.click()
#     page.wait_page_loaded(3)
#     assert page.desktops_fujitsu_page_header.get_text() == 'Настольные компьютеры (ПК) FUJITSU'
#     page.desktops_gigabyte_link.click()
#     page.wait_page_loaded(3)
#     assert page.desktops_gigabyte_page_header.get_text() == 'Настольные компьютеры (ПК) GIGABYTE'
#     page.desktops_hp_link.click()
#     page.wait_page_loaded(3)
#     assert page.desktops_hp_page_header.get_text() == 'Настольные компьютеры (ПК) HP'
#     page.desktops_huawei_link.click()
#     page.wait_page_loaded(3)
#     assert page.desktops_huawei_page_header.get_text() == 'Настольные компьютеры (ПК) HUAWEI'
#     page.desktops_lenovo_link.click()
#     page.wait_page_loaded(3)
#     assert page.desktops_lenovo_page_header.get_text() == 'Настольные компьютеры (ПК) LENOVO'
#     page.desktops_msi_link.click()
#     page.wait_page_loaded(3)
#     assert page.desktops_msi_page_header.get_text() == 'Настольные компьютеры (ПК) MSI'

# desktop acer page content and testing
# def test_desktop_acer_page_content(web_browser):
#     page = MainPage(web_browser)
#     page.desktops_link.click()
#     page.desktops_acer_link.click()
#     page.wait_page_loaded(3)
#     # desktop acer page content exist testing
#     count_titles = page.items_titles.count()
#     assert count_titles > 0
#     for i in range(count_titles):
#         # desktop acer page all titles exist testing
#         assert page.items_titles[i].text != ''
#
#     count_images = page.items_images.count()
#     # desktop acer page images exist testing
#     assert count_images > 0
#     for i in range(count_images):
#         # desktop acer page all images exist testing
#         assert page.items_images[i].get_attribute('src') != ''

# desktop acer page sorting by name testing
# def test_desktop_acer_page_sorting_by_name(web_browser):
#     page = MainPage(web_browser)
#     page.desktops_link.click()
#     page.desktops_acer_link.click()
#     page.sort_by_name.click()
#     page.wait_page_loaded(3)
#     # desktop acer page sorting by title testing
#     assert page.items_titles[0].text == 'Acer Veriton S2680G (DT.VV2ER.00B)' or page.items_titles[0].text == 'Acer Veriton X2670G (DT.VTFER.03F)'

# desktop acer page sorting by price testing
# def test_desktop_acer_page_sorting_by_price(web_browser):
#     page = MainPage(web_browser)
#     page.desktops_link.click()
#     page.desktops_acer_link.click()
#     page.sort_by_price.click()
#     page.sort_by_lst.click()
#     page.wait_page_loaded(3)
#     min_price = int(page.prices[0].text.replace(' ', ''))
#     second_price = int(page.prices[1].text.replace(' ', ''))
#     assert min_price <= second_price

# hits page content testing
# def test_hits_page(web_browser):
#     page = MainPage(web_browser)
#     count_titles = page.items_titles.count()
#     # hits page content exist testing
#     assert count_titles > 0
#     for i in range(count_titles):
#         # hits page all titles exist testing
#         assert page.items_titles[i].text != ''
#
#     count_images = page.items_images.count()
#     # hits page images exist testing
#     assert count_images > 0
#     for i in range(count_images):
#         # hits page all images exist testing
#         assert page.items_images[i].get_attribute('src') != ''

# top 40 selling items page testing
# def test_top_40_selling_items_page(web_browser):
#     page = MainPage(web_browser)
#     page.top_40_items_link.click()
#     page.wait_page_loaded(3)
#     # page header testing
#     assert page.top_40_items_page_header.get_text() == 'Хиты продаж'
#     count_titles = page.items_titles.count()
#     assert count_titles == 40
#     for i in range(count_titles):
#         #  all titles exist testing
#         assert page.items_titles[i].text != ''
#     # page images exist testing
#     count_images = page.items_images.count()
#     assert count_images == 40
#     for i in range(count_images):
#         # all images exist testing
#         assert page.items_images[i].get_attribute('src') != ''

# filters page testing
# def test_monitors_filters_page(web_browser):
#     page = MainPage(web_browser)
#     page.monitors_link.click()
#     page.all_monitors_link.click()
#     page.manufacturer_filter.click()
#     page.checkbox_aoc.click()
#     page.show_link.click()
#     count_titles = page.items_titles.count()
#     assert count_titles > 0
#     for i in range(count_titles):
#         # filter monitor AOC page all titles testing
#         assert 'AOC' in page.items_titles[i].text
#     page.diagonal_link.click()
#     page.min_field.send_keys('27')
#     page.max_field.send_keys('27')
#     page.show_link.click()
#     count_titles = page.items_titles.count()
#     for i in range(count_titles):
#         # filter monitor AOC page titles and diagonal testing
#         assert 'AOC' in page.items_titles[i].text and '27"' in page.items_titles[i].text
#     page.display_type_link.click()
#     page.checkbox_ips.click()
#     page.show_link.click()
#     count_description = page.items_descriptions.count()
#     for i in range(count_description):
#         # filter monitor AOC page display type testing
#         assert 'IPS' in page.items_descriptions[i].text
#     page.resolution_link.click()
#     page.checkbox_full_hd.click()
#     page.show_link.click()
#     page.display_type_close_tab_link.click()
#     page.resolution_close_tab_link.click()
#     count_description = page.items_descriptions.count()
#     for i in range(count_description):
#         # filter monitor AOC page display resolution testing
#         assert '1920x1080 (Full HD)' in page.items_descriptions[i].text
#     page.connectors_link.click()
#     page.checkbox_display_port.click()
#     page.show_link.click()
#     count_description = page.items_descriptions.count()
#     for i in range(count_description):
#         # filter monitor AOC page connectors type (DisplayPort) testing
#         assert 'DisplayPort' in page.items_descriptions[i].text

