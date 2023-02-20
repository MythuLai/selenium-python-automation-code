import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoIFrame():
    def demo_iframe(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        # find parent_iframe switch with iframe locator
        #driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
        # switch with ID
        # driver.switch_to.frame("iframeResult")
        # switch with name
        # driver.switch_to.frame("iframeResult")
        # # switch with index
        # driver.switch_to.frame(0)
        # driver.find_element(By.XPATH, "//a[@id='navbtn_menu']").click()
        # time.sleep(4)

        driver.switch_to.frame("iframeResult")
        driver.switch_to.frame(1)
        driver.find_element(By.XPATH, "//a[@title='Add JavaScript Certification']").click()
        time.sleep(4)





dm_iframe = DemoIFrame()
dm_iframe.demo_iframe()