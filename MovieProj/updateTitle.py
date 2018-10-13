import json, codecs, sys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

request_id = sys.argv[1]
link = sys.argv[2]

urls = []
rating = ''

driver = webdriver.Chrome()
driver.implicitly_wait(1)
wait = WebDriverWait(driver, 1)

urls.append(link)

for url in urls:
    driver.get(url)
    timeout = 1
    try:
        element = EC.presence_of_element_located((By.XPATH, '//*[@id="tomato_meter_link"]/span[2]/span'))
        WebDriverWait(driver, timeout).until(element)
    except:
        print ('Timeout')
    element = driver.find_element_by_xpath('//*[@id="tomato_meter_link"]/span[2]/span')
    rating = element.text + '%'

driver.quit()
file = open('r'+request_id+'.txt', 'w')
file.write(rating)
file.close()