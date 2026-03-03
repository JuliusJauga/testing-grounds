# Exercise 3  
## Widgets and Dynamic DOM  

---

# Task 3.2 – Dynamic Properties  

**Application Under Test:** DemoQA  
**URL:** https://demoqa.com/dynamic-properties  

---

## Test Case Attributes  

| Field | Description |
|--------|------------|
| **Test Case ID** | TC_DEMOQA_003 |
| **Test Case Description** | Verify Dynamic Properties behavior including button enablement after delay, dynamic color change, and delayed visibility of a button after page refresh. |
| **Pre-Conditions** | User can access https://demoqa.com/dynamic-properties and a web browser is installed. |
| **Test Data** | Enable After button; Color Change button; Visible After button |
| **Expected Result** | "Enable After" button becomes enabled after ~5 seconds. "Color Change" button changes CSS class dynamically. "Visible After" button becomes visible after refresh and delay. |
| **Post Condition** | All dynamic elements reflect updated states after timeout and refresh. |
| **Project Name** | DemoQA Automation |
| **Module Name** | Elements – Dynamic Properties |
| **Test Type** | Functional UI Automation |
| **Execution Type** | Automated |
| **Browser** | Google Chrome |
| **Created By** | Julius Jauga |
| **Date of Creation** | 2026-02-23 |

---

## Test Steps

| Step No. | Test Step | Expected Result |
|----------|-----------|----------------|
| 1 | Open Google Chrome browser. | Browser launches successfully. |
| 2 | Navigate to `https://demoqa.com/dynamic-properties` and load the page. | Dynamic Properties page is displayed correctly. |
| 3 | Locate the "Enable After" button on the page. | Button is visible and initially disabled. |
| 4 | Wait for approximately 5 seconds and observe the "Enable After" button. | Button becomes enabled and clickable. |
| 5 | Confirm that the "Enable After" button can be clicked. | Button is active and responsive. |
| 6 | Refresh the page. | Page reloads successfully. |
| 7 | Locate the "Color Change" button and observe its appearance. | Button is visible with its initial visual style. |
| 8 | Wait for approximately 5 seconds and observe the "Color Change" button. | Button visually changes appearance. |
| 9 | Refresh the page again. | Page reloads successfully. |
| 10 | Wait for the "Visible After" button to appear. | The button becomes visible after a short delay. |
| 11 | Observe the "Visible After" button on the page. | Button is visible and available for interaction. |
---
