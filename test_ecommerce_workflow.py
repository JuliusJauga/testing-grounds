import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from helpers import *

test_data = load_test_data_json("test_data.json")

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

@pytest.fixture
def authenticated_user(driver, request):
    data = request.param

    # Login
    driver.get(f"{BASE_URL}/login")
    driver.find_element(By.ID, "Email").send_keys(data["username"])
    driver.find_element(By.ID, "Password").send_keys(data["password"])
    driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

    until(driver, lambda d: "Log out" in d.page_source)

    # Ensure cart empty before test
    empty_cart(driver)

    yield data

    # Postconditions
    empty_cart(driver)

    logout_btns = driver.find_elements(By.LINK_TEXT, "Log out")
    if logout_btns:
        logout_btns[0].click()

def add_create_your_own_jewelry(driver, qty=1, length=25):
    # Leaving default options for now
    driver.get("https://demowebshop.tricentis.com/create-it-yourself-jewelry")

    until(driver, EC.presence_of_element_located((By.ID, "product_attribute_71_10_16")))

    start_qty = get_cart_qty(driver)

    length_input = driver.find_element(By.ID, "product_attribute_71_10_16")
    length_input.clear()
    length_input.send_keys(str(length))

    name = driver.find_element(By.CSS_SELECTOR, ".product-name h1").text.strip()

    price_text = driver.find_element(By.CSS_SELECTOR, ".prices .price-value-71").text
    price = parse_price(price_text)

    for _ in range(qty):
        before = get_cart_qty(driver)
        driver.find_element(By.ID, "add-to-cart-button-71").click()
        wait_for_cart_qty(driver, before + 1)

    assert get_cart_qty(driver) == start_qty + qty

    return name, price

def add_build_your_own_computer(driver, qty=1):
    # Leaving default options for now
    driver.get("https://demowebshop.tricentis.com/build-your-own-computer")
    start_qty = get_cart_qty(driver)

    first_hdd = driver.find_element(By.ID, "product_attribute_16_3_6_18")
    if not first_hdd.is_selected():
        first_hdd.click()

    for _ in range(qty):
        before = get_cart_qty(driver)
        driver.find_element(By.ID, "add-to-cart-button-16").click()
        wait_for_cart_qty(driver, before + 1)

    name = driver.find_element(By.CSS_SELECTOR, ".product-name h1").text.strip()

    price_text = driver.find_element(By.CSS_SELECTOR, ".prices .price-value-16").text
    price = parse_price(price_text)

    assert get_cart_qty(driver) == start_qty + qty

    return name, price

def is_build_computer_page(driver):
    return driver.current_url == "https://demowebshop.tricentis.com/build-your-own-computer"

def is_create_jewelry_page(driver):
    return driver.current_url == "https://demowebshop.tricentis.com/create-it-yourself-jewelry"

def add_custom_product(driver, qty=1, product_props=None):
    url = driver.current_url
    if url.endswith("/create-it-yourself-jewelry"):
        return add_create_your_own_jewelry(driver, qty, **(product_props or {}))
    elif url.endswith("/build-your-own-computer"):
        return add_build_your_own_computer(driver, qty, **(product_props or {}))

def add_product(driver, min_price=0, qty=1, timeout=10, product_props=None):
    xpath = (
        f"(//div[contains(@class,'product-item')]"
        f"[.//div[contains(@class,'add-info')]//span[contains(@class,'price')][number(text()) >= {min_price}]]"
        f"[.//div[contains(@class,'add-info')]//input[@type='button']])[1]"
    )

    try:
        product = driver.find_element(By.XPATH, xpath)
    except:
        raise Exception(f"No product found with price >= {min_price} and available to add to cart")

  
    details = product.find_element(By.CLASS_NAME, "details")
    add_info = details.find_element(By.CLASS_NAME, "add-info")

    price_text = add_info.find_element(By.CLASS_NAME, "prices").text
    price = parse_price(price_text)

    before = get_cart_qty(driver)
    before_url = driver.current_url

    # Try to click the button (might reroute)
    button = add_info.find_element(By.CLASS_NAME, "button-2")
    button.click()

    until(driver, lambda d: get_cart_qty(d) > before or d.current_url != before_url, timeout=timeout, message="Page did not change after clicking add to cart")

    url = driver.current_url
    # Now check where we ended up
    if url != before_url:
        return add_custom_product(driver, qty, product_props)
    else:
        # normal product: we already clicked the button, just wait for cart
        for _ in range(qty - 1):
            before = get_cart_qty(driver)
            button.click()
            wait_for_cart_qty(driver, before + 1)
        name = details.find_element(By.TAG_NAME, "a").text
        return name, price

@pytest.mark.parametrize("authenticated_user", test_data, indirect=True)
def test_ecommerce_workflow(driver, authenticated_user):
    data = authenticated_user
    selected_products = []

    # Add computer
    name, price = add_build_your_own_computer(
        driver,
        qty=data["computer"]["qty"]
    )
    selected_products.append((name, price))

    # Add jewelry
    name, price = add_create_your_own_jewelry(
        driver,
        qty=data["jewelry"]["qty"]
    )
    selected_products.append((name, price))

    # Open cart
    driver.find_element(By.CSS_SELECTOR, ".ico-cart").click()

    # Verify total items
    total_items = get_cart_qty(driver)
    assert total_items == 3

    # Verify product names present
    page_text = driver.page_source
    for name, _ in selected_products:
        assert name in page_text

    # Verify subtotal calculation
    unit_prices = driver.find_elements(By.CLASS_NAME, "product-unit-price")
    total_calc = sum(parse_price(p.text) for p in unit_prices)

    subtotal = parse_price(
        driver.find_element(By.CLASS_NAME, "product-subtotal").text
    )

    assert round(subtotal, 2) >= round(total_calc, 2)

    # Remove first item
    qty_input = driver.find_element(By.CLASS_NAME, "qty-input")
    qty_input.clear()
    qty_input.send_keys("0")

    driver.find_element(By.NAME, "updatecart").click()

    until(driver, lambda d: get_cart_qty(d) == 1)

    # Final verification
    rows = driver.find_elements(By.CSS_SELECTOR, ".cart-item-row")
    assert len(rows) == 1