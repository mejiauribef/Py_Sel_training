from selenium.webdriver.common.by import By

from pageOptions.confirmPage import ConfirmPage

class CheckoutPage:
    def __init__(self,driver):
        self.driver = driver

    cardtitle = (By.CSS_SELECTOR ,".card-title a")
    cardfooter = (By.CSS_SELECTOR ,".card-footer button")
    checkoutbutton = (By.CSS_SELECTOR ,"a[class*='btn-primary']")
    checkoutcardbb = (By.CSS_SELECTOR, "h4.media-heading a")
    checkoutbutton2 = (By.XPATH ,"//button[@class='btn btn-success']")
    
    

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardtitle)
    
    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardfooter)
    
    def getCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutbutton)

    def getCheckoutTitles(self):
        return self.driver.find_elements(*CheckoutPage.checkoutcardbb)
         

    def getCheckoutButton2(self):
        self.driver.find_element(*CheckoutPage.checkoutbutton2).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

    