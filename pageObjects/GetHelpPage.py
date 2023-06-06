import time
from selenium.webdriver.common.by import By


class GetHelpPage:

    btn_getHelpUrl_xpath = "//form[starts-with(@class,'loginform')]//div[starts-with(@class," \
                           "'row justify-content-center')]//a[contains(text(),'Get Help')] "
    get_help_xpath = "//div[@class='card-help ']"
    txt_getHelp_xpath = "//p[contains(text(), 'Get Help')]"

    def __init__(self, driver):
        self.driver = driver

    def navigateToPrivacyPage(self):
        self.driver.find_element(By.XPATH, self.btn_getHelpUrl_xpath).click()
        time.sleep(4)

    def validateResponsiveness(self):
        start_time = time.time()
        self.driver.find_element(By.XPATH, self.txt_getHelp_xpath)
        end_time = time.time()
        assert "OmnyControl" in self.driver.title
        assert end_time - start_time < 5

    def validateLanguageUsed(self):
        get_help = self.driver.find_element(By.XPATH, self.get_help_xpath)
        assert 'clear' in get_help.text.lower()
        assert 'concise' in get_help.text.lower()
        assert 'easy to understand' in get_help.text.lower()

    def validateCompletenessOfInformation(self):
        assert "Search " in self.driver.page_source
        assert " tset " in self.driver.page_source
        assert " Test " in self.driver.page_source
        time.sleep(8)