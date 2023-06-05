import configparser
import secrets
import string
import time
from random import random

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
    btn_profile_xpath = "//*[@class='dropdown-item']"
    btn_edit_xpath = "//a[contains(text(),'Edit')]"
    btn_updateUser_xpath = "//button[contains(text(),'Update User')]"

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
        self.driver.find_element(By.XPATH, self.btn_profileDropdown_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_profileDropdown_xpath).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_profile_xpath)))
        self.driver.find_element(By.XPATH, self.btn_profile_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_edit_xpath).click()
        pass_word = string.ascii_letters + string.digits + string.punctuation
        updatedPassword = ''
        for i in range(8):
            updatedPassword += ''.join(secrets.choice(pass_word))
        #updatedPassword = "Nehaagatebc"
        element = self.driver.find_element(By.NAME, self.textbox_password_name)
        element.clear()
        element.send_keys(updatedPassword)
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.btn_updateUser_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_successfullyLogin_xpath).click()
        time.sleep(5)
        self.accountLogOut()
        wait.until(EC.element_to_be_clickable((By.ID, self.textbox_username_id)))
        try:
            config = configparser.ConfigParser()
            config.read('.\\Configuration\\config.ini')
            # Update the username value
            config['common info']['password'] = updatedPassword
            # Save the changes to the config file
            with open('.\\Configuration\\config.ini', 'w') as configfile:
                config.write(configfile)
            print("Logged with Update Password : " + updatedPassword)
            self.driver.find_element(By.ID, self.textbox_username_id).send_keys(self.userName)
            time.sleep(2)
            self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(self.password)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
            self.driver.find_element(By.XPATH, self.btn_successfullyLogin_xpath).click()
        except:
            self.driver.find_element(By.ID, self.textbox_username_id).send_keys(self.userName)
            self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(updatedPassword)
            time.sleep(2)
            self.driver.find_element(By.XPATH, self.btn_login_xpath).click()
            self.driver.find_element(By.XPATH, self.btn_successfullyLogin_xpath).click()
        time.sleep(5)
