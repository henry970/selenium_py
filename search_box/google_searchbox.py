
import time
import pdb
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def search_page(element, *keys):
    element.send_keys(keys)

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://www.google.com/")
    search_page(driver.find_element(By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input"), "cap")

    search = driver.find_element(By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b").click()
    print(search)
    pdb.set_trace()
    time.sleep(100)



if __name__ == '__main__':
    main()