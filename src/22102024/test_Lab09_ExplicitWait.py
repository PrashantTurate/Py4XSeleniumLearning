import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("App.vwo.com - Explicit Wait")
@allure.description("Verify that App.vwo.com - Explicit Wait")
def test_verify_ExplicitWait():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()

    # driver.implicitly_wait(5) # Automation - 0.01% -

    email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element.send_keys("abc@gmail.com")

    password_web_element = driver.find_element(By.NAME, "password")
    password_web_element.send_keys("password@1234")

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    (WebDriverWait(driver=driver, timeout=5)
     .until(EC.visibility_of_element_located((By.CLASS_NAME, "notification-box-description"))))

    # A Condition to check the element
    # error_msg_element - comes after 5 seconds
    # I have to wait with some condition -
    # wait with the condition
    # Add a condition so that Webdriver should wait for that condition.
    # element is visible then assertion

    # Smart Logic to wait for the element
    # Condition based Logic

    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"

    driver.quit()