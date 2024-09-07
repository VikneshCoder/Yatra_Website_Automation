from selenium.webdriver.common.by import By

from POM.CartPage import CartPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    Prices = (By.XPATH, "//div[@class='inventory_item_price']")  # This a Tuple
    def GetPrice(self):
        return self.driver.find_elements(*HomePage.Prices)  # This Star to tell pycharm it is tuple and make align along

    Button = (By.XPATH, "following-sibling::button")
    def ButtonClick(self, price):
        return price.find_element(By.XPATH, "following-sibling::button")

    Cart = (By.XPATH, "//a[@class='shopping_cart_link']")
    def CartClick(self):
        self.driver.find_element(*HomePage.Cart).click()
        Cart_page = CartPage(self.driver)
        return Cart_page

    Remove_Items = (By.XPATH, "//div[@class='pricebar']//button[text()='Remove']")
    def RemoveItems(self):
        return self.driver.find_element(*HomePage.Remove_Items)