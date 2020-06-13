import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Base.Locaters.Locators_file import Locators

class ProfilePage():

    def __init__(self, driver,actions):
        self.actions = actions
        self.driver = driver


    def Clicking_profileIcon(self):
        return self.driver.find_element(By.XPATH,Locators.ProfileIcon).click()

    def TotalPost(self):
        post = self.driver.find_element(By.XPATH, Locators.PostElement)
        return print(post.text)

    def TotalFollowers(self):
        self.driver.find_element(By.XPATH, Locators.FollowerElement).click()
        self.driver.implicitly_wait(3)
        MaxValue = self.driver.find_element(By.XPATH, "//span[contains(@title,'2')]")
        self.Max = MaxValue.text
        print("Number of followers are:" + self.Max)
        return self.Max

    def GetfollowerNames(self):
        self.driver.find_element(By.XPATH, "//div[@class='Fifk5']//a[@class='_2dbep qNELH kIKUG']").click()
        self.driver.find_element(By.XPATH, "//a[text()=' followers']").click()
        time.sleep(3)
        self.actions.send_keys(Keys.TAB).perform()
        self.actions.send_keys(Keys.TAB).perform()
        NumberOfUserS = self.driver.find_elements(By.XPATH, Locators.NumberOf_Users)
        x = len(NumberOfUserS)
        print(x)
        while x < int(self.Max):
            self.actions.key_down(Keys.SPACE).perform()
            y = self.driver.find_elements(By.XPATH, Locators.NumberOf_Users)
            x = len(y)
        print(x)

        Names=self.driver.find_elements(By.XPATH,Locators.UserNamesElement)
        print(len(Names))

        for j in Names:
            print(j.text)

    def ScrollFollow(self):
        NumberOfUser = self.driver.find_elements(By.XPATH, Locators.NumberOf_Users)
        a = len(NumberOfUser)
        while a < int(self.Max):
            self.actions.key_down(Keys.SPACE).perform()
            b = self.driver.find_elements(By.XPATH, Locators.NumberOf_Users)
            a = len(b)
        print(a)

    def Closebutton_of_follwers(self):
        self.driver.find_element(By.XPATH, Locators.Close_followers).click()
        time.sleep(5)

    def Nooffollowing(self):
        self.driver.find_element(By.XPATH,"//div[@class='Fifk5']//a[@class='_2dbep qNELH kIKUG']").click()
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH,"//a[text()=' following']").click()
        time.sleep(3)

    def Close_Button_of_Following(self):
        self.driver.find_element(By.XPATH,Locators.CloseButtonofFollowing).click()
        time.sleep(5)



