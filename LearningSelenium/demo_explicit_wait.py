import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class DemoExplicitWait():
    def demo_exp_wait(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10, 2, ignored_exceptions=[ElementClickInterceptedException])

        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        wait.until(EC.element_to_be_clickable(depart_from)).click()
        # depart_from.click()
        # driver.implicitly_wait(4)
        depart_from.send_keys("New Delhi")
        # wait.until(EC.presence_of_all_elements_located(depart_from)).send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)
        time.sleep(4)

        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")

        # print(len(search_results))
        for result in search_results:
            # print(result.text)
            if "New York (JFK)" in result.text:
                result.click()
                time.sleep(8)
                break   #out of loop

        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        #choose date by hard code
        # origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        # origin.click()


        # by logic framework
        # all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class !='inActiveTD']")
        # all_dates = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='day-container']//tbody//td[@class != 'inActiveTD']" )))\
        #     .find_elements(By.XPATH, "//div[@class='day-container']//tbody//td[@class != 'inActiveTD']" )
        # # all_dates = driver.find_elements(By.XPATH, "//div[@class='day-container']//tbody//td[@class != 'inActiveTD']")
        # for date in all_dates:
        #     if date.get_attribute("data-date") == "27/02/2023":
        #         date.click()
        #         time.sleep(4)
        #         break
        #
        # driver.find_element(By.XPATH, "//input[@value = 'Search Flights']").click()
        #
        #


expwait = DemoExplicitWait()
expwait.demo_exp_wait()
