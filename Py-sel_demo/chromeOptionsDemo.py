from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Object to handle the different chorme options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")   #window does not appear at all
chrome_options.add_argument("--ignore-certificare-errorrs")

driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)