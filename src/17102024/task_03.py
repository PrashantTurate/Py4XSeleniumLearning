import time

from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By


@allure.title("Verify the Katalon Login")
def test_Katalon_LoginPage():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    make_appointment = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment.click()
    assert driver.current_url == ("https://katalon-demo-cura.herokuapp.com/profile.php#login")
    print("Login page URL: ",driver.current_url)
    username = driver.find_element(By.NAME, "username")
    username.send_keys("John Doe")
    time.sleep(2)
    password = driver.find_element(By.NAME, "password")
    password.send_keys("ThisIsNotAPassword")
    time.sleep(2)
    login = driver.find_element(By.ID,"btn-login").click()
    time.sleep(5)
    assert driver.current_url == ("https://katalon-demo-cura.herokuapp.com/#appointment")
    print("After Login Page URL: ",driver.current_url)
