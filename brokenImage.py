import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set the path to the ChromeDriver executable

# Set the URL with basic authentication
url_with_auth = "https://the-internet.herokuapp.com/broken_images"
driver = webdriver.Chrome()

driver = webdriver.Chrome()
driver.get(url_with_auth)
# Find all image elements using a CSS selector
image_elements = driver.find_elements(By.CSS_SELECTOR, 'img')
for img in image_elements:
        src = img.get_attribute('src')
        response = requests.get(src)

        if response.status_code != 200:
            print("Broken image found:", src)
driver.quit()

'''
driver.find_elements(By.CSS_SELECTOR, 'img') finds all <img> elements on the page using a CSS selector.
The loop iterates through each image element and does the following:
img.get_attribute('src') retrieves the value of the src attribute of the image element.
requests.get(src) sends an HTTP GET request to the image URL.
response.status_code retrieves the HTTP status code returned by the request.
If the status code is not 200, it indicates a broken image, and the image URL is printed.
'''
