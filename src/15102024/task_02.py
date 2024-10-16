from selenium import webdriver
import pytest
import allure


@allure.title("Verify the Katalon demo Home page")
def test_Katalon_Home():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print(driver.title)
    assert driver.title == "CURA Healthcare Service"
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    assert driver.page_source.__contains__("CURA Healthcare Service")