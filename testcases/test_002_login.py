import pytest
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customerLogger import LogGen
from PageObjects.AccountRegistrationPage import AccountRegistrationPage
import os

class Test_Login():
    baseURL=ReadConfig.getApplicationURL()
    user=ReadConfig.getUserEmail()
    password=ReadConfig.getPassword()

    def test_Login(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp=LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.targetpage=self.lp.isMyAccountPageExists()
        if self.targetpage == True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots" + "test_login")
            assert False
