import time
from selenium.webdriver.common.by import By
from Base.Locaters.Locators_file import Locators
from selenium import webdriver
from Base.Locaters.Selenium_Driver import SeleniumDriver

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def getloginLink(self):
        return self.driver.get(Locators.Link)

    def getUserID(self):
        return self.driver.find_element(By.XPATH, Locators.UserID_field)

    def getPass(self):
        return self.driver.find_element(By.XPATH, Locators.Password_field)

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, Locators.LoginButton_field)

    def enterID(self, email):
        self.getUserID().send_keys(email)

    def enterPass(self, password):
        self.getPass().send_keys(password)

    def clickLogin(self):
        self.getLoginButton().click()

    def Login(self,email="", password=""):
        time.sleep(2)
        self.enterID(email)
        time.sleep(2)
        self.enterPass(password)
        self.clickLogin()
