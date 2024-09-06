import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Utilities.BaseClass import Baseclass


class TestBuyDress(Baseclass):
    def test_buy_dress(self):
        AllPrices = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")
        for price in AllPrices:
            price_text = price.text.replace('$', '')
            if float(price_text) >= 25:
                print(f"Price: {price.text}")
                Button = price.find_element(By.XPATH, "following-sibling::button")
                Button.click()

        Cart = self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        Cart.click()
        Continue_ShoppingCart = self.driver.find_element(By.XPATH, "//button[@id='continue-shopping']")
        Continue_ShoppingCart.click()

        AllPrices = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")
        for price in AllPrices:
            price_text = price.text.replace('$', '')
            if float(price_text) >= 40:
                Remove = self.driver.find_element(By.XPATH, "//div[@class='pricebar']//button[text()='Remove']")
                Remove.click()

        Cart = self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        Cart.click()

        Price_In_Cart = self.driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[1]").text
        print(f"Total Price In Cart: {Price_In_Cart}")

        Checkout = self.driver.find_element(By.XPATH, "//button[@id='checkout']")
        Checkout.click()

        FirstName = self.driver.find_element(By.ID, "first-name")
        FirstName.send_keys("John")
        LastName = self.driver.find_element(By.ID, "last-name")
        LastName.send_keys("Doe")
        ZipCode = self.driver.find_element(By.ID, "postal-code")
        ZipCode.send_keys("60780")

        Button_ctn = self.driver.find_element(By.ID, "continue")
        Button_ctn.click()

        Sub_Total = self.driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
        Sub_Total_Price = Sub_Total.text.replace('Item total:', '')
        print(f"Sub Total: {Sub_Total_Price}")

        assert Price_In_Cart in Sub_Total_Price

        Finish = self.driver.find_element(By.XPATH, "//button[@id='finish']")
        Finish.click()

        Success_Message = self.driver.find_element(By.XPATH, "//h2[normalize-space()='Thank you for your order!']").text
        print(f"Success Message: {Success_Message}")

        assert "Thank you for your order!" in Success_Message

        Menu = self.driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
        Menu.click()

        Action = ActionChains(self.driver)
        Logout = self.driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
        Action.move_to_element(Logout).click().perform()


