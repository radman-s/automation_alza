from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BaseElement(object):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def click(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    def input_text(self, text):
        self.web_element.send_keys(text)
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text

    def move_to(self):
        element = ActionChains(self.driver)
        element.move_to_element(self.web_element).perform()
        return None

    def format_price(self):
        price = self.web_element.text[:-2]
        return price.replace(' ', '')

    def format_name(self):
        name = self.web_element.text[16:]
        return name

