from PageObjects.AccountRegistrationPage import AccountRegistrationPage
from PageObjects.HomePage import HomePage
from utilities.customerLogger import LogGen


class Test_001_AccountReg:
    baseURL = "https://www.flipkart.com/account/login?ret=/"
    logger=LogGen.logger()

    def test_account_reg(self, setup):
        self.logger.info("**** test-0001-AccountRegistration started***")
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
        self.logger.info("**** test-0001-AccountRegistration finished***")
