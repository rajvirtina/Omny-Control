import pytest
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_002_ResetPassword:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.logger()

    @pytest.mark.order(2)
    @pytest.mark.regression
    def test_resetPassword(self,setup):
        self.logger.info("****************** Verifying Login to the OmnyControl ****************")
        self.driver = setup # webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName()
        self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
        self.lp.resetPassword()
        self.driver.save_screenshot(".\\Screenshots\\" + "AbleToLoginWithUpdatedPassword.png")
        self.lp.accountLogOut()
        self.driver.close()