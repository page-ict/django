import os
import time
from threading import Thread
import requests


from selenium import webdriver


driver = webdriver.Chrome("./chromedriver")
driver.get("http://google.com")


def myfunc(par):
    if type(par) is list:
        print('ooh')
        par[0].get(par[1])
    else:
        print('ahh')


def go(par):
    ip = "http://127.0.0.1:8000/"
    for i in range(50):
        try:
            r = requests.get(ip)
            if r.status_code == 200:
                par.get(ip)
                break
        except:
            pass
        time.sleep(1)




t = Thread(target=go, args=[driver])
t.start()
print('starting server...')
os.system('python manage.py runserver')