#! -*- coding: UTF-8 -*-

import oauth2 as oauth
import json,sys


APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_SECRET = '' #plurk api for your primary account

consumer = oauth.Consumer(APP_KEY,APP_SECRET)
token = oauth.Token(OAUTH_TOKEN, OAUTH_SECRET)
client = oauth.Client(consumer, token)

post_url = raw_input("which post do you whant to chase?")
url = 'https://www.plurk.com/APP/FriendsFans/getFollowingByOffset?offset=0&limit=1000'
followList = client.request(url, method='GET')
print "smelling all possible targets......"


APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_SECRET = '' #plurk api for kitty

consumer = oauth.Consumer(APP_KEY,APP_SECRET)
token = oauth.Token(OAUTH_TOKEN, OAUTH_SECRET)
client = oauth.Client(consumer, token)

counter = 0
for i in json.loads(followList[1]):
	url = 'https://www.plurk.com/APP/Blocks/block?user_id=%s'%i['id']
	res = client.request(url, method='GET')
	counter = counter+1

print "found targets: ",len(json.loads(followList[1])),"failed targets: ", len(json.loads(followList[1]))-counter



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import re


print "chasing the targets......"

driver = webdriver.Chrome()
driver.get("https://www.plurk.com/login")
actions1 = ActionChains(driver)

username = driver.find_element_by_id("input_nick_name")
username.send_keys("") #kitty account
actions1.click(username)
actions1.key_down(Keys.TAB, username)
actions1.send_keys("") #kitty password
actions1.perform()
driver.find_element_by_id("register_submit").click()
driver.implicitly_wait(1)

driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get(post_url)

found = 0
try:
	textbox = driver.find_element_by_id("input_big")
except NoSuchElementException: 
	print "Seems that the author is in your friends. Use Anonymous_Hounds instead."
	driver.close()
	for i in json.loads(followList[1]):
		url = 'https://www.plurk.com/APP/Blocks/unblock?user_id=%s'%i['id']
		client.request(url, method='GET')
	sys.exit(1)

textbox.send_keys("...")
actions2 = ActionChains(driver)
actions2.click(textbox)
actions2.key_down(Keys.ENTER, textbox)
actions2.perform()
soup = BeautifulSoup(driver.page_source, "html.parser")
lasttext = soup.find_all("a",style="color: #0a9c17")
if len(lasttext)>0:
	print "The author is not in your following. Try using Anonymous_Hounds instead."
	found = 1



prev_nick = ""
for i in json.loads(followList[1]):
	url = 'https://www.plurk.com/APP/Blocks/unblock?user_id=%s'%i['id']
	client.request(url, method='GET')
	if(found==0):
		try:
			textbox = driver.find_element_by_id("input_big")
		except NoSuchElementException:
			if(prev_nick):
				print "chasing completed. The author is: ",prev_nick
				found = 1
				continue
			else:
				print "The author is not in your following. Try using Anonymous_Hounds instead."
				found = 1
				continue
		textbox.send_keys("(cozy)")
		actions2 = ActionChains(driver)
		actions2.click(textbox)
		actions2.key_down(Keys.ENTER, textbox)
		actions2.perform()
		soup = BeautifulSoup(driver.page_source, "html.parser")
		lasttext = soup.find_all("a",style="color: #0a9c17")
		if len(lasttext)>0:
			print "chasing completed. The author is: ",i['nick_name']
			found = 1
		prev_nick = i['nick_name']

if(found==0):
	print "Bad cat! There must be some problems."

driver.close()


