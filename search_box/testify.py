import time
import pdb
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def login_page(element, *keys):
    element.send_keys(keys)

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.testifyltd.com/")
    driver.maximize_window()
    driver.implicitly_wait(12)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")



if __name__ == '__main__':
    main()
