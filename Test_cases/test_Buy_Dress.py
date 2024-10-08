import pytest
from selenium.webdriver import ActionChains
from POM.Homepage import HomePage
from TestData.Test_Data import TestDetailsPageData
from Utilities.BaseClass import Baseclass


class TestBuyDress(Baseclass):
    def test_buy_dress(self, TestDataGet):
        Log = self.Get_Logger()
        Home = HomePage(self.driver)   # Create an Object of the class along with driver argument
        AllPrices = Home.GetPrice()
        for price in AllPrices:
            price_text = price.text.replace('$', '')
            if float(price_text) >= 25:
                Log.info(f"Price Details of the Dress: {price.text}")
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
        Log.info(f"Total Price In Cart: {Price_In_Cart}")

        Detail_Page = Cart_page.CheckOutClick()


        FirstName = Detail_Page.FirstName()
        FirstName.send_keys(TestDataGet["FirstName"])
        LastName = Detail_Page.LastName()
        LastName.send_keys(TestDataGet["LastName"])
        ZipCode = Detail_Page.ZipCode()
        ZipCode.send_keys(TestDataGet["ZipCode"])

        Payment_Page = Detail_Page.ContinueButton()


        Sub_Total = Payment_Page.SubAmount()
        Sub_Total_Price = Sub_Total.text.replace('Item total:', '')
        Log.debug(f"Sub Total in the Payment Page: {Sub_Total_Price}")

        if Price_In_Cart not in Sub_Total_Price:
            Log.warning("Price in cart does not match the subtotal price.")  # Warning level
        else:
            Log.info("Price in cart matches the subtotal price.")

        Success_page = Payment_Page.Finish_Button()

        Success_Message = Success_page.Success_Message().text
        Log.info(f"Success Message: {Success_Message}")

        assert "Thank you for your order!" in Success_Message


        Menu = Success_page.Menu_Bar()
        Menu.click()

        Action = ActionChains(self.driver)
        Logout = Success_page.Logout_Link()
        Action.move_to_element(Logout).click().perform()


    @pytest.fixture(params=TestDetailsPageData.test_Details_Test_Data)
    def TestDataGet(self, request):
        return request.param


