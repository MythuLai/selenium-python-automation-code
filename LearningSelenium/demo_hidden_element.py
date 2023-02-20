import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoHiddenElement():
    def demo_is_displayed(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        elem = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem)
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()
        elem1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem1)


    def demo_is_displayed_yatra(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/hotels")
        driver.find_element(By.XPATH, "//label[normalize-space()='Traveller and Hotel']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div//span[2]").click()
        time.sleep(2)
        elem = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        print(elem)

        try:
            driver.find_element(By.XPATH, "//span[@class='ddSpinnerMinus disabled']").click()
            elem2 = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
            print(elem2)
        except Exception as e:
            print(e)






demo_display = DemoHiddenElement()
# demo_display.demo_is_displayed()
demo_display.demo_is_displayed_yatra()