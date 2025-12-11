import pytest
import yaml
from utils.driver_manager import get_driver
from pages.login_page import LoginPage

#Load test data from YAML file
with open('config/config.yaml') as file:
    config = yaml.safe_load(file)

@pytest.fixture
def driver():
    driver = get_driver()
    driver.get(config["url"])
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open(config['url'])
    login_page.login(config['valid_user']['username'], config['valid_user']['password'])
    # Add assertions here to verify successful login
