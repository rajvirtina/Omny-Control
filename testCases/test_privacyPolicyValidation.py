import pytest
from pageObjects.Privacy_PolicyPage import Privacy_PolicyPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_003_PrivacyPolicy:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.logger()

    @pytest.mark.order(3)
    @pytest.mark.regression
    def test_privacyPolicyValidation(self, setup):
        self.driver = setup  # webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.ph = Privacy_PolicyPage(self.driver)
        self.ph.navigateToPrivacyPage()
        self.ph.validateResponsiveness()
        self.ph.validateCompletenessOfInformation()
        self.driver.save_screenshot(".\\Screenshots\\" + "privacyPolicyPage.png")
        self.driver.close()
        self.logger.info("******* End of Validating OmnyControl Privacy Polices**********")


