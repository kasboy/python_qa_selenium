import pytest
from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera", "edge"], help="Browser")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    driver = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless: options.headless = True
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless: options.headless = True
        driver = webdriver.Firefox(options=options)

    elif browser == "opera":
        options = OperaOptions()
        if headless: options.headless = True
        driver = webdriver.Opera(options=options)

    elif browser == "edge":
        driver = webdriver.Edge("C:\\Users\\Mikhail\\Downloads\\driver\\msedgedriver.exe")

    if maximized:
        driver.maximize_window()

    return driver
