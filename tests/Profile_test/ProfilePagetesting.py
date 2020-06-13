from selenium import webdriver
from selenium.webdriver import ActionChains
from pages.ProfilePage.Profile_page import ProfilePage

driver = webdriver.Chrome()
actions = ActionChains

P1=ProfilePage(driver,actions)
P1.Clicking_profileIcon()