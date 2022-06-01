from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class MainPage(WebPage):

    def __init__(self, driver):
        url = "https://www.regard.ru/"
        super().__init__(driver, url)

    # main page
    login_button = WebElement(xpath='//span[@class="login"]')
    field_email = WebElement(xpath='//input[@name="private_login"]')
    field_password = WebElement(xpath='//input[@name="private_password"]')
    enter_btn = WebElement(xpath='//button[@id="persona_loginButton"]')
    login_user_name = WebElement(xpath="//span[@class='login']")
    logout_button = WebElement(xpath="//a[@id='persona_logoutButton']")

    # about page
    about_page = WebElement(xpath="//a[@name='about']")
    main_info_link = WebElement(xpath="//a[contains(text(),'Общая информация')]")
    main_info_page_header = WebElement(xpath="//h1[contains(text(),'Общая информация')]")
    awards_link = WebElement(xpath="//a[contains(text(),'Наши награды')]")
    awards_page_header = WebElement(xpath="//h1[contains(text(),'Наши награды')]")

    # hits main page
    items_titles = ManyWebElements(xpath="//div[@class='bcontent']/div[@class='aheader']/a")
    items_images = ManyWebElements(xpath="//div[@class='bcontent']/div[@class='block_img']/a/img")
    items_descriptions = ManyWebElements(xpath="//div[@class='bcontent']/div[@class='aheader']/div")
    # pc configuration page
    pc_configuration_page_link = WebElement(xpath='//a[contains(text(),"Конфигуратор ПК")]')
    pc_configuration_page_header = WebElement(xpath='//h1[contains(text(),"Конфигуратор ПК")]')

    # paid page
    paid_page_link = WebElement(xpath='//a[contains(text(),"Оплата")]')
    paid_page_header = WebElement(xpath='//h1[contains(text(),"Оплата")]')

    # delivery page
    delivery_page_link = WebElement(xpath='//a[contains(text(),"Доставка")]')
    delivery_page_header = WebElement(xpath='//h1[contains(text(),"Доставка")]')

    # pickup page
    pickup_page_link = WebElement(xpath='//a[contains(text(),"Самовывоз")]')
    pickup_page_header = WebElement(xpath='//h1[contains(text(),"Самовывоз / Пункты выдачи заказов")]')

    # warranty page
    warranty_page_link = WebElement(xpath='//a[contains(text(),"Гарантия")]')
    warranty_page_header = WebElement(xpath='//h1[contains(text(),"Гарантия и возврат товара")]')

    # contacts page
    content_page_link = WebElement(xpath='//a[contains(text(),"Контакты")]')
    content_page_header = WebElement(xpath='//h1[contains(text(),"Контакты")]')

    # catalog by brends
    catalog_by_brends = WebElement(xpath='//span[@class="tab second "]')
    first_brend = WebElement(xpath='//ul[@class="menu"]//a[contains(text(),"1MORE")]')

    # catalog by types
    catalog_by_types = WebElement(xpath='//span[@class="tab first"]')
    first_type = WebElement(xpath='//li[@class="container   "]//a[contains(text(),"Блоки питания")]')

    # all chargers page
    charges_link = WebElement(xpath='//a[contains(text(),"Блоки питания")]')
    all_chargers_link = WebElement(xpath='//li[contains(@class,"open")]//ul//li//a[contains(@class,"red")][contains('
                                         'text(),"Все товары раздела")]')
    page_chargers_header = WebElement(xpath='//h1[contains(text(),"Блоки питания")]')

    # selling page
    selling_link = WebElement(xpath='//a[contains(text(),"Распродажа")]')
    selling_page_header = WebElement(xpath='//h1[contains(text(),"Распродажа (новые товары по сниженным ценам)")]')

    # dell laptop next page
    laptop_link = WebElement(xpath="//a[contains(text(),'Ноутбуки')]")
    dell_laptop_link = WebElement(xpath="//div[@id='lmenu']/ul[@class='menu ']/li[16]/ul[1]/li[5]/a[1]")
    pagination_links = ManyWebElements(xpath="//div[@class='pagination']/a")

    # appliance page
    appliance_link = WebElement(xpath='//a[contains(text(),"Бытовая техника")]')
    # climates_stuff
    climates_stuff_link = WebElement(xpath='//a[contains(text(),"Климатическая техника")]')
    fan_staff_link = WebElement(xpath='//li[contains(@class,"open")]//a[contains(text(),"Вентиляторы")]')
    fan_page_header = WebElement(xpath='//h1[contains(text(),"Вентиляторы")]')
    up_button_link = WebElement(xpath="//a[@class='right underline']")
    waterheater_stuff_link = WebElement(xpath='//a[contains(text(),"Водонагреватели")]')
    waterheater_page_header = WebElement(xpath='//h1[contains(text(),"Водонагреватели")]')
    weatherstations_stuff_link = WebElement(xpath='//a[contains(text(),"Метеостанции")]')
    weatherstation_page_header = WebElement(xpath='//h1[contains(text(),"Метеостанции")]')
    mobile_conditions_stuff_link = WebElement(xpath='//a[contains(text(),"Мобильные кондиционеры")]')
    mobile_conditions_page_header = WebElement(xpath='//h1[contains(text(),"Мобильные кондиционеры")]')
    heaters_stuff_link = WebElement(xpath='//a[contains(text(),"Обогреватели, конвекторы, тепловентиляторы")]')
    heaters_page_header = WebElement(xpath='//h1[contains(text(),"Обогреватели, конвекторы, тепловентиляторы")]')
    # home_stuff
    home_stuff_link = WebElement(xpath='//a[contains(text(),"Техника для дома")]')
    overlocks_stuff_link = WebElement(xpath='//a[contains(text(),"Оверлоки")]')
    overlocks_page_header = WebElement(xpath='//h1[contains(text(),"Оверлоки")]')
    steam_cleaners_stuff_link = WebElement(xpath='//a[contains(text(),"Пароочистители, отпариватели")]')
    all_steam_cleaners_link = WebElement(xpath='//li[contains(@class,"open current")]//ul//li[contains(@class,'
                                               '"open current")]//ul//li[contains(@class,"open")]//ul//li//a['
                                               'contains(@class,"red")][contains(text(),"Все товары раздела")]')
    all_steam_cleaner_header = WebElement(xpath='//h1[contains(text(),"Пароочистители, отпариватели")]')
    # hoovers_stuff
    hoovers_stuff_link = WebElement(xpath='//a[contains(text(),"Пылесосы")]')
    all_hoovers_stuff_link = WebElement(xpath='//li[contains(@class,"open")]//ul//li[contains(@class,'
                                              '"open")]//ul//li[contains(@class,"open")]//ul//li//a[@class="red"]['
                                              'contains(text(),"Все товары раздела")]')
    all_hoovers_header = WebElement(xpath='//h1[contains(text(),"Пылесосы")]')
    # irons_stuff
    irons_stuff_link = WebElement(xpath='//a[contains(text(),"Утюги")]')
    irons_page_header = WebElement(xpath='//h1[contains(text(),"Утюги")]')
    # sewing_stuff
    sewing_stuff_link = WebElement(xpath='//a[contains(text(),"Швейные машины")]')
    sewing_page_header = WebElement(xpath='//h1[contains(text(),"Швейные машины")]')

    # GPUs page
    gpus_link = WebElement(xpath='//a[contains(text(),"Видеокарты")]')
    amd_radeon_link = WebElement(xpath='//a[normalize-space()="AMD Radeon"]')
    amd_radeon_header = WebElement(xpath='//h1[contains(text(),"Видеокарты AMD Radeon")]')
    amd_radeon_pro_link = WebElement(xpath='//a[normalize-space()="AMD Radeon Pro"]')
    amd_radeon_pro_header = WebElement(xpath='//h1[contains(text(),"Видеокарты AMD Radeon Pro")]')
    nvidia_geforce_link = WebElement(xpath='//a[normalize-space()="NVIDIA GeForce"]')
    nvidia_geforce_header = WebElement(xpath='//h1[contains(text(),"Видеокарты NVIDIA GeForce")]')
    nvidia_quadro_link = WebElement(xpath='//a[normalize-space()="NVIDIA Quadro"]')
    nvidia_quadro_header = WebElement(xpath='//h1[contains(text(),"Видеокарты NVIDIA Quadro")]')

    # AMD gpus sorting by name
    amd_name_sorting = WebElement(xpath='//a[contains(text(),"названию")]')
    first_amd_gpu = WebElement(xpath='//a[contains(text(),"AMD Radeon RX 6500 XT ASUS 4Gb (TUF-RX6500XT-O4G-G")]')

    # HDD page
    hdd_link = WebElement(xpath='//a[contains(text(),"Жесткие диски (HDD)")]')
    hdd_2_link = WebElement(xpath="//a[normalize-space()='2.5\"']")
    hdd_2_seagate_link = WebElement(xpath='//li[contains(@class,"open")]//li[contains(@class,"open")]//a[contains('
                                          'text(),"SEAGATE")]')
    hdd_2_seagate_page_header = WebElement(xpath="//h1[contains(text(),'Жёсткие диски (HDD) SEAGATE (2.5\")')]")
    hdd_2_toshiba_link = WebElement(xpath="//li[contains(@class,'open current')]//li[contains(@class,'open "
                                          "current')]//a[contains(text(),'TOSHIBA')]")
    hdd_2_toshiba_page_header = WebElement(xpath="//h1[contains(text(),'Жёсткие диски (HDD) TOSHIBA (2.5\")')]")
    hdd_2_western_digital_link = WebElement(xpath="//li[contains(@class,'open current')]//li[contains(@class,'open "
                                                  "current')]//a[contains(text(),'WESTERN DIGITAL')]")
    hdd_2_western_digital_page_header = WebElement(xpath="//h1[contains(text(),'Жёсткие диски (HDD) WESTERN DIGITAL ("
                                                         "2.5\")')]")
    hdd_3_link = WebElement(xpath="//a[normalize-space()='3.5\"']")
    hdd_3_seagate_link = WebElement(xpath='//li[contains(@class,"open")]//li[contains(@class,"open")]//a[contains('
                                          'text(),"SEAGATE")]')
    hdd_3_seagate_page_header = WebElement(xpath="//h1[contains(text(),'Жёсткие диски (HDD) SEAGATE (3.5\")')]")
    hdd_3_toshiba_link = WebElement(xpath="//li[contains(@class,'container noborder open current')]//a[contains(text("
                                          "),'TOSHIBA')]")
    hdd_3_toshiba_page_header = WebElement(xpath="//h1[contains(text(),'Жёсткие диски (HDD) TOSHIBA (3.5\")')]")
    hdd_3_western_digital_link = WebElement(xpath="//li[contains(@class,'open')]//li[contains(@class,'open')]//a["
                                                  "contains(text(),'WESTERN DIGITAL')]")
    hdd_3_western_digital_page_header = WebElement(xpath="//h1[contains(text(),'Жёсткие диски (HDD) WESTERN DIGITAL ("
                                                         "3.5\")')]")

    # motherboards page
    motherboards_link = WebElement(xpath='//li[@class="container   "]//a[contains(text(),"Материнские платы")]')
    # amd socket am4 page
    mb_amd_am4_link = WebElement(xpath="//li[contains(@class,'open')]//a[contains(text(),'AMD Socket AM4')]")
    mb_amd_am4_page_header = WebElement(xpath='//h1[contains(text(),"Материнские платы AMD Socket AM4")]')
    mb_amd_fm2_link = WebElement(xpath="//li[contains(@class,'open')]//a[contains(text(),'AMD Socket FM2+')]")
    mb_amd_fm2_page_header = WebElement(xpath="//h1[contains(text(),'Материнские платы AMD Socket FM2+')]")
    mb_amd_strx4_link = WebElement(
        xpath="//li[contains(@class,'open current')]//a[contains(text(),'AMD Socket sTRX4')]")
    mb_amd_strx4_page_header = WebElement(xpath="//h1[contains(text(),'Материнские платы AMD Socket sTRX4')]")
    mb_intel_1151_V2_link = WebElement(
        xpath="//li[contains(@class,'open')]//a[contains(text(),'Intel Socket 1151 v2')]")
    mb_intel_1151_V2_page_header = WebElement(xpath="//h1[contains(text(),'Материнские платы Intel Socket 1151 v2')]")
    mb_intel_1200_link = WebElement(xpath='//li[contains(@class,"open")]//a[contains(text(),"Intel Socket 1200")]')
    mb_intel_1200_page_header = WebElement(xpath="//h1[contains(text(),'Материнские платы Intel Socket 1200')]")
    mb_intel_1700_link = WebElement(xpath="//li[contains(@class,'open')]//a[contains(text(),'Intel Socket 1700')]")
    mb_intel_1700_page_header = WebElement(xpath="//h1[contains(text(),'Материнские платы Intel Socket 1700')]")
    mb_intel_2066_link = WebElement(xpath="//li[contains(@class,'open')]//a[contains(text(),'Intel Socket 2066')]")
    mb_intel_2066_page_header = WebElement(xpath="//h1[contains(text(),'Материнские платы Intel Socket 2066')]")
    mb_intel_775_link = WebElement(xpath="//li[contains(@class,'open')]//a[contains(text(),'Intel Socket 775')]")
    mb_intel_775_page_header = WebElement(xpath="//h1[contains(text(),'Материнские платы Intel Socket 775')]")
    mb_cpu_link = WebElement(xpath="//li[contains(@class,'open')]//a[contains(text(),'Мат. плата + процессор')]")
    mb_cpu_page_header = WebElement(xpath="//h1[contains(text(),'Материнские платы с установленным процессором')]")

    # Desktops page
    desktops_link = WebElement(xpath="//a[contains(text(),'Настольные компьютеры')]")
    desktops_acer_link = WebElement(xpath="//li[contains(@class,'open')]//a[contains(text(),'ACER')]")
    desktops_acer_page_header = WebElement(xpath="//h1[contains(text(),'Настольные компьютеры (ПК) Acer')]")
    desktops_asus_link = WebElement(xpath="//li[contains(@class,'open')]//a[contains(text(),'ASUS')]")
    desktops_asus_page_header = WebElement(xpath="//h1[contains(text(),'Настольные компьютеры (ПК) ASUS')]")
    desktops_dell_link = WebElement(xpath="//li[contains(@class,'open')]//a[contains(text(),'DELL')]")
    desktops_dell_page_header = WebElement(xpath="//h1[contains(text(),'Настольные компьютеры (ПК) DELL')]")
    desktops_fujitsu_link = WebElement(xpath="//li[contains(@class,'open')]//a[contains(text(),'FUJITSU')]")
    desktops_fujitsu_page_header = WebElement(xpath="//h1[contains(text(),'Настольные компьютеры (ПК) FUJITSU')]")
    desktops_gigabyte_link = WebElement(xpath="//li[contains(@class,'open')]//a[contains(text(),'GIGABYTE')]")
    desktops_gigabyte_page_header = WebElement(xpath="//h1[contains(text(),'Настольные компьютеры (ПК) GIGABYTE')]")
    desktops_hp_link = WebElement(xpath="//li[contains(@class,'open')]//a[contains(text(),'HP')]")
    desktops_hp_page_header = WebElement(xpath="//h1[contains(text(),'Настольные компьютеры (ПК) HP')]")
    desktops_huawei_link = WebElement(xpath="//li[contains(@class,'open')]//a[contains(text(),'HUAWEI')]")
    desktops_huawei_page_header = WebElement(xpath="//h1[contains(text(),'Настольные компьютеры (ПК) HUAWEI')]")
    desktops_lenovo_link = WebElement(xpath="//li[contains(@class,'open')]//a[contains(text(),'LENOVO')]")
    desktops_lenovo_page_header = WebElement(xpath="//h1[contains(text(),'Настольные компьютеры (ПК) LENOVO')]")
    desktops_msi_link = WebElement(xpath="//li[contains(@class,'open')]//a[contains(text(),'MSI')]")
    desktops_msi_page_header = WebElement(xpath="//h1[contains(text(),'Настольные компьютеры (ПК) MSI')]")

    # sorting
    sort_by_name = ManyWebElements(xpath="//div[@class='sort']/a")
    sort_by_price = WebElement(xpath="//a[contains(text(),'цене')]")
    sort_by_lst = WebElement(xpath="//a[@class='sortby' and contains(text(),'списком')]")
    prices = ManyWebElements(xpath="//div[@class='list-price']/span")

    # top 40 selling items
    top_40_items_link = WebElement(xpath="//a[@class='right' and contains(text(),'ТОП 40 продаж')]")
    top_40_items_page_header = WebElement(xpath="//h1[contains(text(),'Хиты продаж')]")

    # monitors page
    monitors_link = WebElement(xpath="//a[contains(text(),'Мониторы')]")
    all_monitors_link = WebElement(xpath="//li[contains(@class,'open')]//ul//li//a[contains(@class,'red')][contains("
                                         "text(),'Все товары раздела')]")

    # filters monitors
    manufacturer_filter = WebElement(xpath="//span[contains(text(),'Производитель')]")
    checkbox_aoc = WebElement(xpath="//input[@id='value-14600000']")
    show_link = WebElement(xpath="//a[contains(text(),'показать')]")
    diagonal_link = WebElement(xpath="//span[@id='bold-194']")
    min_field_diagonal_monitor = WebElement(xpath="//input[@id='filter_value_digital_min_194']")
    max_field_diagonal_monitor = WebElement(xpath="//input[@id='filter_value_digital_max_194']")
    display_type_link = WebElement(xpath="//span[contains(text(),'Тип матрицы')]")
    checkbox_ips = WebElement(xpath="//input[@id='value-832']")
    display_type_close_tab_link = WebElement(xpath="//span[@id='bold-195']")
    resolution_link = WebElement(xpath="//span[contains(text(),'Разрешение экрана')]")
    checkbox_full_hd = WebElement(xpath="//input[@id='value-751']")
    resolution_close_tab_link = WebElement(xpath="//span[@id='bold-196']")
    connectors_link = WebElement(xpath="//span[contains(text(),'Разъёмы')]")
    checkbox_display_port = WebElement(xpath="//input[@id='value-847']")

    # filters printers
    printers_link = WebElement(xpath="//a[contains(text(),'Принтеры и МФУ')]")
    all_printers_link = WebElement(xpath="//div[@id='lmenu']/ul[contains(@class,'menu')]/li[contains(@class,"
                                         "'open')]/ul/li[1]/a[1]")
    checkbox_hp_printers = WebElement(xpath="//input[@id='value-3500000']")
    printers_device_type_link = WebElement(xpath="//span[@id='bold-1924']")
    checkbox_hp_mfu = WebElement(xpath="//input[@id='value-5275']")
    printers_type_technology_link = WebElement(xpath="//span[@id='bold-1926']")
    checkbox_hp_mfu_laser = WebElement(xpath="//input[@id='value-5270']")
    price_filter = WebElement(xpath="//span[@id='bold-2']")
    min_field_price_hp_mfu_laser = WebElement(xpath="//input[@id='filter_value_digital_min_2']")
    max_field_price_hp_mfu_laser = WebElement(xpath="//input[@id='filter_value_digital_max_2']")
    make_filters = WebElement(xpath="//a[@id='b_apply_filter']")
