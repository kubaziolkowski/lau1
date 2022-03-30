from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

import time

driver = webdriver.Chrome('/Users/kuba/desktop/chromedriver')

driver.get("https://strefainwestorow.pl/")
time.sleep(3)

print('Sprawdzam rekomendowane spolki z GPW w Warszawie')
try:
    rekomendacje = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Rekomendacje"))
    )
    rekomendacje.click()

except:
    driver.quit()

time.sleep(5)
print('Sprawdzam notowanie oraz najnowsze informacje dot. spolki Ten Square Games')

search_box = driver.find_element_by_name("search")
    
search_box.send_keys('Ten Square Games')

search_box.send_keys(Keys.RETURN)

time.sleep(5)
print('Sprawdzam, czy zmienili sie udzialowcy lub tez czy obecni dokupili/odsprzedali akcje')

try:
    akcjonariat = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Akcjonariat"))
    )
    akcjonariat.click()

except:
    driver.quit()

time.sleep(3)

driver.back()
driver.back()
driver.back()







