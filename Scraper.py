from bs4 import BeautifulSoup
import requests
import time

import lxml

page = requests.get("https://www.phonesiq.com/news")

time.sleep(15)

with open("Links.txt", "w", encoding= "utf-8") as newfile:
 soup = BeautifulSoup(page.text, 'lxml')

 for post in soup.find_all("h2", class_ = 'nk-post-title h4'):
    posts = post.a

    url = posts.get("href")
    content = url + '\n'
    newfile.write(content)
newfile.close()

