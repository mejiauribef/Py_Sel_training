import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

list = []
comparer = []
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://first-pagefly-trial.myshopify.com/collections/fruits")


# Selecting the add to cart buttons
buttons = driver.find_elements_by_xpath("//button[@data-pf-type='ProductATC']")

# ATC for all buttons
for button in buttons:
    # Going up as we are on a child and need to go to parent twice and then go down to h3 (product name)
    # And append to new position of list to save the name of all products
    list.append(button.find_element_by_xpath("parent::div/h3[@data-pf-type='ProductTitle']").text)
    button.click()
    time.sleep(0.5)


driver.find_element_by_css_selector("button.cart-popup__close").click()
time.sleep(1)
# Open cart and proceed to checkout
driver.find_element_by_css_selector("a.site-header__icon.site-header__cart").click()


# Grab new list of product names on cart
compa = driver.find_elements_by_css_selector("a.cart__product-title")
for com in compa:
    comparer.append(com.text)

comparer.reverse()
# Verify if both lists have the same lenght
assert list == comparer


# Proceed to checkout
driver.find_element_by_class_name("cart__submit").click()



driver.close()