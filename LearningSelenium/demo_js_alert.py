import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoJsPopup():
    def demo_js_alert(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")

        # Accept alert
        # driver.find_element(By.XPATH, "//button[contains(text(),'Try it')]").click()
        # time.sleep(2)
        # driver.switch_to.alert.accept()
        # time.sleep(2)

        # dismiss alert
        driver.find_element(By.XPATH, "//button[contains(text(),'Try it')]").click()
        time.sleep(2)
        # Alert(driver).dismiss()
        driver.switch_to.alert.dismiss()
        time.sleep(2)

        # send text in alert
        driver.find_element(By.XPATH, "//button[contains(text(),'Try it')]").click()
        time.sleep(2)
        print(driver.switch_to.alert.text)  # display text in alert
        driver.switch_to.alert.send_keys("RCV Academy")
        driver.switch_to.alert.accept()




dpopup = DemoJsPopup()
dpopup.demo_js_alert()