from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_open_homepage():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://demowebshop.tricentis.com/")
        assert "Demo Web Shop" in driver.title
    finally:
        driver.quit()