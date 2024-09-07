from selenium.webdriver.common.by import By

from POM.PaymentPage import PaymentPage


class DetailsPage:
    def __init__(self, driver):
        self.driver = driver


    First_name = (By.ID, "first-name")
    def FirstName(self):
        return self.driver.find_element(*DetailsPage.First_name)

    Last_name = (By.ID, "last-name")
    def LastName(self):
        return self.driver.find_element(*DetailsPage.Last_name)

    Zip_code = (By.ID, "postal-code")
    def ZipCode(self):
        return self.driver.find_element(*DetailsPage.Zip_code)

    Continue_button = (By.ID, "continue")
    def ContinueButton(self):
        self.driver.find_element(*DetailsPage.Continue_button).click()
        Payment_Page = PaymentPage(self.driver)
        return Payment_Page