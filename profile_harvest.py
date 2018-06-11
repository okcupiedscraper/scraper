from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import csv

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36") #most used userer-agent at the moment

driver = webdriver.Chrome("", chrome_options=opts) #chrome driver


def login():
    driver.get("https://okcupid.com")  # opens up chrome - okcupid
    agent = driver.execute_script("return navigator.userAgent")
    print(agent)
    user_name = ""  # give username
    password = ""  # give password
    time.sleep(5)
    button = driver.find_element_by_xpath('//*[@id="root"]/span/div/div[1]/div[1]/div[2]/button')
    button.click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="root"]/span/div/div[2]/span/div/form/div[2]/div[1]/span[2]/input').send_keys(
        user_name)
    driver.find_element_by_xpath('//*[@id="root"]/span/div/div[2]/span/div/form/div[2]/div[2]/span[2]/input').send_keys(
        password)
    driver.find_element_by_xpath('//*[@id="root"]/span/div/div[2]/span/div/form/div[3]/input').click()

    time.sleep(5)


def inf_scroll():
    counter=1
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.90);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match = False
    user_list1 = []
    varr = 'https://okcupid.com'
    while(match == False):
        lastCount = lenOfPage
        time.sleep(5)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.90);var lenOfPage=document.body.scrollHeight;return lenOfPage;")


        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        foo = soup.find('div', {"class": 'match-results-cards'})
        user_list = foo.find_all('a', {'class': 'image_link'})
        for user in user_list:
            user_list1.append(user.get('href'))


        if lastCount==lenOfPage or counter==100:
            match = True

        counter+=1
    user_list1 = list(set(user_list1))
    with open('C:/Users/alexel_t91/Desktop/csvusers7.csv', 'w', encoding='utf8') as userfile:
        userfilewriter = csv.writer(userfile)
        userfilewriter.writerow(user_list1)
        userfile.close()

login() #opens up browser and logins
inf_scroll() #scrapes the results of every person set in each city
driver.quit()
