import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Alerts")
@allure.description("Verify Alerts")
def test_alerts_js_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_alert = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    element_alert.click()

    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()

    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You successfully clicked an alert"
    print(result_text)

    time.sleep(5)


def test_alerts_confirm():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    element_confirm.click()

    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    #alert.accept()
    alert.dismiss()

    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You clicked: Cancel"
    print(result_text)

    time.sleep(5)


def test_alerts_prompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    element_prompt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    element_prompt.click()

    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.send_keys("Pramod")

    alert.accept()
    # alert.dismiss()

    result_text = driver.find_element(By.ID, "result").text
    assert result_text == "You entered: Pramod"
    print(result_text)

    time.sleep(5)