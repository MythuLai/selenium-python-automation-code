# select_by_index(index)[source]
# Select the option at the given index. This is done by examining the “index” attribute of an element, and not merely by counting.
#
#
# select_by_value(value)[source]
# Select all options that have a value matching the argument. That is, when given “foo” this would select an option like:
#
#
# select_by_visible_text(text)[source]
# Select all options that display text matching the argument. That is, when given “Bar” this would select an option like:

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


class DemoDropDown():
    def demo_dropdown(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.salesforce.com/au/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        driver.maximize_window()
        dropdwn = driver.find_element(By.NAME, "UserTitle")

        ddselect = Select(dropdwn)

        ddselect.select_by_value("IT_Manager_AP")
        time.sleep(3)
        ddselect.select_by_index(3)
        time.sleep(3)
        ddselect.select_by_visible_text("Marketing / PR Manager")
        time.sleep(3)


dddemo = DemoDropDown()
dddemo.demo_dropdown()