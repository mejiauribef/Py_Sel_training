from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

#Using JS methods to get the DOM value attribute
driver.find_element_by_name("name").send_keys("hello")
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

#Clicking the button using Js click not Selenium 
shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();",shopButton)
#Scroll using Js
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

driver.close()