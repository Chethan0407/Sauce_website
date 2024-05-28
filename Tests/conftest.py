from Utilities.read_config import read_configuration



import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def driver(request):
    base_url = read_configuration('Default', 'BaseUrl')
    driver = webdriver.Chrome()  # or whichever driver you're using
    driver.get(base_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


