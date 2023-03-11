from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random
import time



class InvalidUserLoginError:

    url = 'https://web.facebook.com/login/'
    invalid_email = 'abc@supersqa.com'
    valid_email = "henryokolie615@gmail.com"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def go_to_my_account(self):
        self.driver.get(self.url)

    def input_email(self):
        field = self.driver.find_element(By.ID, 'email')
        field.send_keys(self.invalid_email)
        time.sleep(2)

    def input_password(self):
        field = self.driver.find_element(By.ID, 'pass')
        field.send_keys('kjblkjliou')

    def click_login(self):
        self.driver.find_element(By.ID, 'loginbutton').click()
        time.sleep(2)

    def forget_password(self):
        self.driver.find_element(By.CSS_SELECTOR, "#login_link > div > a").click()
        time.sleep(2)


    def inputs_mails(self):
        field = self.driver.find_element(By.CSS_SELECTOR, "#identify_email")
        field.send_keys(self.valid_email)
        time.sleep(2)

    def click_search(self):
        self.driver.find_element(By.NAME, "did_submit").click()
        time.sleep(2)

    def click_continue(self):
            self.driver.find_element(By.NAME, "reset_action").click()
            time.sleep(10)



    def main(self):
        self.go_to_my_account()
        self.input_email()
        self.input_password()
        self.click_login()
        self.forget_password()
        self.inputs_mails()
        self.click_search()
        self.click_continue()
        self.driver.quit()

if __name__ == '__main__':

    obj = InvalidUserLoginError()
    obj.main()