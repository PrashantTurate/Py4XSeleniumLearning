import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("SVG")
@allure.description("Verify svg")
def test_verify_svg():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()

    #name() or local-name()

    list_of_states = (driver.find_elements(
        By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']"))

    for state in list_of_states:
        print(state.get_attribute("aria-label"))
        if "Maharashtra" in state.get_attribute("aria-label"):
            state.click()
            break

    time.sleep(5)