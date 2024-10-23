from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

edge_driver_path = r"C:\Windows\msedgedriver.exe"
service = Service(edge_driver_path)
driver = webdriver.Edge(service=service)

driver.get('https://web.whatsapp.com')
print("In 5 seconds, scan the QR code.")
time.sleep(5)  

contacts_and_files = [
    ('1213321123', r'C:\Users\admin\Documents\A.KARTHIKEYAN[192325143]poster-1[1].pptx'),
]

for phone_number, file_path in contacts_and_files:

    search_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true" and @data-tab="3"]'))
    )
    search_box.clear()
    search_box.send_keys(phone_number)

    contact = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, f'//span[@title="{phone_number}"]'))
    )
    contact.click()

    message_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true" and @data-tab="6"]'))
    )
    message_box.send_keys('Sending you a file.')
    message_box.send_keys(Keys.ENTER)

    attach_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@title="Attach"]'))
    )
    attach_button.click()


    file_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//input[@accept="*"]'))
    )
    file_input.send_keys(file_path)

    send_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//span[@data-icon="send"]'))
    )
    send_button.click()

    print(f"File sent to {phone_number} successfully.")

driver.quit()
