import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = None


def pytest_addoption(parser):
        parser.addoption(
                "--browser_name", action="store",default="chrome"
        )

@pytest.fixture(scope="class")
def web_driver_setup(request):
        global driver
        browser_name = request.config.getoption("browser_name")
        if browser_name == "chrome":
                driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser_name == "firefox":
                driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser_name == "edge":
                driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        time.sleep(5)
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        request.cls.driver = driver
        yield
        driver.close()

@pytest.mark.hookwrapper 
def pytest_runtest_makereport(item):
        """
        Extends the PyTest Plugin to take an screenshot in html report, whenever test fails.
        :param item:
        """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])
        if report.when == 'call' or report.when == "setup":
                xfail = hasattr(report, 'wasxfail')
                if (report.skipped and xfail) or (report.failed and not xfail):
                        file_name = report.nodeid.replace("::", "_") + ".png"
                        _capture_screenshot(file_name)
                        if file_name:
                                html = '<img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                                       'onclick="window.open(this.src)" align="right"/>' % file_name
                        extra.append(pytest_html.extras.html(html))
                        report.extra = extra

def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)



