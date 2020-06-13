import time
from selenium.webdriver.common.by import By
from Base.Locaters.Locators_file import Locators

class LogOut():

    def __init__(self,driver):
        self.driver = driver

    def GotoSetting(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators.SettingOption).click()

    def Click_Logout(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, Locators.LogoutButton).click()

    def QuitDriver(self):
        return self.driver.quit()