from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class MainFile():
    def testweb(self):
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
        time.sleep(1)

        for _ in range(1):
            btnAdElement = driver.find_element(By.XPATH, "//button[normalize-space()='Add Element']")
            # clicking on the button
            btnAdElement.click()
            time.sleep(1)  # Adding a small delay between clicks

        time.sleep(1)

        btndlt = driver.find_elements(By.XPATH, "//button[normalize-space()='Delete']")
        # Clicking on the Delete buttons for all added elements
        for btn in btndlt:
            btn.click()
            time.sleep(1)  # Adding a small delay between clicks

        driver.quit()


myfunc = MainFile()
myfunc.testweb()

##changes

