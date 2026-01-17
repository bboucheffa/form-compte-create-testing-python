import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # mode headless
    chrome_options.add_argument("--no-sandbox")  # nécessaire pour CI Linux
    chrome_options.add_argument("--disable-dev-shm-usage")  # éviter les problèmes mémoire
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    #driver.maximize_window()
    yield driver
    driver.quit()