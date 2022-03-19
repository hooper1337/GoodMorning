from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from keyboard import press




url = 'https://twitter.com/i/flow/login'

email = input("Please enter your twitter email: ")
print("\n")
password = input("Please enter your twitter password: ")

#instantiate the chrome class web
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)
wait = WebDriverWait(driver, 30)

#maximize the chrome windows to full-screen
driver.maximize_window()

#open twitter 
driver.get(url)

#application waits for the email field to be visibles
wait.until(EC.visibility_of_element_located((By.NAME, "text")))

#write the email
driver.find_element(by=By.NAME, value='text').send_keys(email)

#click on advance
press('enter')

#application waits for the email field to be visibles
wait.until(EC.visibility_of_element_located((By.NAME, "password")))

#write the password
driver.find_element(by=By.NAME, value='password').send_keys(password)

#click on login
press('enter')

sleep(10)