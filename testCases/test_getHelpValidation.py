import pytest
from pageObjects.GetHelpPage import GetHelpPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_GetHelp:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.logger()

    @pytest.mark.order(4)
    @pytest.mark.regression
    def test_getHelpValidation(self, setup):
        self.driver = setup  # webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.gh = GetHelpPage(self.driver)
        self.gh.navigateToPrivacyPage()
        self.gh.validateResponsiveness()
        self.gh.validateCompletenessOfInformation()
        self.driver.save_screenshot(".\\Screenshots\\" + "getHelpPage.png")
        self.driver.close()
        self.logger.info("******* End of Validating OmnyControl GetHelpPage Validation**********")