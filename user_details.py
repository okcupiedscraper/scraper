from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import csv
import ast

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")

driver = webdriver.Chrome("", chrome_options=opts)


def login():
    driver.get("https://okcupid.com")  # opens up chrome - okcupid
    agent = driver.execute_script("return navigator.userAgent")
    print(agent)
    user_name = "evich_blah@mail.com"  # give username
    password = "1234567890As!"  # give password
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


def scrape():
    with open('profile_urls.csv', 'r') as userfile:
        userfilereader = csv.reader(userfile)
        for col in userfilereader:
            userlist.append(col)

    actual_list = ast.literal_eval(str(userlist[0]))
    print(len(actual_list))
    actual_list = list(set(actual_list))
    print(len(actual_list))
    userfile.close()


    for user in actual_list:
        driver.get("https://okcupid.com"+user)
        time.sleep(3)
        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')




        class_name = "userinfo2015-basics-username"
        class_age = "userinfo2015-basics-asl-age"
        class_location = "userinfo2015-basics-asl-location"

        div_name = 0


        users_age = None
        users_location = None
        gender = None
        users_essay = None
        users_gender = None
        users_background = None
        users_misc = None


        try:
            div_name = soup.find('div', {"class": class_name})
        except:
            pass

        if (div_name!=0) and (div_name != None):

            users_name = div_name.text

            img_list = []
            bar = 0
            try:
                bar = soup.find('div', {"class": 'userinfo2015-thumb'})
            except:
                pass

            if (bar != 0) and (bar is not None):
                images = bar.find_all('img')
                for imge in images:
                    img_list.append(imge.get('data-src'))



            try:
                span_age = soup.find('span', {"class": class_age})
                users_age = span_age.string
            except:
                pass
            try:
                span = soup.find('span', {"class": class_location})
                users_location = span.string
            except:
                pass

            div_gender = 0

            try:
                class_gender = "details2015-section basics"
                div_gender = soup.find('table', {"class": class_gender})
            except:
                pass
            if (div_gender!=0) and (div_gender is not None):
                users_gender = div_gender.text
                for gnd in users_gender.split():
                    if gnd == 'Man,':
                        gender = "male"
                    elif gnd == 'Woman,':
                        gender = "female"


            try:
                class_body = "profile2015-content-main"
                div = soup.find('div', {"class": class_body})
                sep = "See questions"
                users_essay1 = div.text
                users_essay2 = users_essay1.partition(sep)
                users_essay = users_essay2[0]
            except:
                pass


            div_back = 0
            try:
                class_gender = "details2015-section background"
                div_back = soup.find('table', {"class": class_gender})
            except:
                pass


            div_misc = 0
            try:
                class_gender = "details2015-section misc"
                div_misc = soup.find('table', {"class": class_gender})
            except:
                pass



            graph_url = 0
            href = 0
            try:
                href = soup.find('a', {"class": "traits2015-more"})
            except:
                pass

            if (href != None) and (href != 0):
                graph_url = 1

            if div_back == 0:
                users_background = "No user background"
            elif (div_back is not None) and (div_back != 0):
                users_background = div_back.text
                users_background = users_background.replace('.st0{clip-path:url(#SVGID_2_);}  globe', '')
                users_background = users_background.replace('                    ', '')

            if div_misc == 0:
                users_misc = "No user misc"
            elif (div_misc != 0) and (div_misc is not None):
                users_misc = div_misc.text
                users_misc = users_misc.replace('.cls-1{fill:none;}.cls-2{clip-path:url(#clip-path);}Label', '')

            if div_gender == 0:
                users_misc = "No user misc"
            elif (div_gender != 0) and (div_gender is not None):
                users_gender = users_gender.replace('  clipboard  ', '')

            if graph_url != 0:
                href = href.get('href')
                graph_url = "https://www.okcupid.com" + str(href)
                driver.get(graph_url)
                time.sleep(3)
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')

                class_graph = "personalityChart2015-chart"
                foo = 0
                try:
                    foo = soup.find('div', {"class": class_graph})
                except:
                    pass
                if (foo!=0) and (foo is not None):
                    div_all = foo.find_all('div')
                    graph_text = []
                    graph_width = []
                    for div in div_all:
                        graph_text.append(div.text)

                    for div in soup.find_all('div', {"class": "chartTrait-bar-inner"}):
                        graph_width.append(div.get('style'))
                    s = "-"
                    img_list = [x for x in img_list if x is not None]
                    img_list = s.join(img_list)

                    s = "-"
                    graph_text = [x for x in graph_text if x is not None]
                    graph_text = s.join(graph_text)

                    s = "-"
                    graph_width = [x for x in graph_width if x is not None]
                    graph_width = s.join(graph_width)

                    print(user, users_name, users_age, users_location, gender, users_essay, img_list, graph_text, graph_width, users_gender, users_background, users_misc)
                    print(user+(' with grapgh'))
            else:
                s = "-"
                img_list = [x for x in img_list if x is not None]
                img_list = s.join(img_list)
                graph_text = "User didnt have graph"
                graph_width = "User didnt have graph"
                print(user, users_name, users_age, users_location, gender, users_essay, img_list, graph_text, graph_width, users_gender, users_background, users_misc)
                print(user + (' without grapgh'))

            



login()
userlist = []
scrape()

driver.quit()
