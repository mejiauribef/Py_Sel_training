from pageOptions.homePage import HomePage
from tests.HomePageData import HomePageData
from utilities.BaseClass import BaseClass
import pytest


class TestHomePage(BaseClass):

    def test_formSubmission(self , getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("First name is: " + getData["firstname"])
        homePage.getNameInput().send_keys(getData["firstname"])
        log.info(homePage.printJavascript())
        homePage.getEmailInput().send_keys(getData["lastname"])
        homePage.getCheckBoxAccept().click()
        homePage.getSubmitButton().click()
        self.selectOptionByText(homePage.getFormSelect(),getData["gender"])
        alertText = homePage.getSuccessMessage().text
        assert ("Success" in alertText)
        self.driver.refresh()

    homepagedata = HomePageData.test_HomePage_Data
    @pytest.fixture(params= homepagedata)
    def getData(self,request):
        return request.param

    
