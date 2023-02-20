import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoFindWebelementState():
    def demo_find_state(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://training.openspan.com/login")
        demo_state = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(demo_state)

        demo_state = driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("test")
        # time.sleep(2)
        demo_state = driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("testing")
        # time.sleep(2)
        demo_state1 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(demo_state1)




findstate = DemoFindWebelementState()
findstate.demo_find_state()
