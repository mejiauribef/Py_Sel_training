# Implicit wait 
# Explicit wait
# Pause the test for few secons using Time class
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#for explicit wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

# implicit wait or global wait // wait until 5 seconds if object is not displayed 
# if app takes 1.5s to load whole content it will not wait the 5 seconds, this input is the max wait
# uncomment next line to have it active
# driver.implicitly_wait(5)

driver.get("http://www.rahulshettyacademy.com/seleniumPractise/")

# Here we search for products containing "ber"
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
count =len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

# ATC for all buttons
for button in buttons:
    button.find_element_by_xpath("parent::div/parent::div/h4").text
    button.click()

# Open cart and proceed to checkout
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_css_selector("div.action-block button").click()

#Explicit wait
wait = WebDriverWait(driver,5)
wait.until(EC.presence_of_element_located(By.CLASS_NAME,"promoCode"))

# Enter promo code 
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

wait.until(EC.presence_of_element_located(By.CSS_SELECTOR,"span.promoInfo"))
print(driver.find_element_by_css_selector("span.promoInfo").text)

driver.close()