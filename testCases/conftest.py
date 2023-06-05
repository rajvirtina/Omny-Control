import os.path
import time
import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(30)
        print("Launching Chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(30)
        print("Launching Firefox browser.........")
    else:
        driver = webdriver.Ie()
        driver.maximize_window()
        driver.implicitly_wait(30)
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


#############  PyTest HTML Report #####################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        print("entered into if loop")
        config.stash[metadata_key]['Project Name'] = 'OmnyControl'
        config.stash[metadata_key]['Module Name'] = 'Login'
        config.stash[metadata_key]['Tester'] = 'RajKumar'
    else:
        config._metadata['Project Name'] = 'OmnyControl'
        config._metadata['Module Name'] = 'Login'
        config._metadata['Tester'] = 'RajKumar'


# It is hook for delete/Modify Environment info to HTML Report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    setattr(report, "duration_formatter", "%H:%M:%S.%f")
    extra = getattr(report, "extra", [])
    if report.when == "call":
        extra.append(pytest_html.extras.url("https://omnymanage.dev.omnytraq.com/dashboard"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time() * 1000))) + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html1 = '«div><img src="%s" alt="screenshot" style="width:300px;height=200px"' \
                        'onclick="window.open(this.src)" align="right"/></div/>' % file_name
                extra.append(pytest_html.extras.html(html1))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "OmnyControl Application!"
