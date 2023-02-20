import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoMouseOver():
    def demo_mouse_over(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()

        #create an obj of class ActionChains
        act_chains = ActionChains(driver)

        # morebutton = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        # act_chains.move_to_element(morebutton).perform()
        # time.sleep(3)
        # driver.find_element(By.XPATH, "//span[normalize-space()='Xplore']").click()
        # time.sleep(3)

        #for login
        acctbutton = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
        act_chains.move_to_element(acctbutton).perform()
        driver.find_element(By.XPATH, "//a[@id='signInBtn']").click()
        time.sleep(3)


dmouse = DemoMouseOver()
dmouse.demo_mouse_over()