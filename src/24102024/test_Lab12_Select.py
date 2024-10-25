import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("Select")
@allure.description("Verify Select dropdown")
def test_select_dropdown():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")
    driver.maximize_window()

    dropdown = driver.find_element(By.ID, "dropdown")
    s1 = Select(dropdown)
    time.sleep(2)
    s1.select_by_visible_text("Option 2")
    time.sleep(2)
    s1.select_by_index(1)


    time.sleep(5)