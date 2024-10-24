import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


@allure.title("Verify the registration page")
@allure.description("Verify the user is able to register")
def test_verify_registration_page():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    driver.maximize_window()

    first_name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
    first_name.send_keys("Amit")
    time.sleep(2)
    last_name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
    last_name.send_keys("Sharma")
    time.sleep(2)
    email = driver.find_element(By.XPATH, "//input[@name='email']")
    email.send_keys("amit.sharma@xyz.com")
    time.sleep(2)
    contact_number = driver.find_element(By.XPATH, "//input[@id='input-telephone']")
    contact_number.send_keys("9923455609")
    time.sleep(2)

    password = driver.find_element(By.ID, "input-password")
    password.send_keys("abcd1234")
    time.sleep(2)
    confirm_password = driver.find_element(By.ID, "input-confirm")
    confirm_password.send_keys("abcd1234")

    subscribe_nl = driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']")
    subscribe_nl.click()
    time.sleep(2)
    agree_policy = driver.find_element(By.XPATH, "//input[@name='agree']")
    agree_policy.click()
    time.sleep(2)

    submit = driver.find_element(By.XPATH, "//input[@value='Continue']")
    submit.click()
    time.sleep(3)

    print("After Registration URL: ", driver.current_url)
    assert driver.current_url == ("https://awesomeqa.com/ui/index.php?route=account/success")


    expected_message = "Your Account Has Been Created!"
    actual_message = driver.find_element(By.TAG_NAME, "h1").text
    assert expected_message == actual_message
    print(actual_message)

    time.sleep(5)
    driver.quit()
