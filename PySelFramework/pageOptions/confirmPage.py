from selenium.webdriver.common.by import By

class ConfirmPage:
    def __init__(self,driver):
        self.driver = driver

    countrySelector = (By.ID ,"country")
    countryButton = (By.LINK_TEXT , "India")
    checkBoxbutton = (By.XPATH , "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.CSS_SELECTOR ,"[type='submit']")
    successMessage = (By.CSS_SELECTOR ,"[class*='alert-success']")

    def countryCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBoxbutton)

    def getCountrySelector(self):
        return self.driver.find_element(*ConfirmPage.countrySelector)
    
    def getCountryButton(self):
        return self.driver.find_element(*ConfirmPage.countryButton)
    
    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.successMessage)