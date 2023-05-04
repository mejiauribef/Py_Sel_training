from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://www.Google.com")
driver.find_element_by_css_selector("input.gLFyf.gsfi").send_keys("Quien es el duro para TA ")
driver.find_element_by_css_selector("input.gLFyf.gsfi").send_keys(Keys.RETURN)
text_result = driver.find_element_by_css_selector("h3.LC20lb.MBeuO.MMgsKf").text


if text_result == "Daddy Yankee - Dura (Video Oficial) - YouTube":
    text_result = driver.find_element_by_css_selector("h3.LC20lb.MBeuO.MMgsKf").click()




driver.close()


