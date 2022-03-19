from lib2to3.pgen2 import driver
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


url = 'https://twitter.com/'

username = input("Please enter your twitter email:\n")
password = input("Please enter your twitter password: \n")

#instantiate the chrome class web
driver = webdriver.Chrome(ChromeDriverManager().install())

#maximize the chrome windows to full-screen
driver.maximize_window()

driver.get("https://twitter.com/")





