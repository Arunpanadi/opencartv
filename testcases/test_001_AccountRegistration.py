from PageObjects.AccountRegistrationPage import AccountRegistrationPage
from PageObjects.HomePage import HomePage


class Test_001_AccountReg:
    baseURL = "https://demo.opencart.com/"

    def test_account_reg(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.hp.clickmyaccount()
        self.hp.clickregister()

        self.regpage = AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("ak")
        self.regpage.setLastName("s")
        self.regpage.setEmail("razpo0@gmail.com")
        #self.email=randomeString.random_string_generator()+'gmail.com'
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
