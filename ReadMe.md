This bot simply goes to the website of PhonesIQ and scrapes the links of various news links with BeautifulSoup.
It then stores this links in a text file, another python file called Comments.py holds a list of strings which are randomly
typed strings.

The Automator.py(the main bot) uses Selenium webdriver with chromedriver, and logs in to the site with the user name and password
specified and then randomly picks from the comments list and inputs them in the comment section of each news tab and then goes back
and repeats the same step for each link in the generated text file.