from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random
import time


driver = webdriver.Chrome()
driver.implicitly_wait(10)
time.sleep(2)

url = "http://demostore.supersqa.com/my-account/"
email_field_id = "reg_email"
password_field_Id = "reg_password"
logout_bnt_css = "#post-9 > div > div > nav > ul > li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a"


# go to url
driver.get(url)
email_field = driver.find_element(By.ID, email_field_id)


# generate random email
letters = string.ascii_lowercase
rand_string = ''.join(random.choice(letters) for i in range(15))
random_email = rand_string + '@gmail.com'


# type in the email field
email_field.send_keys(random_email)

# find password field and enter password
password_field = driver.find_element(By.ID, password_field_Id)
password_field.send_keys("Okolie92/")
time.sleep(2)

register_button = driver.find_element(By.CSS_SELECTOR, "#customer_login > div.u-column2.col-2 > form > p:nth-child(4) > button")
register_button.click()
time.sleep(2)

try:
    logout_bnt = driver.find_element(By.CSS_SELECTOR, logout_bnt_css)
except:
    raise Exception("User not logged in after registering.")

if logout_bnt.is_displayed():
    print("PASS.")
else:
    raise Exception("User not logged in after registering.")




