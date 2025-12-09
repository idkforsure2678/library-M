from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service())
driver.get("http://localhost/project/Library M.html")

wait = WebDriverWait(driver, 10)  # 10 seconds wait

print("Hello from Selenium")
print("Automated test by: Cris Roniel Ibali")
print("Entering:", driver.title)

# --- Test Case 1: Login ---
print("\nTest Case 1: Login as admin")
driver.find_element(By.ID, "login-button").click()
time.sleep(5)  # Wait for animation
username = driver.find_element(By.ID, "user")
password = driver.find_element(By.ID, "pass")
username.send_keys("admin")
time.sleep(2)
password.send_keys("admin")
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='LOGIN']").click()
wait.until(EC.title_contains("Library M"))
time.sleep(5)
print("Login successful.\n")

# --- Test Case 2: Add a book ---
print("Test Case 2: Add a new book")
time.sleep(2)
driver.find_element(By.ID, "title").send_keys("Selenium Book")
time.sleep(2)
driver.find_element(By.ID, "author").send_keys("Tester")
time.sleep(2)
driver.find_element(By.ID, "year").send_keys("2025")
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Save Book']").click()
wait.until(EC.presence_of_element_located((By.XPATH, "//table[@id='bookTable']//td[text()='Selenium Book']")))
time.sleep(5)
print("Book added successfully.\n")

# --- Test Case 3: Edit the book ---
print("Test Case 3: Edit the added book")
driver.find_element(By.XPATH, "//table[@id='bookTable']//td[text()='Selenium Book']/following-sibling::td/button[@class='edit-btn']").click()
time.sleep(3)
title_field = driver.find_element(By.ID, "title")
title_field.clear()
time.sleep(2)
title_field.send_keys("Selenium Book Edited")
time.sleep(2)
driver.find_element(By.XPATH, "//button[text()='Save Book']").click()
wait.until(EC.presence_of_element_located((By.XPATH, "//table[@id='bookTable']//td[text()='Selenium Book Edited']")))
time.sleep(5)
print("Book edited successfully.\n")

# --- Test Case 4: Delete the book ---
print("Test Case 4: Delete the edited book")
time.sleep(2)
driver.find_element(By.XPATH, "//table[@id='bookTable']//td[text()='Selenium Book Edited']/following-sibling::td/button[@class='delete-btn']").click()
driver.switch_to.alert.accept()
wait.until(EC.invisibility_of_element_located((By.XPATH, "//table[@id='bookTable']//td[text()='Selenium Book Edited']")))
time.sleep(5)
print("Book deleted successfully.\n")

# --- Test Case 5: Add a book for borrow/return ---
print("Test Case 5: Add a book for borrowing")
driver.find_element(By.ID, "title").send_keys("Borrow Test Book")
driver.find_element(By.ID, "author").send_keys("Tester")
driver.find_element(By.ID, "year").send_keys("2025")
driver.find_element(By.XPATH, "//button[text()='Save Book']").click()
wait.until(EC.presence_of_element_located((By.XPATH, "//table[@id='bookTable']//td[text()='Borrow Test Book']")))
time.sleep(5)
print("Borrow test book added successfully.\n")

# --- Test Case 6: Borrow the book ---
print("Test Case 6: Borrow the book")
driver.find_element(By.XPATH, "//table[@id='bookTable']//td[text()='Borrow Test Book']/following-sibling::td/button[text()='Borrow']").click()
wait.until(EC.visibility_of_element_located((By.ID, "borrowerName")))
driver.find_element(By.ID, "borrowerName").send_keys("John Doe")
time.sleep(3)
driver.find_element(By.XPATH, "//button[text()='Confirm']").click()
driver.find_element(By.XPATH, "//button[text()='Borrowed Books']").click()
wait.until(EC.presence_of_element_located((By.XPATH, "//table[@id='borrowedTable']//td[text()='Borrow Test Book']")))
time.sleep(5)
print("Book borrowed successfully.\n")

# --- Test Case 7: Return the book ---
print("Test Case 7: Return the borrowed book")
driver.find_element(By.XPATH, "//table[@id='borrowedTable']//td[text()='Borrow Test Book']/following-sibling::td/button[text()='Return']").click()
driver.find_element(By.XPATH, "//button[text()='Available Books']").click()
wait.until(EC.presence_of_element_located((By.XPATH, "//table[@id='bookTable']//td[text()='Borrow Test Book']")))
time.sleep(5)
print("Book returned successfully.\n")

# --- Test Case 8: View Borrow/Return Logs ---
print("Test Case 8: View Borrow/Return logs")
driver.find_element(By.XPATH, "//button[text()='Borrow/Return Logs']").click()
wait.until(EC.presence_of_element_located((By.XPATH, "//table[@id='logTable']//td[text()='John Doe']")))
log_rows = driver.find_elements(By.XPATH, "//table[@id='logTable']//td[4]")  # Borrower column
borrower_names = [b.text for b in log_rows]
time.sleep(5)
print("Logs fetched:", borrower_names, "\n")

# --- Test Case 9: Search functionality ---
print("Test Case 9: Search functionality")
search_field = driver.find_element(By.ID, "search")
search_field.send_keys("Borrow Test Book")
wait.until(EC.presence_of_element_located((By.XPATH, "//table//td[text()='Borrow Test Book']")))
time.sleep(5)
print("Search executed successfully.\n")
search_field.clear()
time.sleep(2)

# --- Test Case 10: Switch table views ---
print("Test Case 10: Switch table views")
driver.find_element(By.XPATH, "//button[text()='Available Books']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[text()='Borrowed Books']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[text()='Borrow/Return Logs']").click()
time.sleep(5)
print("Table views switched successfully.\n")

print("All automated tests completed successfully.")
driver.quit()
