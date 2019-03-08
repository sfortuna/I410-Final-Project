import password_generator
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("""
               Welcome to Steve's I430 Final Project
""")
print('-'*50)

name=input("Please enter the name of the website you would liek to create an account for: ")
account=input("Please enter the website url that you want to use: ")
driver = webdriver.Firefox()

if driver.get(account):
    assert name in driver.title
else:
    print("An error has occurred. Please start over.")
    
