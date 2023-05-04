from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")

# Clink link text to open new window
driver.find_element_by_partial_link_text("Click Here").click()

# Get all the windows open by automation 
parentWindowId = driver.window_handles[0] #position 1 of array for parent
childWindowId = driver.window_handles[1]  #position 2 of array for child

# We need to switch to the new window to have effect on it
driver.switch_to.window(childWindowId)
print(driver.find_element_by_tag_name("h3").text)
# After text copy we close new window
driver.close()
driver.switch_to.window(parentWindowId)
print(driver.find_element_by_tag_name("h3").text)
