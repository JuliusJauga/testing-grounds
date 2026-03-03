from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import logging
from random import uniform
import pytest

from helpers import *

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")

logger = logging.getLogger(__name__)

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def add_element_to_list(driver, first_name, last_name, email, age, salary, department):
    until(driver, EC.element_to_be_clickable((By.ID, "addNewRecordButton"))).click()
    
    until(driver, EC.visibility_of_element_located((By.ID, "firstName")))
    
    driver.find_element(By.ID, "firstName").send_keys(first_name)
    driver.find_element(By.ID, "lastName").send_keys(last_name)
    driver.find_element(By.ID, "userEmail").send_keys(email)
    driver.find_element(By.ID, "age").send_keys(str(age))
    driver.find_element(By.ID, "salary").send_keys(str(salary))
    driver.find_element(By.ID, "department").send_keys(department)
    
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    
    until(driver, EC.invisibility_of_element_located((By.ID, "firstName")))

def next_page(driver):
    xpath = "//div[@role='group']//button[normalize-space(text())='Next']"
    elem = until(driver, EC.presence_of_element_located((By.XPATH, xpath)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", elem)
    
    clickable = until(driver, EC.element_to_be_clickable((By.XPATH, xpath)))
    ActionChains(driver).move_to_element(clickable).perform()
    try:
        clickable.click()
    except Exception:
        logger.warning("Regular click failed, trying JavaScript click (Ads?)")
        driver.execute_script("arguments[0].click();", clickable)

def delete_first_element(driver):
    clickable = until(driver, EC.element_to_be_clickable((By.CSS_SELECTOR, "span[title='Delete']")))
    ActionChains(driver).move_to_element(clickable).perform()
    try:
        clickable.click()
    except Exception:
        logger.warning("Regular click failed, trying JavaScript click (Ads?)")
        driver.execute_script("arguments[0].click();", clickable)

def current_page(driver):
    return until(driver, EC.presence_of_element_located((By.XPATH, "//div[@class='col-auto' and contains(text(), 'Page')]")))

def test_demoqa(driver):
    driver.get("https://demoqa.com/")

    assert "demosite" in driver.title

    navigate(driver, "Elements", "Web Tables")
    
    for i in range(10):
        add_element_to_list(driver, f"First{i}", f"Last{i}", f"user{i}@example.com", int(uniform(18, 70)), int(uniform(10000, 100000)), "Example")

    assert "1 of 2" in current_page(driver).text
    
    next_page(driver)

    assert "2 of 2" in current_page(driver).text
    
    delete_first_element(driver)

    assert len(driver.find_elements(By.CSS_SELECTOR, "tbody tr")) == 10

    assert "1 of 1" in current_page(driver).text