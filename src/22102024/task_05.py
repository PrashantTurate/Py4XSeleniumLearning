import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


@allure.title("Print the Titles & respective Prices together")
@allure.description("Verify that 62 items are there for macmini")
def test_eBayApp_verify_title_prices():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    driver.maximize_window()

    search_box_input_xpath = driver.find_element(By.XPATH, "//input[@placeholder='Search for anything']")
    # search_box_inout_css = driver.find_element(By.CSS_SELECTOR,"#gh-ac")
    search_box_input_xpath.send_keys("macmini")

    search_box_button = driver.find_element(By.CSS_SELECTOR, "input[value='Search']")
    search_box_button.click()

    list_of_items = driver.find_elements(By.CSS_SELECTOR, ".s-item__title")
    list_of_items_price = driver.find_elements(By.CSS_SELECTOR, ".s-item__price")

    assert len(list_of_items) == 62
    print("Total number of items: ", len(list_of_items))

    # for val in list_of_items:
    #    print(val.text,end="||")
    # for val in list_of_items_price:
    #    print(val.text,end="||")

    for title, price in zip(list_of_items, list_of_items_price):
        title_value = title.text
        price_value = price.text
        print(f"Title:{title_value},Price:{price_value}")

    time.sleep(5)
    driver.quit()