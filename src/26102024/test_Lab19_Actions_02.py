import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton


@allure.title("Actions Builder P2")
@allure.description("Verify MouseBack activity")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    driver.maximize_window()

    time.sleep(2)

    click_results = driver.find_element(By.ID, "click")
    click_results.click()

    time.sleep(2)

    # KEY_DOWN
    actions_builders = ActionBuilder(driver=driver)
    actions_builders.pointer_action.pointer_up(MouseButton.BACK)
    actions_builders.perform()
    time.sleep(3)
    actions_builders.pointer_action.pointer_up(MouseButton.FORWARD)
    actions_builders.perform()


    time.sleep(5)
    driver.quit()
