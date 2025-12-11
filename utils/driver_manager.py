from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    options = webdriver.ChromeOptions()
    # Remove headless for now
    # options.add_argument("--headless")

    #service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver
