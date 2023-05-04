from pageOptions.homePage import HomePage
from utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    def test_e2e(self):
        cardsadded = []
        checkoutcardtitles = []
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkoutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()
                cardsadded.append(cardText)
            elif cardText == "iphone X":
                checkoutPage.getCardFooter()[i].click()
                cardsadded.append(cardText)
            
        
        checkoutPage.getCheckoutButton().click()
        checkouttitles = checkoutPage.getCheckoutTitles()
        i = -1
        for titles in checkouttitles:
            i = i + 1
            titlesadded = titles.text
            log.info(titlesadded)
            checkoutcardtitles.append(titlesadded)
        
        log.info(checkoutcardtitles)
        log.info(cardsadded)
        assert checkoutcardtitles == cardsadded 

        confirmPage = checkoutPage.getCheckoutButton2()
        log.info("Entering country name as ind")
        confirmPage.getCountrySelector().send_keys("ind")
        self.veryfyLinkPresence("India")
        confirmPage.getCountryButton().click()
        confirmPage.countryCheckBox().click()
 
        assert confirmPage.countryCheckBox().is_selected
        confirmPage.getPurchaseButton().click()
        textMatch = confirmPage.getSuccessMessage().text
        log.info("Text recieved from application is: " + textMatch )

        assert  ("Success! Thank you!" in textMatch)


        
