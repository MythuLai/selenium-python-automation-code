import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoGetText():
    def demo_gettext(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com")
        result = driver.find_element(By.XPATH, "//*[contains(text() , 'Yatra for Business')]").text
        print(result)
        time.sleep(4)




findbyid = DemoGetText()
findbyid.demo_gettext()