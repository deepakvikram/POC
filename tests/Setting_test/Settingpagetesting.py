from selenium import webdriver
from selenium.webdriver import ActionChains
from pages.LogOutPage.LogOut import LogOut


driver = webdriver.Chrome()
actions = ActionChains

L1 = LogOut(driver)
L1.GotoSetting()
L1.Click_Logout()