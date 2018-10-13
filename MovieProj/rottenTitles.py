import json, codecs
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def scap(request_id):

    urls = []

    result = []

    driver = webdriver.Chrome()
    driver.implicitly_wait(1)
    wait = WebDriverWait(driver, 1)

    file = codecs.open('titles' + str(request_id) + '.txt', 'r', 'utf-8')
    for line in file.readlines():
        urls.append('https://www.rottentomatoes.com/search/?search=' + line)

    for url in urls:
        driver.get(url)
        isMovie = True
        timeout = 1
        try:
            element = EC.presence_of_element_located((By.ID, 'Search Results'))
            WebDriverWait(driver, timeout).until(element)
            driver.find_element_by_link_text("More Movies...").click()
        except:
            print ('Timeout')
            continue
        tvPages = 1
        for i in range(1, 11000):
            try:
                if isMovie:
                    element = EC.text_to_be_present_in_element((By.XPATH, '//*[@id="PartialResults"]/nav[1]/span'), str(i) + " of ")
                else:
                    element = EC.text_to_be_present_in_element((By.XPATH, '//*[@id="PartialResults"]/nav[1]/span'), str(tvPages) + " of ")
                WebDriverWait(driver, timeout).until(element)
                severalPages = True
                if i > 3:
                    if isMovie:
                        isMovie = False
                        driver.execute_script("arguments[0].click();", driver.find_element_by_xpath('//*[@id="filterList"]/li[1]/span'))
                        try:
                            element = EC.presence_of_element_located((By.ID, 'tvSeriesSection'))
                            WebDriverWait(driver, timeout).until(element)
                            driver.find_element_by_link_text("More TV...").click()
                            i = 0
                            continue
                        except TimeoutException:
                            print ('Timeout')
                            break
                    else:
                        if tvPages > 3:
                            break
            except:
                severalPages = False
            table = zip((driver.find_elements_by_xpath('//*[@id="PartialResults"]/ul/li/div[3]/span[1]/a'), driver.find_elements_by_xpath('//*[@id="PartialResults"]/ul/li/div[3]/a'))[not isMovie],
                        (driver.find_elements_by_xpath('//*[@id="PartialResults"]/ul/li/div[3]/span[2]'),driver.find_elements_by_xpath('//*[@id="PartialResults"]/ul/li/div[3]/span'))[not isMovie],
                        driver.find_elements_by_xpath('//*[@id="PartialResults"]/ul/li/div[1]/span[1]'))
            if isMovie: rat = driver.find_elements_by_xpath('//*[@id="PartialResults"]/ul/li/div[1]/span[2]')
            else :
                rat = driver.find_elements_by_xpath('//*[@id="PartialResults"]/ul/li/div[1]/span/span[2]')
            cur = 0
            for rows in table:
                if rows[2].get_attribute("class") != 'tMeterIcon tiny noRating':
                    result.append( {"name" : rows[0].text, "year": (rows[1].text[2:-1][1:],rows[1].text[2:-1])[isMovie], "rating": rat[cur].text, "link": rows[0].get_attribute('href')})
                    cur += 1
                else:
                    result.append( {"name" : rows[0].text, "year": rows[1].text[2:-1], "rating": 'No Score Yet', "link": rows[0].get_attribute('href')})

            if not severalPages or (severalPages and driver.find_element_by_xpath('//*[@id="PartialResults"]/nav[1]/button[2]').get_attribute("class") == 'left btn btn-primary-rt btn-xs disabled'):
                if not isMovie:
                    break
                isMovie = False
                driver.execute_script("arguments[0].click();", driver.find_element_by_xpath('//*[@id="filterList"]/li[1]/span'))
                try:
                    element = EC.presence_of_element_located((By.ID, 'tvSeriesSection'))
                    WebDriverWait(driver, timeout).until(element)
                    driver.find_element_by_link_text("More TV...").click()
                except TimeoutException:
                    print ('Timeout')
                    break
            if severalPages:
                try:
                    if not isMovie:
                        tvPages += 1
                    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath('//*[@id="PartialResults"]/nav[1]/button[2]'))
                except:
                    print("Error")

    driver.quit()

    with open("r" + str(request_id) + ".json", "w") as outfile:
            json.dump(result, outfile, indent=4)