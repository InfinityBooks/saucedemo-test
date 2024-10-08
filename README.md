# SauceDemo Automation Test Suite

## Overview

This project contains automated test cases for the SauceDemo website, created using **Python**, **Selenium**, and **Cucumber**. The tests cover key functionality such as user login, adding items to the cart, and completing the checkout process. In addition to the automated tests, manual test cases are documented below for ease of access.

## Technologies Used

- **Python**: Main language used to write the automation scripts.
- **Selenium**: WebDriver used to interact with the SauceDemo web application.
- **Cucumber**: Used to write tests in a behavior-driven format (Gherkin) and execute them with the help of Behave.

## Automated Test Coverage

### 1. **Login Functionality**
- Tests both valid and invalid login attempts.

### 2. **Adding Items to Cart**
- Verifies that items can be added to the cart and the total price is calculated correctly.

### 3. **Checkout Process**
- Tests the checkout process to ensure it completes successfully with a confirmation.

## How to Run the Tests

### Prerequisites
- Ensure that you have **Python** installed on your system.
- Install **pip** if it is not already installed.
- Clone the repository to your local machine.

### Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/InfinityBooks/saucedemo-test.git
   ```

2. **Navigate to the Project Directory**
   ```bash
   cd saucedemo-test
   ```

3. **Install Required Packages**
   Behave and Selenium

4. **Set up Environment Variables**
   You will need to set up the following environment variables:
   - `CHROMEDRIVER_PATH`: Path to your ChromeDriver executable.
   - `SAUCEDEMO_URL`: The URL for the SauceDemo website.

   On **Linux/macOS**:
   ```bash
   export CHROMEDRIVER_PATH='/path/to/chromedriver'
   export SAUCEDEMO_URL='https://www.saucedemo.com/'
   ```

   On **Windows**:
   ```bash
   set CHROMEDRIVER_PATH='C:\path\to\chromedriver.exe'
   set SAUCEDEMO_URL='https://www.saucedemo.com/'
   ```

### Running the Tests

1. **Run the Automated Tests Using Cucumber and Behave**
   To execute all the tests:
   ```bash
   behave
   ```

   This will run the test suite and display the results.

---

## Manual Test Cases

Below are the manual test cases that correspond to the automated tests, providing a clear framework for manual testing of key functionalities.

### Test Case 1: Login Functionality

**Objective**: Ensure that users can successfully log in with valid credentials and are blocked from logging in with invalid credentials.

**Steps**:
1. Navigate to the Sauce Demo website: https://www.saucedemo.com/
2. Enter a valid username (e.g., `standard_user`).
3. Enter the correct password (e.g., `secret_sauce`).
4. Click the Login button.
5. Verify that the user is redirected to the Inventory Page.
6. Attempt to log in with invalid credentials (e.g., incorrect username or password).
7. Verify that the system displays an error message and prevents the login attempt.

**Expected Results**:
- With valid credentials, the user is successfully logged in and directed to the inventory page.
- With invalid credentials, the user receives an error message and cannot log in.

**Reasoning**: Login functionality is critical for ensuring that only authorized users can access the application. Testing this ensures the correct handling of valid and invalid credentials, which is vital for both usability and security.

---

### Test Case 2: Adding Items to the Cart and Verifying Total

**Objective**: Ensure that users can add items to the cart and that the cart updates with the correct total price.

**Steps**:
1. Log in with valid credentials.
2. Add the first item (e.g., Sauce Labs Backpack) to the cart.
3. Add a second item (e.g., Sauce Labs Bike Light).
4. Click the Cart icon to view the cart.
5. Verify that both items are listed in the cart.
6. Confirm that the total price matches the sum of the individual items.
7. Remove one item and verify that the total updates correctly.

**Expected Results**:
- Items should be added to the cart successfully and displayed correctly.
- The total price should reflect the correct sum of the selected items.
- Removing an item should result in the total being recalculated accordingly.

**Reasoning**: Adding items to the cart is a core function of any eCommerce website. Testing this ensures that users can interact with the shopping cart, and that the pricing is accurate, which is crucial for the shopping experience.

---

### Test Case 3: Checkout Process and Order Confirmation

**Objective**: Verify that users can complete the checkout process and receive an order confirmation upon successful submission.

**Steps**:
1. Log in with valid credentials.
2. Add an item to the cart and proceed to the cart page.
3. Click the Checkout button.
4. Fill out the necessary fields (e.g., first name, last name, postal code) on the checkout form.
5. Click Continue, then click Finish to complete the order.
6. Verify that the user is redirected to an order confirmation page.
7. Confirm that the message "Thank you for your order!" is displayed.

**Expected Results**:
- The user should be able to fill out the checkout form and complete the purchase without issues.
- A confirmation page should display the message "Thank you for your order!" after successful checkout.

**Reasoning**: The checkout process is the most critical step in an eCommerce transaction. Any issues here would directly affect the ability to complete a purchase, which could impact both customer satisfaction and business revenue.
