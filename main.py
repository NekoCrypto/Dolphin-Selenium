import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver

import time

profile_id = '' # User ID in Dolphin Anty


mla_url = 'http://localhost:3001/v1.0/browser_profiles/'+profile_id+'/start?automation=1'
resp = requests.get(mla_url)

json = resp.json()
print(json)

port = str(json['automation']['port'])
print(port)

chrome_dolphin_driver_path = Service(r"C:\PATH") # Download driver here https://anty-assets.s3.eu-central-1.amazonaws.com/chromedriver114.zip # Source https://dolphin-anty.com/docs/basic-automation/

options = Options()

options.debugger_address = "127.0.0.1:"+port

driver = webdriver.Chrome(service=chrome_dolphin_driver_path, chrome_options=options)

driver.get('https://twitter.com/')
print(driver.title)
time.sleep(5)


time.sleep(20)
