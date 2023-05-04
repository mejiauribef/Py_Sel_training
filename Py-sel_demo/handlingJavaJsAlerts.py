from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://www.rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys("Felipe  M.")
driver.find_element_by_id("alertbtn").click()
alerts = driver.switch_to.alert
print(alerts.text) #gets text
alerts.accept()  #positive option
alerts.dismiss() #negative option

driver.close()


