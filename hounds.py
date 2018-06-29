#! -*- coding: UTF-8 -*-

import oauth2 as oauth
import json


APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_SECRET = ''  #plurk api token

consumer = oauth.Consumer(APP_KEY,APP_SECRET)
token = oauth.Token(OAUTH_TOKEN, OAUTH_SECRET)
client = oauth.Client(consumer, token)

master_nick = raw_input("who is the master?")
post_url = raw_input("which post do you whant to chase?")
url = 'https://www.plurk.com/APP/UserSearch/search?query=%s'%master_nick
response = client.request(url, method='GET')
master = json.loads(response[1])['users'][0]['id']

url = 'https://www.plurk.com/APP/FriendsFans/getFriendsByOffset?user_id=%s&limit=1000'%master
response = client.request(url, method='GET')
print "smelling all possible targets......"


counter = 0
for i in json.loads(response[1]):
	url = 'https://www.plurk.com/APP/Blocks/block?user_id=%s'%i['id']
	res = client.request(url, method='GET')
	counter = counter+1

print "found targets: ",len(json.loads(response[1])),"failed targets: ", len(json.loads(response[1]))-counter



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import re


print "chasing the targets......"

driver = webdriver.Chrome()
driver.get("https://www.plurk.com/login")
actions1 = ActionChains(driver)

username = driver.find_element_by_id("input_nick_name")
username.send_keys("") #any acount that have no friends and response
actions1.click(username)
actions1.key_down(Keys.TAB, username)
actions1.send_keys("") #password
actions1.perform()
driver.find_element_by_id("register_submit").click()
driver.implicitly_wait(1)

driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to.window("tab2")
driver.get(post_url)
textbox = driver.find_element_by_id("input_big")



found = 0
for i in json.loads(response[1]):
	url = 'https://www.plurk.com/APP/Blocks/unblock?user_id=%s'%i['id']
	client.request(url, method='GET')
	if(found==0):
		textbox = driver.find_element_by_id("input_big")
		textbox.send_keys("I got you!")
		actions2 = ActionChains(driver)
		actions2.click(textbox)
		actions2.key_down(Keys.ENTER, textbox)
		actions2.perform()
		soup = BeautifulSoup(driver.page_source, "html.parser")
		lasttext = soup.find_all("a",style="color: #0a9c17")
		if len(lasttext)>0:
			print "chasing completed. The author is: ",i['nick_name']
			found = 1

if(found==0):
	print "not found! bad dog. Maybe the author is someone you following."

driver.close()


