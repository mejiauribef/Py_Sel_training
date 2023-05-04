from selenium.webdriver.common.by import By
from pageOptions.checkoutPage import CheckoutPage

class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage

    #test_HomePage code
    nameinput = (By.CSS_SELECTOR , "[name='name']")
    emailinput = (By.NAME , "email")
    checkboxaccept = (By.ID,"exampleCheck1")
    formselect = (By.ID, "exampleFormControlSelect1")
    submitbutton = (By.XPATH, "//input[@value='Submit']")
    successmessage = (By.CSS_SELECTOR , "[class*='alert-success']")

    def getNameInput(self):
        return self.driver.find_element(*HomePage.nameinput)

    def getEmailInput(self):
        return self.driver.find_element(*HomePage.emailinput)

    def getCheckBoxAccept(self):
        return self.driver.find_element(*HomePage.checkboxaccept)

    def getFormSelect(self):
        return self.driver.find_element(*HomePage.formselect)

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submitbutton)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successmessage)

    #Code for printing input
    def printJavascript(self):
        return self.driver.execute_script('return document.getElementsByName("name")[0].value')
