import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from POM.Homepage import HomePage
from Utilities.BaseClass import Baseclass


class TestBuyDress(Baseclass):
    def test_buy_dress(self):
        Home = HomePage(self.driver)   # Create an Object of the class along with driver argument
        AllPrices = Home.GetPrice()
        for price in AllPrices:
            price_text = price.text.replace('$', '')
            if float(price_text) >= 25:
                print(f"Price: {price.text}")
                Button = Home.ButtonClick(price)
                Button.click()

        Cart_page = Home.CartClick()
        Continue_ShoppingCart = Cart_page.ContinueShoppingCartClick()
        Continue_ShoppingCart.click()

        AllPrices = Home.GetPrice()
        for price in AllPrices:
            price_text = price.text.replace('$', '')
            if float(price_text) >= 40:
                Remove = Home.RemoveItems()
                Remove.click()

        Home.CartClick()

        Price_In_Cart = Cart_page.PriceInCartText().text
        print(f"Total Price In Cart: {Price_In_Cart}")

        Detail_Page = Cart_page.CheckOutClick()

        FirstName = Detail_Page.FirstName()
        FirstName.send_keys("John")
        LastName = Detail_Page.LastName()
        LastName.send_keys("Doe")
        ZipCode = Detail_Page.ZipCode()
        ZipCode.send_keys("60780")

        Payment_Page = Detail_Page.ContinueButton()


        Sub_Total = Payment_Page.SubAmount()
        Sub_Total_Price = Sub_Total.text.replace('Item total:', '')
        print(f"Sub Total: {Sub_Total_Price}")

        assert Price_In_Cart in Sub_Total_Price

        Success_page = Payment_Page.Finish_Button()

        Success_Message = Success_page.Success_Message().text
        print(f"Success Message: {Success_Message}")

        assert "Thank you for your order!" in Success_Message

        Menu = Success_page.Menu_Bar()
        Menu.click()

        Action = ActionChains(self.driver)
        Logout = Success_page.Logout_Link()
        Action.move_to_element(Logout).click().perform()


