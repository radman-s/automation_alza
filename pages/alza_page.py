from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator

class AlzaPage(BasePage):

    url = 'https://www.alza.cz/'

    @property
    def mobile_phones(self):
        locator = Locator(By.CSS_SELECTOR, 'a[title="Mobilní telefony"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def iphone11pro_link(self):
        locator = Locator(By.CSS_SELECTOR, 'a[href="/iphone-11-pro/18872151.htm"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def product1(self):
        locator = Locator(By.XPATH, '(//a[@class="name browsinglink impression-binded"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def price_product1(self):
        locator = Locator(By.XPATH, '(//span[@class="c2"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def product_name(self):
        locator = Locator(By.CSS_SELECTOR, 'h1[itemprop="name"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def product1_exc_vat(self):
        locator = Locator(By.CSS_SELECTOR, 'span[class="price_withoutVat"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def product_price(self):
        locator = Locator(By.CSS_SELECTOR, 'span[class="bigPrice price_withVat"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def checkbox_1(self):
        locator = Locator(By.CSS_SELECTOR, 'td[class="hookProductCheckBox"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def price_checkbox_1(self):
        locator = Locator(By.CSS_SELECTOR, 'span[class="hookProductPrice"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def checkbox_2(self):
        locator = Locator(By.XPATH, '(//td[@class="accessoryGroupCheckBox"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def price_checkbox_2(self):
        locator = Locator(By.XPATH, '(//span[@class="accessoryGroupPrice"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def checkbox_3(self):
        locator = Locator(By.XPATH, '(//td[@class="accessoryGroupCheckBox"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def price_checkbox_3(self):
        locator = Locator(By.XPATH, '(//span[@class="accessoryGroupPrice"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def checkbox_4(self):
        locator = Locator(By.XPATH, '(//td[@class="accessoryGroupCheckBox"])[3]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def price_checkbox_4(self):
        locator = Locator(By.XPATH, '(//span[@class="accessoryGroupPrice"])[3]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def glass_dialog(self):
        locator = Locator(By.CSS_SELECTOR, 'a[class="dialog-body__button"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def add_to_card(self):
        locator = Locator(By.CSS_SELECTOR, 'a[class="btnx normal green buy"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def product_name_checkout(self):
        locator = Locator(By.XPATH, '//div[@id="textc"]/a[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def proceed_checkout(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="varAToBasketButton"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def product_name_basket(self):
        locator = Locator(By.XPATH, '(//a[@class="mainItem"])')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def total_vat(self):
        locator = Locator(By.CSS_SELECTOR, 'span[id="price"]')
        return BaseElement(driver=self.driver, locator=locator)




