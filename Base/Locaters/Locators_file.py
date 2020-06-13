

class Locators():

    #Login page Locators

    Link = "https://www.instagram.com/"
    UserID_field = "//input[@name='username']"
    Password_field = "//input[@name='password']"
    LoginButton_field = "//button[@class='sqdOP  L3NKy   y3zKF     ']"
    Invalid_username_text_path="//div[@class='eiCW-']/p"
    insta_invalid_email_text="The username you entered doesn't belong to an account. Please check your username and try again."
    insta_invalid_password_text="Sorry, your password was incorrect. Please double-check your password."

    #Home page Locators

    Loginalert = "//button[@class='aOOlW   HoLwm ']"
    LoginalertON="//div/button[@class='aOOlW  bIiDR  ']"
    Hearts = "//span[@class='fr66n']"
    Search = "XTCLo x3qfX"
    profile_icon="//div[@class='Fifk5']//span[@class='_2dbep qNELH']"


    #Profile page Locators

    ProfileIcon = "//div[@class='Fifk5']//span[@class='_2dbep qNELH']"
    PostElement = "//span[@class='-nal3 '] "
    FollowerElement = "//div[@class='Fifk5']//a[@class='_2dbep qNELH kIKUG']"
    NumberOf_Users = "//div[@class='PZuss']/li"
    Close_followers = "//button[@class='wpO6b']"
    UserNamesElement="//a[@class='FPmhX notranslate  _0imsa '] "
    CloseButtonofFollowing= "//div[@class='WaOAr']/button[@class='wpO6b ']"

    #Setting page locators or Logout

    SettingOption = "//button[@class='wpO6b ']"
    LogoutButton = "//button[text()='Log Out']"