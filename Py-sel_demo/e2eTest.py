from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#for explicit wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_link_text("Shop").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")


# Product's tile Xpath //div[@class='card h-100']
# Produc't title Xpath //div[@class='card h-100']/div/h4/a
for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
wait = WebDriverWait(driver, 17)
wait.until(EC.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

assert driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").is_selected

driver.find_element_by_css_selector("input[type='submit']").click()
successText = driver.find_element_by_css_selector("div.alert-success").text

assert "Success! Thank you!" in successText
driver.get_screenshot_as_file("screen.png")


driver.close()