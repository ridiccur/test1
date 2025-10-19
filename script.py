import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.rpachallenge.com/")

employees_table = pd.read_excel('challenge.xlsx', dtype=str)

start_button = driver.find_element(By.XPATH, "//button[text()='Start']")
start_button.click()

for i in range(len(employees_table)):
    fname_table = employees_table.loc[i, 'First Name']
    fname_input = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']")
    fname_input.send_keys(fname_table)

    lname_table = employees_table.loc[i, 'Last Name ']
    lname_input = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']")
    lname_input.send_keys(lname_table)

    company_table = employees_table.loc[i, 'Company Name']
    company_input = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']")
    company_input.send_keys(company_table)

    role_table = employees_table.loc[i, 'Role in Company']
    role_input = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']")
    role_input.send_keys(role_table)

    address_table = employees_table.loc[i, 'Address']
    address_input = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']")
    address_input.send_keys(address_table)

    email_table = employees_table.loc[i, 'Email']
    email_input = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']")
    email_input.send_keys(email_table)

    phone_table = employees_table.loc[i, 'Phone Number']
    phone_input = driver.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']")
    phone_input.send_keys(phone_table)

    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()







