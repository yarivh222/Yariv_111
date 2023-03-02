"""
Hi,
About Selenium exercise,
Please note that I used few websites to get the code and has gap (/time limitation) to perform it e2e by myself

I know how to perform the exercise in Load Runner (or Jmeter), its basic web recording.
However below I added the code and also can explain it, still code found in few websites

Asnwer#2(1)
The Implicit Wait in Selenium is used to tell the web driver to wait for a certain amount of time before it
throws a “No Such Element Exception”. The default setting is 0.

The Explicit Wait in Selenium is used to tell the Web Driver to wait for certain conditions
 (Expected Conditions) or maximum time exceeded before throwing “ElementNotVisibleException” exception
(https://www.guru99.com/implicit-explicit-waits-selenium.html#implicit-wait)

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# open webdriver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# load up to 10 sec for search
wait = WebDriverWait(driver, 10)
search_bar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.search-keyword")))

# 1st product seracr 3 products
search_bar.clear()
search_bar.send_keys("Cucumber")
search_results = driver.find_elements(By.CSS_SELECTOR, "div.product-action > button")
search_results[0].click()

search_bar.clear()
search_bar.send_keys("Beetroot")
search_results = driver.find_elements(By.CSS_SELECTOR, "div.product-action > button")
search_results[0].click()
search_bar.clear()
search_bar.send_keys("Carrot")
search_results = driver.find_elements(By.CSS_SELECTOR, "div.product-action > button")
search_results[0].click()

# Go to cart and proceed to checkout
cart = driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']")
cart.click()
proceed_to_checkout = driver.find_element(By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]")
proceed_to_checkout.click()

# Apply discount code and verify
discount_code = driver.find_element(By.CSS_SELECTOR, "input.promoCode")
discount_code.clear()
discount_code.send_keys("rahulshettyacademy")
apply_discount = driver.find_element(By.CSS_SELECTOR, "button.promoBtn")
apply_discount.click()

# Verify that the discount code is accepted
discount_applied = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.promoInfo"), "Code applied ..!"))
assert discount_applied
