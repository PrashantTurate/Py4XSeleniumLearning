from selenium import webdriver
import pytest
import allure

@allure.title("Veify the App VWO login page")
def test_sample():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"
