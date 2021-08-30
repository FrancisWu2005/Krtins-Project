import os
import random


from fp.fp import FreeProxy

from selenium.webdriver.common.proxy import Proxy, ProxyType

from selenium import webdriver
import time
import bs4
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.options import Options

import speech_recognition as sr
import ffmpy
import requests
import urllib
import pydub
from pydub import AudioSegment

f1 = 'fresh_proxies_proxies.txt'
f2 = 'fresh_proxies_ports.txt'
f3 = 'fresh_proxies_proxy_speed.txt'
f4 = 'fresh_proxies_up_time.txt'
f5 = 'fresh_proxies_country.txt'
f6 = 'fresh_proxies_anonymity.txt'

def proxy_ret():
    url = 'http://free-proxy.cz/en/'
    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=800,600")
    options.add_argument("--disable-dev-shm-usage")
    
    capabilities = options.to_capabilities()
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\kkeel\webdrivers\chromedriver.exe')
    driver.get(url)    
    page1 = driver.page_source
    soup = bs4.BeautifulSoup(page1, "lxml")
    table = soup.find('div', attrs = {'id':'__init__'})

    proxies = []
    ports = []
    proxy_speed = []
    up_time = []
    country = []
    anonymity = []

    for x in range (1, 5):
        text = driver.find_element_by_xpath('//*[@id="proxy_list"]/tbody/tr[%d]/td[1]/script' % x).text
        proxies.append(text)

    for x in range (6, 23):
        text = driver.find_element_by_xpath('//*[@id="proxy_list"]/tbody/tr[%d]/td[1]/script' % x).text
        proxies.append(text)

    for x in range (1, 5):
        text1 = driver.find_element_by_xpath('//*[@id="proxy_list"]/tbody/tr[%d]/td[2]/span' % x).text
        ports.append(text1)

    for x in range (6, 23):
        text1 = driver.find_element_by_xpath('//*[@id="proxy_list"]/tbody/tr[%d]/td[2]/span' % x).text
        ports.append(text1)

    for x in range (1, 5):
        text2 = driver.find_element_by_xpath('//*[@id="proxy_list"]/tbody/tr[%d]/td[8]/small' % x).text
        proxy_speed.append(text2)

    for x in range (6, 23):
        text2 = driver.find_element_by_xpath('//*[@id="proxy_list"]/tbody/tr[%d]/td[8]/small' % x).text
        proxy_speed.append(text2)

    for x in range (1, 5):
        text3 = driver.find_element_by_xpath('//*[@id="proxy_list"]/tbody/tr[%d]/td[9]/small' % x).text
        up_time.append(text3)

    for x in range (6, 23):
        text3 = driver.find_element_by_xpath('//*[@id="proxy_list"]/tbody/tr[%d]/td[9]/small' % x).text
        up_time.append(text3)

    for x in range (1, 5):
        text4 = driver.find_element_by_xpath('//*[@id="proxy_list"]/tbody/tr[%d]/td[4]/div/a' % x).text
        country.append(text4)

    for x in range (6, 23):
        text4 = driver.find_element_by_xpath('//*[@id="proxy_list"]/tbody/tr[%d]/td[4]/div/a' % x).text
        country.append(text4)

    for x in range (1, 5):
        text5 = driver.find_element_by_xpath('//*[@id="proxy_list"]/tbody/tr[%d]/td[7]/small' % x).text
        anonymity.append(text5)

    for x in range (6, 23):
        text5 = driver.find_element_by_xpath('//*[@id="proxy_list"]/tbody/tr[%d]/td[7]/small' % x).text
        anonymity.append(text5)
    

    f_1 = open(f1, 'r+')
    f_2 = open(f2, 'r+')
    f_3 = open(f3, 'r+')
    f_4 = open(f4, 'r+')
    f_5 = open(f5, 'r+')
    f_6 = open(f6, 'r+')


    f_1.truncate()
    f_2.truncate()
    f_3.truncate()
    f_4.truncate()
    f_5.truncate()
    f_6.truncate()


    f_1 = open(f1, 'w')
    f_2 = open(f2, 'w')
    f_3 = open(f3, 'w')
    f_4 = open(f4, 'w')
    f_5 = open(f5, 'w')
    f_6 = open(f6, 'w')
    
    
    for x in (proxies):
        f_1.write(x)
        f_1.write('\n')

    for x in (ports):
        f_2.write(x)
        f_2.write('\n')

    for x in (proxy_speed):
        f_3.write(x)
        f_3.write('\n')

    for x in (up_time):
        f_4.write(x)
        f_4.write('\n')

    for x in (country):
        f_5.write(x)
        f_5.write('\n')

    for x in (anonymity):
        f_6.write(x)
        f_6.write('\n')

        
proxy_ret()
