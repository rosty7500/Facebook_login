__author__ = 'admin'

from selenium.webdriver.common.by import By

class login_locators(object):
    _email = (By.ID, "email")
    _password = (By.ID, "pass")
    _submit = (By.XPATH, "//form[@id='login_form']/table/tbody/tr[2]/td[3]/label/input")
    _name_present = (By.XPATH, "//li[@id='navItem_1171771790']/a/div/span")
    _incorrect_email = (By.XPATH, "//div[@id='js_0']/div/div/div/a")
    _incorrect_password = (By.XPATH, "//div[@id='js_0']/div/div/div/a")
    _logout_dropdown = (By.ID,"userNavigationLabel")
    _logout = (By.XPATH, "//div[@id='BLUE_BAR_ID_DO_NOT_USE']/div/div/div[1]/div/div/ul/li[12]/a/span/span")












