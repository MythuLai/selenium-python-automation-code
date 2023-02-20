import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoAutoSuggest():
    def demo_autosuggest_dropdown(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(2)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(4)

        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")

        print(len(search_results))
        for result in search_results:
            # print(result.text)
            if "New York (JFK)" in result.text:
                result.click()
                time.sleep(8)
                break   #out of loop

        #choose date by hard code
        origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        origin.click()
        time.sleep(4)
        # driver.find_element(By.XPATH, "//td[@id='21/02/2023']").click()
        # time.sleep(4)

        # by logic framework
        # all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class !='inActiveTD']")
        all_dates = driver.find_elements(By.XPATH, "//div[@class='day-container']//tbody//td[@class != 'inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "27/02/2023":
                date.click()
                time.sleep(4)
                break

        driver.find_element(By.XPATH, "//input[@value = 'Search Flights']").click()



dddemo = DemoAutoSuggest()
dddemo.demo_autosuggest_dropdown()