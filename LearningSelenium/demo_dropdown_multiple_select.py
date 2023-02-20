import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


class DemoDropDownMultiSelect():
    def demo_dropdown_multi(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://skryabin.com/market/quote.html")
        driver.maximize_window()

        dropdwn = driver.find_element(By.NAME, "carMake")

        dd_multi = Select(dropdwn)

        dd_multi.select_by_index(0)

        dd_multi.select_by_value("BMW")

        dd_multi.select_by_visible_text("Toyota")
        # time.sleep(4)

        dd_multi.deselect_by_index(0)
        # time.sleep(4)
        dd_multi.deselect_by_value("BMW")
        # time.sleep(3)
        dd_multi.deselect_all()






dddemo = DemoDropDownMultiSelect()
dddemo.demo_dropdown_multi()