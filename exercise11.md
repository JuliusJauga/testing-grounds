# Exercise 1
## Formal Test Case Definition and Environment Setup

### Task 1.1  E-Commerce Workflow
#### Test Case Attributes

| Field | Description |
|---|---|
| **Test Case ID** | TC_ECOM_001 |
| **Test Case Description** | Verify end-to-end E-Commerce workflow where high-price products from Featured Products (price > 900.00) and Jewelry category (price > 300.00) are added to the shopping cart, validated, and managed by updating item quantity to remove a product. |
| **Pre-Conditions** | User can access https://demowebshop.tricentis.com/ and a web browser is installed. |
| **Test Data** | Featured Products filter: price > 900.00; Jewelry category filter: price > 300.00; Cart quantity update value: 0 |
| **Expected Result** | Products matching the defined price filters are successfully added to the cart, success notifications appear, shopping cart counter updates correctly (1 -> 2 -> 3), and setting quantity to 0 removes the item from the cart. |
| **Post Condition** | Shopping cart reflects updated contents after item removal and remaining products stay visible in the cart. |
| **Project Name** | Demo Web Shop Automation |
| **Module Name** | Product Catalog / Shopping Cart |
| **Created By** | Julius Jauga |
| **Date of Creation** | 2026-02-11 |


---

#### Test Steps

| Step No. | Test Step | Expected Result |
|---|---|---|
| 1 | Open the Web Browser | Browser launches successfully |
| 2 | Navigate to "https://demowebshop.tricentis.com/" | Home page opens and page title is correct |
| 3 | Wait for the site to load | All main elements are visible and page is fully loaded |
| 4 | Navigate to the "Computers" category | Computers category page opens |
| 5 | Navigate to the "Desktops" subcategory | Desktop products page opens |
| 6 | Locate the first product with price greater than 900.00 | Product is found and price value is greater than 900.00 |
| 7 | Click "Add to cart" under the item | Success notification appears and cart counter updates to (1) |
| 8 | Locate the next product with price greater than 900.00 | Second matching product is found with correct price |
| 9 | Click "Add to cart" under the second item | Success notification appears and cart counter updates to (2) |
| 10 | Navigate to the "Jewelry" page | Jewelry category page opens successfully |
| 11 | Locate the first product with price greater than 300.00 | Product is found and price value is greater than 300.00 |
| 12 | Click "Add to cart" under the jewelry item | Success notification appears and cart counter updates to (3) |
| 13 | Navigate to the "Shopping cart" page | Shopping cart page opens successfully |
| 14 | Observe items listed in the shopping cart | All three added products are visible in the cart |
| 15 | Check product names and prices in the cart | Product names and prices match selected items |
| 16 | Validate cart subtotal calculation | Displayed subtotal equals sum of item prices (arithmetic verification) |
| 17 | Change quantity of first item to "0" | Quantity field accepts value change |
| 18 | Press Enter to update cart | Cart refreshes and item is removed |
| 19 | Observe shopping cart counter | Cart counter decreases accordingly |
| 20 | Verify final cart state | Cart shows correct remaining items and updated total |


### Task 1.2  Choosing test automation tool and setting up the environment.

Python Selenium

- selenium
- webdriver-manager
- pytest
---

#### Setting up

```
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

#### Test example to open application home page
```
pytest
```

## Test Steps

| Step No. | Test Step | Expected Result |
|----------|-----------|----------------|
| 1 | Open Google Chrome browser. | Browser opens successfully. |
| 2 | Enter the URL `https://demoqa.com/progress-bar` in the address bar and press Enter. | Progress Bar page loads and is visible. |
| 3 | Locate the Start button on the page. | Start button is displayed and clickable. |
| 4 | Locate the progress bar element on the page. | Progress bar is visible and shows 0% progress. |
| 5 | Inspect the progress bar and verify its CSS class contains the blue indicator class (`bg-info`). | Blue color class is present. |
| 6 | Click the Start button to begin the progress. | Progress percentage starts increasing automatically. |
| 7 | Wait until the progress bar reaches 100%. | Progress value reaches 100% and stops increasing. |
| 8 | Verify that the progress bar CSS class changes to the green indicator class (`bg-success`). | Progress bar color changes to green. |
| 9 | Locate and click the Reset button. | Progress bar resets to 0%. |
| 10 | Verify that the progress bar displays 0%. | Progress value is reset to 0%. |
| 11 | Verify that the progress bar CSS class reverts to the blue indicator class (`bg-info`). | Progress bar color returns to blue. |
