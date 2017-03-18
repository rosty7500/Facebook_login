__author__ = 'admin'

from selenium import webdriver
import time
import os
import csv

from pages.Locators import login_locators

path = os.getcwd()
print(path)

class feature_pages(object):
    def __init__(self, base_url):
        self.driver = webdriver.Chrome(path + '\\chrome\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(base_url)

        #valid login

    def accessing_signin_pages_valid(self):
        driver1 = self.driver
        time.sleep(10)
        driver1.find_element(*login_locators._email).send_keys("rosty_06@yahoo.com")
        driver1.find_element(*login_locators._password).send_keys("rash02079190!@#$%")
        time.sleep(2)
        driver1.find_element(*login_locators._submit).click()
        time.sleep(8)
        driver1.find_element(*login_locators._name_present).is_displayed()
        driver1.quit()

        #invalid email

    def accessing_invalid_login(self):
        driver1 = self.driver
        time.sleep(10)
        driver1.find_element(*login_locators._email).send_keys("rosty_06@gmail.com")
        driver1.find_element(*login_locators._password).send_keys("rash02079190!@#$%")
        time.sleep(2)
        driver1.find_element(*login_locators._submit).click()
        time.sleep(10)
        self.invalid_email = driver1.find_element(*login_locators._incorrect_email).text
        driver1.quit()
        return self.invalid_email

        #invalid password

    def accessing_invalid_password_login(self):
        driver1 = self.driver
        time.sleep(10)
        driver1.find_element(*login_locators._email).send_keys("rosty_06@yahoo.com")
        driver1.find_element(*login_locators._password).send_keys("test")
        time.sleep(2)
        driver1.find_element(*login_locators._submit).click()
        time.sleep(15)
        self.invalid_password = driver1.find_element(*login_locators._incorrect_password).text
        driver1.quit()
        return self.invalid_password

        #Multiple logins (Need to update the CSV)

    def accessing_multiple_login(self):
        with open('login-import-data.csv') as csv_file:
            readCSV = csv.reader(csv_file, delimiter=',')
            u = []
            p = []
            for row in readCSV:
                username = row[0]
                password = row[1]
                u.append(username)
                p.append(password)

        for i in range(0, len(u)):
            driver1 = self.driver
            element = driver1.find_element(*login_locators._email).send_keys(u[i])
            print (u[i])
            element1 = driver1.find_element(*login_locators._password).send_keys(p[i])
            print(p[i])
            time.sleep(3)
            driver1.find_element(*login_locators._submit).click()
            time.sleep(6)
            driver1.find_element(*login_locators._logout_dropdown).click()
            time.sleep(5)
            driver1.find_element(*login_locators._logout).click()
            i = i + 1
        driver1.quit()








