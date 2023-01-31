'''
LOGIN TO BITSNET
--> Update your login and password in the 'login_conf.ini'
--> Run this script using python3
--> If ran successfully will give output - 'Success'
--> If not ran successfully will give output - 'Failure'
'''

import requests
import xml.etree.ElementTree as ElementTree
import getpass

login = input('Login ID : ')
password = getpass.getpass('Password : ')

#login request headers


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://campnet.bits-goa.ac.in:8090/httpclient.html',
    'Connection': 'keep-alive',
}

data = {
    'mode': '191',
    'username': login,
    'password': password,
    'a': '1669121329680',
    'producttype': '0',
}

#login POST request
response = requests.post('https://campnet.bits-goa.ac.in:8090/login.xml', headers=headers, data=data)
x = response.content

#parsing response
root = ElementTree.fromstring(x)
for log in root.iter('message'):
    if 'signed' in log.text:
    	print('Success')
    	#'You are signed in as {username}'
    else:
    	print('Failure')
    	#'Login failed. Invalid user name/password. Please contact the administrator.'
