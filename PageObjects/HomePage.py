

from selenium.webdriver.common.by import By


class HomePage():

#Locators
    lnk_myaccount_xpath="//span[normalize-space()='My Account']"
    lnk_register_linktext="Register"
    lnk_login_linktext="Login"

#constructor
    def __init__(self,driver):
        self.driver=driver

#Action method

    def clickmyaccount(self):
        self.driver.find_element(By.XPATH,self.lnk_myaccount_xpath).click()



    def clickregister(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_register_linktext).click()

    def clicklogin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()


