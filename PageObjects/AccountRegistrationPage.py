from selenium.webdriver.common.by import By

class AccountRegistrationPage():

    txt_firstname_name="firstname"
    txt_lastname_name="lastname"
    txt_email_name="email"
    txt_telephone_name="telephone"
    txt_password_name="password"
    txt_confpassword_name="confirm"
    chk_policy_name="agree"
    btn_cont_xpath="//button[normalize-space()='Continue']"

    def __init__(self,driver):
        self.driver=driver


    def setFirstName(self,fname):
        self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)

    def setPrivacyPolicy(self):
        self.driver.find_element(By.NAME,self.chk_policy_name).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.btn_cont_xpath).click()



