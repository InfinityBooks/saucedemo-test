import os
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the browser driver as a global variable
driver = None

def setup_driver():
    global driver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(os.getenv('CHROMEDRIVER_PATH'))
    driver = webdriver.Chrome(service=service, options=chrome_options)

def quit_driver():
    global driver
    if driver:
        driver.quit()

@given('I navigate to the SauceDemo website')
def navigate_to_website(context):
    setup_driver()
    context.driver = driver
    context.driver.get(os.getenv('SAUCEDEMO_URL'))

@then('I should see the correct landing page title')
def verify_landing_page_title(context):
    assert "Swag Labs" in context.driver.title, "Landing page title is incorrect!"
    print("Landing page title verified successfully.")

@when('I log in with valid credentials')
def login_successful(context):
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    context.driver.find_element(By.ID, "login-button").click()

@then('I should be on the inventory page')
def verify_inventory_page(context):
    assert "inventory.html" in context.driver.current_url, "Login failed!"
    print("Login successful and inventory page loaded.")

@when('I log in with invalid credentials')
def login_unsuccessful(context):
    invalid_usernames = ["invalid_user", "wrong_user", "test_user"]
    for username in invalid_usernames:
        context.driver.find_element(By.ID, "user-name").send_keys(username)
        context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        context.driver.find_element(By.ID, "login-button").click()
        error_message = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        )
        assert error_message.is_displayed(), f"Error message not displayed for username: {username}"
        print(f"Error message displayed for invalid username '{username}'.")

@then('I should see an error message')
def verify_error_message(context):
    print("Error message verified successfully.")

@when('I add two items to the cart')
def add_items_to_cart(context):
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

@when('I proceed to checkout')
def proceed_to_checkout(context):
    context.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    context.driver.find_element(By.ID, "checkout").click()
    context.driver.find_element(By.ID, "first-name").send_keys("John")
    context.driver.find_element(By.ID, "last-name").send_keys("Doe")
    context.driver.find_element(By.ID, "postal-code").send_keys("12345")
    context.driver.find_element(By.XPATH, "//input[@data-test='continue']").click()
    context.driver.find_element(By.XPATH, "//button[@data-test='finish']").click()

@then('I should see a confirmation message')
def verify_confirmation_message(context):
    confirmation_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[@data-test='thankyou']"))
    )
    assert confirmation_message.is_displayed(), "Checkout failed!"
    print("Checkout successful!")
    quit_driver()
