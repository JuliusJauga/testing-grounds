import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from helpers import *

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


def test_progress_bar_color_change(driver):
    driver.get("https://demoqa.com/progress-bar")

    until(driver, EC.presence_of_element_located((By.ID, "startStopButton")))

    start_button = driver.find_element(By.ID, "startStopButton")
    progress_bar = driver.find_element(By.CSS_SELECTOR, ".progress-bar")

    # Initial color validation (should be blue - bg-info)
    initial_class = progress_bar.get_attribute("class")
    assert "bg-info" in initial_class

    # Start progress
    start_button.click()

    # Wait until 100%
    until(driver, lambda d: progress_bar.get_attribute("aria-valuenow") == "100" and "bg-success" in progress_bar.get_attribute("class"))

    # Validate value is 100
    final_value = progress_bar.get_attribute("aria-valuenow")
    assert final_value == "100"

    # Validate color changed to green (bg-success)
    final_class = progress_bar.get_attribute("class")
    assert "bg-success" in final_class

    # Click Reset
    reset_button = driver.find_element(By.ID, "resetButton")
    reset_button.click()

    # Validate reset value
    reset_value = progress_bar.get_attribute("aria-valuenow")
    assert reset_value == "0"

    # Validate color reverted (back to blue)
    reset_class = progress_bar.get_attribute("class")
    assert "bg-info" in reset_class