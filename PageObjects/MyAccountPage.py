from selenium.webdriver.common.by import By

class MyAccountPage():
    ink_logout_xpath="//a[@class='dropdown-item'][normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.ink_logout_xpath).click()