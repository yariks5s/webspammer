import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import json
import random

bot_token = ''# your bot token
chat_id = '840355587'
phone = '997377322'

def wikipedia():
    driver = webdriver.Chrome('C:\\Users\\bryuh\\PycharmProjects\\botspammer\\chromedriver.exe')
    try:
        driver.get("https://en.wikipedia.org/wiki/Main_Page")
        time.sleep(10)
        search = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div/div/form/div/input[1]')
        search.send_keys('Ukraine')
        search.send_keys(Keys.ENTER)
        time.sleep(10)
        link = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[4]/div[3]/ul/li[1]/div[1]/a')
        link.click()
    finally:
        driver.quit()

def start_spamming():
    driver = webdriver.Chrome('C:\\Users\\bryuh\\PycharmProjects\\botspammer\\chromedriver.exe')
    try:
        driver.get("https://web.telegram.org/k/")
        time.sleep(10)

        button = driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[2]/div/div[2]/button/div')
        button.click()
        time.sleep(10)

        country = driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[1]/div/div[3]/div[1]/div[1]')
        country.send_keys('Ukraine')
        country.send_keys(Keys.ENTER)
        time.sleep(10)

        phone_number = driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[1]/div/div[3]/div[2]/div[1]')
        phone_number.send_keys(phone)
        next_btn = driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[1]/div/div[3]/button[1]/div')
        next_btn.click()
        text_message = 'give me a code'
        requests.request(method='GET', url=f'https://api.telegram.org/bot{bot_token}/'
                                           f'sendMessage?chat_id={chat_id}&text={text_message}')
        code = ''
        for i in range(100):
            code = json.loads(requests.request(method='GET',
                                               url=f'https://api.telegram.org/bot{bot_token}/getUpdates?').text)[
                'result'][-1][
                'message']['text']

            time.sleep(2)
            date = json.loads(requests.request(method='GET',
                                               url=f'https://api.telegram.org/bot{bot_token}/getUpdates?').text)[
                'result'][-1]['message']['date']
            print((time.time() - date) / 60)
            if code.isdigit() and abs((time.time() - date) / 60) < 1:
                code_input = driver.find_element(by=By.XPATH,
                                                 value='//*[@id="auth-pages"]/div/div[2]/div[3]/div/div[3]/div/input')
                code_input.send_keys(code)
                time.sleep(5)
                # code_input.send_keys(Keys.ENTER)


    finally:
        driver.quit()


# start_spamming()
wikipedia()
