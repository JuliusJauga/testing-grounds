# Exercise 3  
## Widgets and Dynamic DOM

---

# Task 3.1 – Progress Bar Workflow  

**Application Under Test:** DemoQA  
**URL:** https://demoqa.com/progress-bar  

---

## Test Case Attributes  

| Field | Description |
|---|---|
| **Test Case ID** | TC_DEMOQA_002 |
| **Test Case Description** | Verify Progress Bar functionality: start progress, validate dynamic percentage increase, confirm color change at 100%, and validate reset functionality. |
| **Pre-Conditions** | User can access https://demoqa.com/progress-bar and a web browser is installed. |
| **Test Data** | Target completion value: 100%; Initial expected class: bg-info; Completion class: bg-success |
| **Expected Result** | Progress bar starts increasing after clicking Start, reaches 100%, changes color from blue (bg-info) to green (bg-success), and resets back to 0% with original color after clicking Reset. |
| **Post Condition** | Progress bar displays 0% and returns to initial visual state (blue color). |
| **Project Name** | DemoQA Automation |
| **Module Name** | Widgets – Progress Bar |
| **Test Type** | Functional UI Automation |
| **Execution Type** | Automated |
| **Browser** | Google Chrome |
| **Created By** | Julius Jauga |
| **Date of Creation** | 2026-02-23 |

---

## Test Steps

| Step No. | Test Step | Expected Result |
|----------|-----------|----------------|
| 1 | Open Google Chrome browser. | Browser opens successfully. |
| 2 | Navigate to `https://demoqa.com/progress-bar` and load the page. | Progress Bar page is displayed correctly. |
| 3 | Locate the Start button on the page. | Start button is visible and ready to click. |
| 4 | Locate the progress bar on the page. | Progress bar is visible and displays 0%. |
| 5 | Click the Start button to begin the progress. | Progress bar percentage starts increasing automatically. |
| 6 | Wait until the progress bar reaches 100%. | Progress bar stops at 100%. |
| 7 | Observe the progress bar after it reaches 100%. | Progress bar visually indicates completion. |
| 8 | Click the Reset button. | Progress bar resets to 0%. |
| 9 | Observe the progress bar after reset. | Progress bar returns to its initial state and shows 0%. |

---