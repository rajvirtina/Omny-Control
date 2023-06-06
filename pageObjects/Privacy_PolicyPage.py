import time
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig


class Privacy_PolicyPage:
    privacyUrl = ReadConfig.getPrivacyUrl()

    btn_privacyUrl_xpath = "//form[starts-with(@class,'loginform')]//div[starts-with(@class," \
                           "'row justify-content-center')]//a[contains(text(),'Privacy Policy')] "
    privacy_policy_xpath = "//*[@id='privacy']"
    txt_privacyPolicy_xpath = "//h1[contains(text(), 'PRIVACY POLICY')]"

    def __init__(self, driver):
        self.driver = driver

    def navigateToPrivacyPage(self):
        self.driver.find_element(By.XPATH, self.btn_privacyUrl_xpath).click()
        time.sleep(7)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(self.privacyUrl)

    def validateResponsiveness(self):
        start_time = time.time()
        self.driver.find_element(By.XPATH, self.txt_privacyPolicy_xpath)
        end_time = time.time()
        assert "Omnyk - Enhancing Reach of Healthcare" in self.driver.title
        assert end_time - start_time < 5

    def validateLanguageUsed(self):
        privacy_policy = self.driver.find_element(By.XPATH, self.privacy_policy_xpath)
        assert 'Information We Collect' in privacy_policy.text.lower()
        assert 'Changes to This Policy' in privacy_policy.text.lower()
        assert 'easy to understand' in privacy_policy.text.lower()

    def validateCompletenessOfInformation(self):
        assert "USAGE INFORMATION" in self.driver.page_source
        assert "INFORMATION SECURITY" in self.driver.page_source
        assert "OUR POLICIES FOR CHILDREN" in self.driver.page_source
        assert "CHANGES TO THIS POLICY" in self.driver.page_source
        time.sleep(8)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
