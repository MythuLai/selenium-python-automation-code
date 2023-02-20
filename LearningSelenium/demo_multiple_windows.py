import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoMultiWindows():
    def demo_multi_wins(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        parent_handle = driver.current_window_handle
        driver.find_element(By.XPATH, "//a[normalize-space()='View All']").click()
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                chlid_handle = driver.find_element(By.XPATH, "//span[contains(text(),'Flat 16% OFF (up to Rs. 2,000)')]").click()
                time.sleep(4)
                driver.close()
                time.sleep(3)
                break

        driver.switch_to.window(parent_handle)
        driver.find_element(By.XPATH, "//a[normalize-space()='View All']").click()  


        time.sleep(3)





dddemo = DemoMultiWindows()
dddemo.demo_multi_wins()