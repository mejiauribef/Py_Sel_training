import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://www.rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
lengthCountries = len(countries)
for country in countries:
    if country.text == "India":
        country.click()
        break

assert "India" == driver.find_element_by_id("autosuggest").get_attribute('value')


driver.close()
