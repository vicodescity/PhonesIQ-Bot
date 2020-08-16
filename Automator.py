from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
import Comments 
import lxml
import random

options = Options()
options.add_argument(f'user-agent={UserAgent().random}')
driver = webdriver.Chrome(chrome_options = options)

driver.get("https://www.phonesiq.com/login")

time.sleep(10)

driver.find_element_by_css_selector("#username").send_keys("")

time.sleep(3)

driver.find_element_by_css_selector("#password").send_keys("")

time.sleep(3)

driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[1]/div[3]/form/button").click()

time.sleep(10)

driver.get("https://www.phonesiq.com/news")

time.sleep(10)

with open("Links.txt", "r", encoding="utf-8") as file:

    for post in file.readlines():

        driver.get(post)

        time.sleep(15)

        comment = random.choice(Comments.comments)

        time.sleep(25)

        driver.find_element_by_css_selector("body > div.nk-main > div.container > div:nth-child(3) > div.col-lg-8 > div > div.nk-reply > form > textarea").send_keys(comment)

        time.sleep(10)

        driver.find_element_by_css_selector("body > div.nk-main > div.container > div:nth-child(3) > div.col-lg-8 > div > div.nk-reply > form > button").click()

        time.sleep(10)

        driver.back()

        driver.back()


file.close()
driver.quit()