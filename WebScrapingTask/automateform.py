from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# Navigate to the Google form
driver.get("https://forms.gle/WT68aV5UnPajeoSc8")

# Wait for the form to load
WebDriverWait(driver, 10).until(EC.title_contains("Python (Selenium) Assignment"))


def fill_form(name, phone, email, address, pin, dob, gender, code):
    inputs = driver.find_elements(By.CLASS_NAME, "whsOnd.zHQkBf")
    addR = driver.find_element(By.CLASS_NAME, 'KHxj8b.tL9Q4c')

    time.sleep(10)
    inputs_array = [
        name, phone, email, pin, dob, gender, code
    ]

    for i in range(len(inputs)):
        inputs[i].clear()
        inputs[i].send_keys(inputs_array[i])
    time.sleep(5)
    addR.send_keys(address)
    time.sleep(5)
    submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "NPEfkd.RveJvd.snByac")))
    submit_button.click()


# Set up the Chrome driver


# Fill in the form fields
# name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "whsOnd.zHQkBf")))
# name_input.send_keys("Pradeep Kumar Meena")

# phone_input = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CLASS_NAME, "whsOnd.zHQkBf")))
# phone_input.send_keys("8209221145")

# email_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "whsOnd.zHQkBf")))
# email_input.send_keys("pradeepmeena1608@gmail.com")

# address_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "KHxj8b.tL9Q4c")))
# address_input.send_keys("Hostel H Indian Institute of Technology Gandhinagar, Gandhinagar Gujrarat")

# pin_code = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "whsOnd.zHQkBf")))
# pin_code.send_keys("382355")

# dob = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "whsOnd.zHQkBf")))
# dob.send_keys("16/08/2004")

# gender = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "whsOnd.zHQkBf")))
# dob.send_keys("Male")

# ver_code = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "whsOnd.zHQkBf")))
# ver_code.send_keys("GNFPYC")

# # Submit the form
# submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "NPEfkd.RveJvd.snByac")))
# submit_button.click()


fill_form('Pradeep Kumar Meena', 8209221145, 'pradeepmeena1608@gmail.com', 'Hostel H Indian Institute of Technology Gandhinagar, Gandhinagar Gujrarat',382355, "16/08/2004", "Male", "GNFPYC")
time.sleep(2)  # wait for the confirmation page to load
driver.save_screenshot('confirmation_page.png')
# Close the browser
driver.quit()




    


