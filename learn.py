from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open Zepto login page (update the URL if necessary)
driver.get('https://www.zepto.com')

# Wait until the phone number input is visible (adjust this locator according to actual element)
wait = WebDriverWait(driver, 10)
phone_number_input = wait.until(EC.visibility_of_element_located((By.NAME, 'phone')))  # Update the locator here if necessary

# Enter phone number
phone_number_input.send_keys('7799882064')

# Enter name (adjust the locator if necessary)
name_input = driver.find_element(By.NAME, 'name')  # Replace with correct locator
name_input.send_keys('Rakesh')

# Submit the form (update XPath or button locator)
login_button = driver.find_element(By.XPATH, '//*[@id="login_button_id"]')  # Replace with correct login button's XPath
login_button.click()

# Wait for some time to let the page load after submitting
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="profile_element"]')))  # Update with actual element after login

# Verify successful login
print("Login successful!")

# Close the browser
driver.quit()
