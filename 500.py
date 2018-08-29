from selenium.common import exceptions
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import re
import requests
import json
import sys
from bs4 import BeautifulSoup
from pymouse import PyMouse
import random
import string
import urllib.request
import logging
from urllib import request
from urllib import parse
from urllib.request import urlopen

url = "https://www.XXX.com/admin?uid=18893259274"

header = {
"Host": "www.XXX.com",
"Connection": "keep-alive",
"X-Requested-With": "XMLHttpRequest",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
"Content-Type": "application/x-www-form-urlencoded",
"Accept": "*/*",
"Referer":"https://www.XXX.com/admin",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"zh-CN,zh;q=0.9"
}

res = requests.get(url,headers = header).text
res = parse.unquote(res)
print(res.encode('utf-8').decode('utf8'))

