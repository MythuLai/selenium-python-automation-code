import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoRightDoubleClick():
    def demo_right_double(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()

        #right click
        act_chains = ActionChains(driver)
        # elem1 = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        # copyelem = driver.find_element(By.XPATH, "//span[normalize-space()='Copy']")
        # act_chains.context_click(elem1).perform()
        # time.sleep(3)
        # copyelem.click()

        #double click
        elem2 = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        act_chains.double_click(elem2).perform()
        time.sleep(5)





dclick = DemoRightDoubleClick()
dclick.demo_right_double()