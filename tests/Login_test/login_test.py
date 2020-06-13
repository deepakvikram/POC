from pages.LoginPage.Log_page import LoginPage
from selenium import webdriver
from selenium.webdriver import ActionChains
from Base.Locaters.Selenium_Driver import SeleniumDriver
import pytest
from Base.Locaters.Locators_file import Locators
import time
from selenium.webdriver.common.by import By
from pages.HomePage.Home_page import homePageInsta
from pages.LogOutPage.LogOut import LogOut


driver = webdriver.Chrome()
actions = ActionChains
Lp = LoginPage(driver)
SL = SeleniumDriver(driver)
HM = homePageInsta(driver,actions)
LO= LogOut(driver)


@pytest.mark.run(order=3)
def test_Valid_login():
    SL.GetLink_and_maximize()
    Lp.Login("deepakvikram7@gmail.com", "@")
    time.sleep(3)
    HM.Insta_alert_Notnow()
    user = driver.find_element(By.XPATH, Locators.profile_icon)
    if user is not None:
        assert True
    else:
        assert False
    ##Logging out user
    HM.profile_icon_click()
    LO.GotoSetting()
    LO.Click_Logout()


@pytest.mark.run(order=2)
def test_Invalid_loginID():
    SL.GetLink_and_maximize()
    Lp.Login( "deepakvikram7@gmail.co", "1234567890")
    time.sleep(4)
    invalid_username_text_check=driver.find_element(By.XPATH, Locators.Invalid_username_text_path)
    text=invalid_username_text_check.text
    assert text == Locators.insta_invalid_email_text

@pytest.mark.run(order=1)
def test_Invalid_Password():
    SL.GetLink_and_maximize()
    Lp.Login( "deepakvikram7@gmail.com", "1234567890")
    time.sleep(4)
    invalid_username_text_check=driver.find_element(By.XPATH, Locators.Invalid_username_text_path)
    invalid_text_pass=invalid_username_text_check.text
    assert invalid_text_pass == Locators.insta_invalid_password_text

