from selenium.webdriver.common.by import By

from POM.SuccessPage import SuccessPage


class PaymentPage:
    def __init__(self, driver):
        self.driver = driver

    Sub_Amount = (By.XPATH, "//div[@class='summary_subtotal_label']")
    def SubAmount(self):
        return self.driver.find_element(*PaymentPage.Sub_Amount)

    FinishButton = (By.XPATH, "//button[@id='finish']")
    def Finish_Button(self):
        self.driver.find_element(*PaymentPage.FinishButton).click()
        Success_page = SuccessPage(self.driver)
        return Success_page
