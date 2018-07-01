#! -*- coding: UTF-8 -*-

import oauth2 as oauth
import json


APP_KEY = 'ePABg6nDiN4q'
APP_SECRET = 'zgg597gw7BwuUxV1vsPtg1UCkfdzYqY3'
OAUTH_TOKEN = 'D4soIh7fwFHa'
OAUTH_SECRET = 'BpGCQ9xgvBVnY9q6I0oH512yX8s80Xiv'

consumer = oauth.Consumer(APP_KEY,APP_SECRET)
token = oauth.Token(OAUTH_TOKEN, OAUTH_SECRET)
client = oauth.Client(consumer, token)

off = 0
url = 'https://www.plurk.com/APP/Blocks/get'
response = client.request(url, method='GET')
r = int(json.loads(response[1])['total'])

while(off<r):
	url = 'https://www.plurk.com/APP/Blocks/get'
	response = client.request(url, method='GET')
	for i in json.loads(response[1])['users']:
		url = 'https://www.plurk.com/APP/Blocks/unblock?user_id=%s'%i['id']
		client.request(url, method='GET')
	off=off+10



