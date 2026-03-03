from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def until(driver, condition, timeout=10, message=""):
    try:
        return WebDriverWait(driver, timeout).until(condition)
    except:
        raise Exception(message)
    
def navigate(driver, *links):
    for link_text in links:
        until(driver, EC.element_to_be_clickable((By.LINK_TEXT, link_text))).click()

def wait_for_cart_qty(driver, expected, timeout=10):
    until(driver, lambda d: get_cart_qty(d) == expected, timeout, f"Expected cart quantity to be {expected}")

def get_cart_qty(driver):
    text = driver.find_element(By.CSS_SELECTOR, ".cart-qty").text
    return int(text.strip("()"))

def parse_price(text):
    return float(text.replace("$", "").replace(",", ""))

def get_total_cart_items(driver):
    cart_rows = driver.find_elements(By.CSS_SELECTOR, ".cart-item-row")
    total = 0
    for row in cart_rows:
        qty_input = row.find_element(By.CLASS_NAME, "qty-input")
        total += int(qty_input.get_attribute("value"))
    return total

def remove_first_product(driver):
    rows = driver.find_elements(By.CSS_SELECTOR, ".cart-item-row")
    if not rows:
        raise Exception("Cart is empty")

    first_row = rows[0]
    qty_input = first_row.find_element(By.CLASS_NAME, "qty-input")
    qty_before = int(qty_input.get_attribute("value"))

    total_before = get_total_cart_items(driver)

    qty_input.clear()
    qty_input.send_keys("0")

    driver.find_element(By.NAME, "updatecart").click()

    wait_for_cart_qty(driver, total_before - qty_before)
