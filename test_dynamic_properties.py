import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from helpers import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_dynamic_properties_buttons(driver):
    driver.get("https://demoqa.com/dynamic-properties")

    until(driver, EC.presence_of_element_located((By.ID, "enableAfter")))

    enable_button = driver.find_element(By.ID, "enableAfter")
    color_button = driver.find_element(By.ID, "colorChange")
    initial_color_button_class = color_button.get_attribute("class")

    # Initially button should be disabled
    assert not enable_button.is_enabled()

    # Wait until button becomes enabled (~5 seconds)
    until(driver, lambda d: d.find_element(By.ID, "enableAfter").is_enabled(), timeout=5)

    # Re-fetch element to avoid stale reference
    enable_button = driver.find_element(By.ID, "enableAfter")

    # Validate enabled state
    assert enable_button.is_enabled()

    # Refresh page
    driver.refresh()

    # Wait for class change
    until(driver, lambda d: d.find_element(By.ID, "colorChange").get_attribute("class") != initial_color_button_class, timeout=5)

    # Re-fetch element
    color_button = driver.find_element(By.ID, "colorChange")

    # Capture updated class
    updated_class = color_button.get_attribute("class")

    # Validate class changed
    assert initial_color_button_class != updated_class

    # Refresh page
    driver.refresh()

    # Wait for invisible button to appear
    until(driver, lambda d: d.find_element(By.ID, "visibleAfter").is_displayed(), timeout=5)

    assert driver.find_element(By.ID, "visibleAfter").is_displayed()