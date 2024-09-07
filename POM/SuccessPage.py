from selenium.webdriver.common.by import By


class SuccessPage:
    def __init__(self, driver):
        self.driver = driver

    SuccessMessage = (By.XPATH, "//h2[normalize-space()='Thank you for your order!']")
    def Success_Message(self):
        return self.driver.find_element(*SuccessPage.SuccessMessage)

    Menu = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    def Menu_Bar(self):
        return self.driver.find_element(*SuccessPage.Menu)

    Logout = (By.XPATH, "//a[@id='logout_sidebar_link']")
    def Logout_Link(self):
        return self.driver.find_element(*SuccessPage.Logout)


