import configparser
from Utilities.read_config import read_configuration
import pytest
from selenium import webdriver

config = configparser.ConfigParser()
config.read('config.ini')


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def driver(request, browser):
    base_url = read_configuration('Default', 'BaseUrl')
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise print("enter valid browser should be chrome or firefox")

    driver.get(base_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

