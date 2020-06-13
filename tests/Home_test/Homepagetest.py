from pages.HomePage.Home_page import homePageInsta
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
actions = ActionChains


h1 = homePageInsta(driver,actions)
time.sleep(5)
h1.Insta_alert_Notnow()