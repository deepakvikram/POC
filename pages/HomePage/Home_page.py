import time
from selenium.webdriver.common.by import By
from Base.Locaters.Locators_file import Locators
from selenium.webdriver.common.keys import Keys

class homePageInsta():

    def __init__(self, driver,actions):
        self.driver = driver
        self.actions = actions

    def Insta_alert_Notnow(self):
        return self.driver.find_element(By.XPATH, Locators.Loginalert).click()

    def Insta_alert_turnOn(self):
        return self.driver.find_element(By.XPATH,Locators.LoginalertON).click()

    def heart_element(self):
        len_of_hearts=self.driver.find_elements(By.XPATH, Locators.Hearts)
        return len(len_of_hearts)

    def Click_heart(self):
        NoOfHearts = self.heart_element()
        for i in range(NoOfHearts):
            self.driver.find_element(By.XPATH, Locators.Hearts).click()
            time.sleep(5)
        self.actions.send_keys(Keys.END, Keys.HOME).perform()
        time.sleep(10)

    def search_element(self):
        return self.driver.find_element(By.CLASS_NAME, Locators.Search)

    def Send_values_in_search(self, search):
        return self.search_element().send_keys(search)

    def profile_icon_click(self):
        return self.driver.find_element(By.XPATH, Locators.profile_icon).click()

    #def Insta_alert_close(self):
        #return self.Insta_alert_Notnow().click()


