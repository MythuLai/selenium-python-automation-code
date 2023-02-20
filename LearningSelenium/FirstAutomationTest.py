import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver = webdriver.Chrome(ChromeDriverManager().install())
# # driver = webdriver.Edge(EdgeChromiumDriverManager().install())
#
# # driver = webdriver.Firefox(executable_path="C:\\browserDrivers\\geckodriver.exe")
# driver.get("https://www.rcvacademy.com")
# driver.maximize_window()
# print(driver.title)
# driver.close()

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.ID, 'login-input').send_keys('test@test.com')
        time.sleep(4)



findbyid= DemoFindElementByID()
findbyid.locate_by_id_demo()