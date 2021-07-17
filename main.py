'''
Created Date: Saturday July 17th 2021 4:45:25 pm
Author: Andrés X. Vargas
-----
Last Modified: Saturday July 17th 2021 5:41:03 pm
Modified By: the developer known as Andrés X. Vargas at <axvargas@fiec.espol.edu.ec>
-----
Copyright (c) 2021 MattuApps
'''

from linkedin_scraper import Company, Person, actions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep 

opts = Options()
opts.add_argument(
    'user_agent=Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18')
driver = webdriver.Chrome('./chromedriver.exe', options=opts)

with open('pass.txt', mode='r', encoding='utf8') as f:
    passw = f.readlines()
    passw = passw[0].strip()

email = "axvargas@fiec.espol.edu.ec"

actions.login(driver, email, passw)

sleep(30)
company = Company("https://www.linkedin.com/company/uribe-schwarzkopf",  driver=driver)

company.scrape(close_on_complete=False)

print(company)