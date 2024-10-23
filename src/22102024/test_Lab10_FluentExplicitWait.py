import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)


@allure.title("App.vwo.com - Fluent Explicit Wait")
@allure.description("Verify that App.vwo.com - Fluent Explicit Wait")
def test_verify_Fluent_Explicit_Wait():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()

    email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element.send_keys("abc@gmail.com")

    password_web_element = driver.find_element(By.NAME, "password")
    password_web_element.send_keys("password@1234")

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]

    # Fluent Wait
    (WebDriverWait(driver=driver, poll_frequency=1, timeout=5, ignored_exceptions=ignore_list)
    .until(EC.visibility_of_element_located((By.CLASS_NAME, "notification-box-description"))))

    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"

    driver.quit()