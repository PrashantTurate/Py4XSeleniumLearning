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


@allure.title("Drag&Drop")
@allure.description("Verify drag and drop actions")
def test_verify_drag_drop():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    driver.maximize_window()

    element_to_drag = driver.find_element(By.ID, "draggable")
    element_to_drop = driver.find_element(By.ID, "droppable")

    time.sleep(2)

    actions = ActionChains(driver)
    actions.click_and_hold(on_element=element_to_drop).perform()
    time.sleep(3)
    actions.drag_and_drop(element_to_drag, element_to_drop).perform()


    time.sleep(5)
    driver.quit()
