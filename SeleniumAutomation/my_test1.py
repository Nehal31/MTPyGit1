
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "http://www.google.com/"

def main():

    # get the path of ChromeDriverServer
    dir = os.path.dirname(__file__)
    chrome_driver_path = dir + "chromedriver.exe"
    print("Chrome driver : " + chrome_driver_path)

    driver = webdriver.Chrome(chrome_driver_path)
    driver.implicitly_wait(30)
    driver.maximize_window()

    driver.get(URL)

    print(driver)

    driver.quit()

if __name__ == '__main__':
    main()
