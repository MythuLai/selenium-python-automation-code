import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class DemoScreenshot():
    def demo_screen_capture(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        continue_demo = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        continue_demo.screenshot(".\\test.png")     # . current project pwd
        continue_demo.click()
        time.sleep(4)
        driver.get_screenshot_as_file("C:\\python-selenium\\error.png")
        driver.save_screenshot(".\\test1.png")



dddemo = DemoScreenshot()
dddemo.demo_screen_capture()