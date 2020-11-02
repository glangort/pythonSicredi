from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from numpy.core.defchararray import join

browser = webdriver.Chrome(executable_path=r'./chromedriver.exe')
browser.get('http://www.rpachallenge.com/')

my_dataframe = pd.read_excel('./challenge.xlsx')


buttonStart = browser.find_element_by_xpath(
    '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')
buttonStart.click()
count = 0
for index, row in my_dataframe.iterrows():
    email = browser.find_element(
        By.CSS_SELECTOR, '[ng-reflect-name=labelEmail]').send_keys(str(my_dataframe['Email'][index]))

    phone = browser.find_element(
        By.CSS_SELECTOR, '[ng-reflect-name=labelPhone]').send_keys(str(my_dataframe['Phone Number'][index]))

    role = browser.find_element(
        By.CSS_SELECTOR, '[ng-reflect-name=labelRole]').send_keys(str(my_dataframe['Role in Company'][index]))

    first = browser.find_element(
        By.CSS_SELECTOR, '[ng-reflect-name=labelFirstName]').send_keys(str(my_dataframe['First Name'][index]))

    last = browser.find_element(
        By.CSS_SELECTOR, '[ng-reflect-name=labelLastName]').send_keys(str(my_dataframe['Last Name '][index]))

    address = browser.find_element(
        By.CSS_SELECTOR, '[ng-reflect-name=labelAddress]').send_keys(str(my_dataframe['Address'][index]))

    company = browser.find_element(
        By.CSS_SELECTOR, '[ng-reflect-name=labelCompanyName]').send_keys(str(my_dataframe['Company Name'][index]))

    button = browser.find_element_by_xpath(
        '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')  # next
    button.click()
