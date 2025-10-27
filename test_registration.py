from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start ChromeDriver
driver = webdriver.Chrome()

# Open your Kubernetes app
driver.get("http://localhost:31634")  # update if NodePort changes
driver.maximize_window()  # helps make elements visible
time.sleep(2)

# Fill the form
driver.find_element(By.NAME, "full_name").send_keys("Test User")
driver.find_element(By.NAME, "email").send_keys("test_user@gmail.com")
driver.find_element(By.NAME, "username").send_keys("testuser123")
driver.find_element(By.NAME, "password").send_keys("password123")
driver.find_element(By.NAME, "confirm_password").send_keys("password123")
driver.find_element(By.NAME, "phone").send_keys("9876543210")
driver.find_element(By.NAME, "dob").send_keys("2000-01-01")
driver.find_element(By.NAME, "gender").send_keys("Male")
driver.find_element(By.NAME, "address").send_keys("Hyderabad, India")

# Wait for the button to be clickable
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

# Scroll into view (in case something overlaps)
driver.execute_script("arguments[0].scrollIntoView(true);", button)
time.sleep(1)

# Try clicking the button safely
try:
    button.click()
except Exception as e:
    print(f"Normal click failed: {e}. Trying JavaScript click.")
    driver.execute_script("arguments[0].click();", button)

time.sleep(3)
print("Test Completed Successfully!")
driver.quit()

