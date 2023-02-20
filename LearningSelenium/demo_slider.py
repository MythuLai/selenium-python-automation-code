import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoSliders():
    def demo_slide(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.snapdeal.com/products/mobiles-screen-guards?sort=plrty")
        driver.maximize_window()

        #find locator for left and right sliders
        elem1 = driver.find_element(By.XPATH, "//a[contains(@class,'left-handle')]")
        elem2 = driver.find_element(By.XPATH, "//a[contains(@class,'right-handle')]")

        #move to the right for elem1
        # ActionChains(driver).drag_and_drop_by_offset(elem1, 80 ,0).perform()
        #ActionChains(driver).click_and_hold(elem1).pause(1).move_by_offset(60,0).release().perform()
        # ActionChains(driver).move_to_element(elem1).pause(1).click_and_hold(elem1).move_by_offset(70,0).release().perform()
        # time.sleep(4)

        # #move to the left for elem2
        # ActionChains(driver).drag_and_drop_by_offset(elem2, -80, 0).perform()
        # time.sleep(3)

        # move to the both left right elem2
        ActionChains(driver).drag_and_drop_by_offset(elem1, 60, 0).perform()
        # time.sleep(3)
        ActionChains(driver).drag_and_drop_by_offset(elem2, -80, 0).perform()
        # time.sleep(3)


dclick = DemoSliders()
dclick.demo_slide()