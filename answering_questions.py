from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from random import randint


opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")

driver = webdriver.Chrome("", chrome_options=opts)


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
    driver.find_element_by_xpath('//*[@id="root"]/span/div/div[2]/span/div/form/div[2]/div[1]/span[2]/input').send_keys(user_name)
    driver.find_element_by_xpath('//*[@id="root"]/span/div/div[2]/span/div/form/div[2]/div[2]/span[2]/input').send_keys(password)
    driver.find_element_by_xpath('//*[@id="root"]/span/div/div[2]/span/div/form/div[3]/input').click()

    time.sleep(5)



def answer():
    driver.get("https://www.okcupid.com/profile/15018248552462369290/questions")
    time.sleep(5)
    parent = driver.find_element_by_css_selector('.content.clearfix')
    button = parent.find_element_by_tag_name('button')
    try:
        button.send_keys(u'\ue007')
    except:
        answer()

    for i in range(0, 10000):
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.01);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        time.sleep(2)
        parent = driver.find_element_by_css_selector('.profile2015-content.questions')
        parent = parent.find_element_by_css_selector('.container.my_answer')
        spans = parent.find_elements_by_tag_name('span')
        spans = list(spans)
        n = randint(0, len(spans) - 1)
        button = spans[n]
        time.sleep(2)
        try:
            driver.execute_script("arguments[0].click();", button)
        except:
            answer()

        parent = driver.find_element_by_css_selector('.container.acceptable_answers')
        label = parent.find_element_by_css_selector('.checkbox.irrelevant.checked')
        span = label.find_element_by_tag_name('span')
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.1);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        time.sleep(2)
        try:
            driver.execute_script("arguments[0].click();", span)
        except:
            answer()

        time.sleep(2)

        spans = parent.find_elements_by_tag_name('label')
        spans = list(spans)
        n = randint(0, 1)
        button = spans[n]
        time.sleep(2)
        try:
            driver.execute_script("arguments[0].click();", button)
        except:
            answer()

        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.09);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        parent = driver.find_element_by_css_selector('.container.importance')
        parent = parent.find_element_by_css_selector('.importance_radios')
        span_ = ['c', 'a', 'r']
        span_[0] = parent.find_element_by_css_selector('.importance_4.radio')
        span_[1] = parent.find_element_by_css_selector('.importance_3.radio')
        span_[2] = parent.find_element_by_css_selector('.importance_1.radio')
        n = randint(0, 2)
        button = span_[n]
        try:
            driver.execute_script("arguments[0].click();", button)
        except:
            answer()
        time.sleep(2)
        button = driver.find_element_by_css_selector('.submit_btn.flatbutton.small.okblue')
        try:
            driver.execute_script("arguments[0].click();", button)
        except:
            answer()



login()

answer()
