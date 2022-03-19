from lib2to3.pgen2 import driver
from time import sleep
from selenium.webdriver.chrome.service import Service
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




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

#application waits for the login field to be visibles
wait.until(EC.visibility_of_element_located((By.NAME, "text")))

#write the email
driver.find_element(by=By.NAME, value='text').send_keys(email)