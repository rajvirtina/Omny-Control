import pytest
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.logger()

    @pytest.mark.order(1)
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("****************** Verifying Login to the OmnyControl ****************")
        self.driver = setup # webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName()
        self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")

        act_title = self.driver.title
        exp_title = "OmnyControl"

        if act_title == exp_title:
            self.logger.info("*** Successfully lands in the OmnyControl DashBoard ***")
        elif act_title != exp_title:
            self.logger.info("**** Successfully not lands in the OmnyControl DashBoard ****")
        self.lp.accountLogOut()
        self.driver.close()
        self.logger.info("******* End of Login to the OmnyControl **********")
