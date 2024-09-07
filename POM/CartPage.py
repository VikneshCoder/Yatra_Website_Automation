from selenium.webdriver.common.by import By

from POM.DetailsPage import DetailsPage


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    Continue_ShoppingCart = (By.XPATH, "//button[@id='continue-shopping']")
    def ContinueShoppingCartClick(self):
        return self.driver.find_element(*CartPage.Continue_ShoppingCart)

    Price_In_Cart = (By.XPATH, "(//div[@class='inventory_item_price'])[1]")
    def PriceInCartText(self):
        return self.driver.find_element(*CartPage.Price_In_Cart)

    CheckOut = (By.XPATH, "//button[@id='checkout']")
    def CheckOutClick(self):
        self.driver.find_element(*CartPage.CheckOut).click()
        Detail_Page = DetailsPage(self.driver)
        return Detail_Page