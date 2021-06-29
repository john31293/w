import requests
import selenium
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('https://login.live.com')

URL ='https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1624967999&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d761b3a7e-32fd-f0d5-b84a-f9c77a9d461c&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&pcexp=false&cobrandid=90015' 

values = {'email': 'email',
          'password':'password'}
		  
     
r = requests.post(URL, data=values)
print(r.content)
