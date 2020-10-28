#kelly j 10-28-2020  learn together week 13, using this weeks lessons in a product
#this week we learned about scraping, controling browswers, etc... 
#for the learn together, I am going to open up firefox and go to youtube, search for a band name
# and then play the 1st result that comes back
#we had to install requests, beautifulsoup4, and seleium.  all set up in a virtual env.
#see readme.md for directions on how to set up 
#
#for the part about waiting till it could find the element by id I used this link
#https://stackoverflow.com/questions/55560173/how-to-search-and-play-a-video-on-youtube-using-selenium-in-python

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

bandname = input("Please enter band name: ")
# print(bandname)

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 3)
driver.get("http://www.youtube.com/")

search_elem = driver.find_element_by_xpath(r'//input[@id="search"]')
search_elem.send_keys(bandname)
search_elem.submit()

visible = EC.visibility_of_element_located
wait.until(visible((By.ID, "video-title")))
playelem = driver.find_element_by_id("video-title").click()
# playelem.click()


