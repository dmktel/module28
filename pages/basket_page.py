from pages.elements import WebElement, ManyWebElements
from pages.main_page import MainPage


class BasketPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)

    search_field = WebElement(xpath="//input[@id='query']")
    search_button = WebElement(xpath="//button[contains(text(),'Найти')]")
    add_to_basket_link = ManyWebElements(xpath="//div[@class='price']/span/a")
    items_titles = ManyWebElements(xpath="//div[@class='bcontent']/div[@class='aheader']/a")
    basket_link = WebElement(xpath="//div[@id='basket']/a")
    basket_page_header = WebElement(xpath="//h1[contains(text(),'Корзина')]")
    items_ids = ManyWebElements(xpath="//tr[@class='goods_line']/td[@class='t1']")
    prices_in_basket = ManyWebElements(xpath="//tr[@class='goods_line']/td[@class='t3']/span")
    sum_item_basket = ManyWebElements(xpath="//tr[@class='goods_line']/td[@class='t5']/span")
    all_sum_basket = WebElement(xpath="//span[@id='sum_itogo']")
    delete_button = ManyWebElements(xpath="//tr[@class='goods_line']/td[@class='t6']/a")
    empty_basket = WebElement(xpath="//h3[@class='alarm']")






