import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoImplicitWait():
    def demo_imp_wait(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(19)
        driver.get("https://login.salesforce.com/")
        driver.maximize_window()
        driver.find_element(By.ID, "username").send_keys("RCV Academy")
        driver.find_element(By.ID, "password").send_keys("RCV Academy")


impwait = DemoImplicitWait()
impwait.demo_imp_wait()

