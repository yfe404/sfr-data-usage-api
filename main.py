import io
import os
import sys
import json
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

MAIN_URL="https://www.sfr.fr/cas/login"

def wait_element(driver, elem_info, timeout=10, message="Error"):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(elem_info)
        )
        return element 
    except Exception as err:
        driver.quit()
        print(err, file=sys.stderr)


if __name__ == "__main__":
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(MAIN_URL)

    _klass = "R"
    elem_info = (By.CLASS_NAME, _klass)
    element = wait_element(driver, elem_info)
    element.click()
    
    _id = "username"
    elem_info = (By.ID, _id)
    element = wait_element(driver, elem_info)
    element.send_keys(os.environ.get("USERNAME"))

    _id = "password"
    elem_info = (By.ID, _id)
    element = wait_element(driver, elem_info)
    element.send_keys(os.environ.get("PASSWORD"))

    time.sleep(1)
    element.send_keys(Keys.RETURN)

    xpath = "/html/body/header/nav[5]/ul/li[9]/a"
    elem_info = (By.XPATH, xpath)
    element = wait_element(driver, elem_info)
    time.sleep(2)
    element.click()

    xpath = "/html/body/header/nav[5]/ul/li[4]/a"
    elem_info = (By.XPATH, xpath)
    element = wait_element(driver, elem_info)
    time.sleep(2)
    element.click()

    xpath = "/html/body/div/div/div/div[2]/app-root/acceuil-component-bloc/div/div[3]/app-reinitialisation-forfait/div/div[1]"
    elem_info = (By.XPATH, xpath)
    element = wait_element(driver, elem_info)
    print(f"Next reset: {element.text}")

    xpath = "/html/body/div/div/div/div[2]/app-root/acceuil-component-bloc/div/div[3]/div[2]/app-en-france/section/div[2]/div[1]/div[1]/div[2]/p"
    elem_info = (By.XPATH, xpath)
    element = wait_element(driver, elem_info)
    print(f"Usage: {element.text}")

    driver.quit()
