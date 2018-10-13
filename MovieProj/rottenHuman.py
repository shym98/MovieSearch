import json

import scrapy, codecs
import csv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(1)
wait = WebDriverWait(driver, 1)
result = []
def scrapH(request_id):
    urls = []
    links = []
    file = codecs.open('names' + str(request_id) + '.txt', 'r', 'utf-8')
    for line in list(set(file.readlines())):
        urls.append('https://www.rottentomatoes.com/search/?search=' + line)
    for url in urls:
        driver.get(url)
        try:
            driver.find_element_by_link_text("More Celebrities...").click()
        except:
            continue
        for i in range(1, 11000):
            timeout = 1
            try:
                element = EC.text_to_be_present_in_element((By.XPATH, '//*[@id="PartialResults"]/nav[1]/span'),
                                                           str(i) + " of ")
                WebDriverWait(driver, timeout).until(element)
                severalPages = True
            except:
                severalPages = False
            results = driver.find_elements_by_xpath('//*[@id="PartialResults"]/ul/li/div/div/a')
            for rows in results:
                link = rows.get_attribute('href')
                links.append(link)
            for link in links:
                parseCeleb(link)
            if not severalPages:
                break
            try:
                driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(
                    '//*[@id="PartialResults"]/nav[1]/button[2]'))
            except:
                print('error')
    driver.quit()
    with open("h" + str(request_id) + ".json", "w") as outfile:
        json.dump(result, outfile, indent=4)

def parseCeleb(url):
    driver.get(url)
    try:
            name = driver.find_element_by_xpath('//*[@id="main_container"]/div[1]/div[1]/section/div/div[1]/h1').text
    except:
            name = None
    try:
            photo = driver.find_element_by_xpath(
                '//*[@id="main_container"]/div[1]/div[1]/section/div/div[2]/a/div').get_attribute('style')[23:-3]
    except:
            photo = None
    try:
            highestRating = driver.find_element_by_xpath(
                '//*[@id="main_container"]/div[1]/div[1]/section/div/div[3]/div[1]/a/span').text
    except:
            highestRating = None
    try:
            lowestRating = driver.find_element_by_xpath(
                '//*[@id="main_container"]/div[1]/div[1]/section/div/div[3]/div[2]/a/span').text
    except:
            lowestRating = None
    try:
            birthday = str(driver.find_element_by_xpath(
                '//*[@id="main_container"]/div[1]/div[1]/section/div/div[3]/div[3]/time').get_attribute('datetime'))[
                       0:10]
    except:
            birthday = None
    try:
            bio = driver.find_element_by_xpath(
                '//*[@id="main_container"]/div[1]/div[1]/section/div/div[3]/div[5]').text
    except:
            bio = None
    result.append({"name": name,
               "photo": photo,
               "highestRating": highestRating,
               "lowestRating": lowestRating,
               "birthday": birthday,
               "bio": bio,
               "rottenLink": url})
