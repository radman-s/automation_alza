from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator

class AlzaPage(BasePage):

    url = 'https://www.alza.cz/'

    # buy procedure
    @property
    def mobile_phones(self):
        locator = Locator(By.CSS_SELECTOR, 'a[title="Mobilní telefony"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def iphone11pro_link(self):
        locator = Locator(By.CSS_SELECTOR, 'a[href="/iphone-11-pro/18872151.htm"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def iphone11pro_pic(self):
        locator = Locator(By.XPATH, '(//a[@href="/iphone-11-pro?dq=5669274"])[3]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def product_name1(self):
        locator = Locator(By.XPATH, '(//a[@class="name browsinglink impression-binded"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def product_price1(self):
        locator = Locator(By.XPATH, '(//span[@class="c2"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def product_price_nodph(self):
        locator = Locator(By.XPATH, '(//span[@class="c1"])[1]/b')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def product_name2(self):
        locator = Locator(By.CSS_SELECTOR, 'h1[itemprop="name"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def product_price2(self):
        locator = Locator(By.CSS_SELECTOR, 'span[class="bigPrice price_withVat"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def case_check(self):
        locator = Locator(By.CSS_SELECTOR, 'td[class="hookProductCheckBox"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def warranty_check(self):
        locator = Locator(By.XPATH, '(//td[@class="accessoryGroupCheckBox"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def insurance_check(self):
        locator = Locator(By.XPATH, '(//td[@class="accessoryGroupCheckBox"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def protect_glass(self):
        locator = Locator(By.XPATH, '(//td[@class="accessoryGroupCheckBox"])[3]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def case_price(self):
        locator = Locator(By.CSS_SELECTOR, 'span[class="hookProductPrice"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def warranty_price(self):
        locator = Locator(By.XPATH, '(//span[@class="accessoryGroupPrice"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def insurance_price(self):
        locator = Locator(By.XPATH, '(//span[@class="accessoryGroupPrice"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def protect_glass_price(self):
        locator = Locator(By.XPATH, '(//span[@class="accessoryGroupPrice"])[3]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def protect_glass_button(self):
        locator = Locator(By.CSS_SELECTOR, 'div[id="dialog-button-0"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def buy_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[class="btnx normal green buy"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def basked(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="varAToBasketButton"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def total_price(self):
        locator = Locator(By.XPATH, '(//td[@class="c2"])[7]')
        return BaseElement(driver=self.driver, locator=locator)
