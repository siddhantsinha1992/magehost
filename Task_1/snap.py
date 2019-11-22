#!/usr/bin/env python3

import json
import requests
import sys
import datetime

droplet_id = int(sys.argv[1])
api_token = 'your api_token'
api_url_base = 'https://api.digitalocean.com/v2/'

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

def get_account_info():
	api_url = '{0}account'.format(api_url_base)
	response = requests.get(api_url, headers=headers)
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None

def droplet_on(droplet_id):
	api_url = '{0}droplets/{1}'.format(api_url_base,droplet_id)
	response = requests.get(api_url, headers=headers)
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None

def power_off(droplet_id):
	api_url = '{0}droplets/{1}/actions'.format(api_url_base,droplet_id)
	params = {'type' : 'power_off'}
	post = requests.post(api_url, headers=headers, params=params)
	if post.status_code == 201:
		return json.loads(post.content.decode('utf-8'))
	else:
		return None

def snapshot(droplet_id):
	time = str(datetime.datetime.now())
	api_url = '{0}droplets/{1}/actions'.format(api_url_base,droplet_id)
	params = {'type' : 'snapshot', 'name': f"Droplet {droplet_id} {time}"}
	post = requests.post(api_url, headers=headers, params=params)
	if post.status_code == 201:
		return json.loads(post.content.decode('utf-8'))
	else:
		return None

snapshot = snapshot(droplet_id)
if snapshot is not None:
    print("Here's snapshot info: ")
    for k, v in snapshot['action'].items():
        print('{0}:{1}'.format(k, v))
else:
    print('[!] Request Failed')

'''
power_info = power_off(168210634)
if power_info is not None:
    print("Here's your info: ")
    for k, v in power_info['action'].items():
        print('{0}:{1}'.format(k, v))

else:
    print('[!] Request Failed')


droplet_info = droplet_on(168210634)

if droplet_info is not None:
    print("Here's your info: ")
    for k, v in droplet_info['droplet'].items():
        print('{0}:{1}'.format(k, v))

else:
    print('[!] Request Failed')

account_info = get_account_info()

if account_info is not None:
    print("Here's your info: ")
    for k, v in account_info['account'].items():
        print('{0}:{1}'.format(k, v))

else:
    print('[!] Request Failed')

'''
