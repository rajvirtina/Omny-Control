import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.readProperties import ReadConfig


class LoginPage:
    userName = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    textbox_username_id = "exampleInputEmail1"
    textbox_password_name = "password"
    btn_login_xpath = "//form[@method='post']//child::button[text()='Login']"
    btn_successfullyLogin_xpath = "//button[text()='Done']"
    btn_profileDropdown_xpath = "//a[starts-with(@id,'navbar')]//div"
    btn_logOut_id = "logout"
    btn_logOutConfirmYes_xpath = "//button[text()='Yes, Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self):
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(self.userName)
        time.sleep(2)
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(self.password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
        try:
            element = self.driver.find_element(By.XPATH, self.btn_successfullyLogin_xpath)
        except:
            print("Successfully Not Logged into the Account")
            time.sleep(5)
        else:
            element.click()
            time.sleep(5)

    def accountLogOut(self):
        self.driver.find_element(By.XPATH, self.btn_profileDropdown_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_profileDropdown_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, self.btn_logOut_id)))
        self.driver.find_element(By.ID, self.btn_logOut_id).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.btn_logOutConfirmYes_xpath).click()
        time.sleep(2)

    def resetPassword(self):
        pass

