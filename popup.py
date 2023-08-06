# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# "Authentication pop up can not be handled by using any locators in selenium."
# "We need to pass username:password pair in application URL."
#
#
# driver = webdriver.Chrome()
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
#
# time.sleep(2)
#
# driver.quit()
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path to the ChromeDriver executable

# Set the URL with basic authentication
url_with_auth = "http://admin:admin@the-internet.herokuapp.com/basic_auth"

# Configure ChromeDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome()

try:
    # Open the URL with basic authentication
    driver.get(url_with_auth)
    time.sleep(2)
    # Find and print the page message
    page_message = driver.find_element(By.CSS_SELECTOR, "p").text
    print(page_message)

finally:
    # Close the browser window
    driver.quit()

#


