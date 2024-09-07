import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser name: chrome or firefox"
    )
    parser.addoption(
        "--username", action="store", default="standard_user", help="Username for login"
    )
    parser.addoption(
        "--password", action="store", default="secret_sauce", help="Password for login"
    )

@pytest.fixture(scope='class')
def LoginSetup(request):   # Browser Code Setup
    browser_name = request.config.getoption("browser_name")
    User_name = request.config.getoption("username")         # Code From Pytest DOC related to Browser
    Password = request.config.getoption("password")

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    else:
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element(By.ID, "user-name").send_keys(User_name)
    driver.find_element(By.ID, "password").send_keys(Password)
    driver.find_element(By.ID, "login-button").click()
    request.cls.driver = driver  # Assigning Driver to the Class Object
    yield
    driver.quit()