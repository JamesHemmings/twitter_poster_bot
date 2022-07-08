import time

from selenium import webdriver
import os

if __name__ == "__main__":
twitter_home = "https://twitter.com/home"

#driver setup
chrome_driver_path = "chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:\Users\james\AppData\Local\Google\Chrome Beta\User Data')
options.binary_location = "C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
driver.implicitly_wait(time_to_wait=10)

driver.get(twitter_home)

tweet_entry = driver.find_element_by_css_selector('.DraftEditor-root br')
tweet_entry.send_keys("This is my first tweet,it was made using Python")

submit_tweet = driver.find_elements_by_xpath("//span[contains( text(), 'Tweet')]")
submit_tweet[2].click()