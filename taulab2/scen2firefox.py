from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

import time

driver = webdriver.Firefox('/Users/kuba/desktop/chromedriver')

driver.get("https://www.plemiona.pl/")
time.sleep(3)

print('Wchodzę w link w celu utworzenia konta')
try:
    make_account = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Bezpłatna rejestracja!"))
    )
    make_account.click()

except:
    driver.quit()

time.sleep(3)

user_box = driver.find_element_by_id("register_username")
user_box.send_keys('darthvader42069')

time.sleep(3)

password_box = driver.find_element_by_id("register_password")
password_box.send_keys('Fs45!fAH763DdJ')

time.sleep(3)

email_box = driver.find_element_by_id("register_email")
email_box.send_keys('bababababa@wp.pl')

time.sleep(3)

try:
    make_account2 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Stwórz konto"))
    )
    make_account2.click()

except:
    driver.quit()

time.sleep(3)
