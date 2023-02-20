import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        # driver.find_element(By.TAG_NAME, 'input').send_keys('test@test.com')
        lista = driver.find_elements(By.TAG_NAME, 'a')
        print(len(lista))
        for i in lista:
            print(i.text)

        time.sleep(4)




findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()