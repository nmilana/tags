import os
from selenium import webdriver
# import selenium.webdriver.support.expected_conditions as EC
import time
import random

browser = webdriver.Chrome(executable_path="driver/chromedriver")

# log/pass
f = open("../sign.txt", "r", encoding='utf-8')
time.sleep(0.5)
log = []
n_log = 0
for line in f:
    log.append(line[:-1].split(":"))
    print(log)
f.close()
print(f'len(log) = {len(log)}')

username, password = log[0]
print(f'first => {username}:{password}')
time.sleep(.5)


# input("Go to accounts login")
browser.get("https://www.instagram.com/accounts/login/")
time.sleep(2)

print(f"The URL of the current page: {browser.current_url}")

# input("Go to login")
# username / password / Log in

for c in username:
    browser.find_element_by_css_selector('[name=username]').send_keys(c)
    time.sleep(.4)
time.sleep(1)
for c in password:
    browser.find_element_by_css_selector('[name=password]').send_keys(c)
    time.sleep(.3)
time.sleep(2)
browser.find_element_by_css_selector('[type=submit]').click()
time.sleep(5)

print(f"The URL of the current page: {browser.current_url}")
# input("-----Press-Enter-----")
# read the user dir list
lst = os.listdir(f"files/{username}/")
print(lst)

# finding amount of tag files
n_tag = len(lst) - 1
print(f'n_tag = {n_tag}')

while n_tag:
    time.sleep(1)

    print("# Action on the site with the selfname")
    browser.get("https://www.instagram.com/" + username + "/")
    # browser.get("https://www.instagram.com/mama_v_dome_/")
    time.sleep(3)

    print(f"The URL of the current page: {browser.current_url}")

    print("# go to the first post")
    browser.find_element_by_css_selector('article a').click()
    time.sleep(2)

    # read the user comment list
    fc = open(f"files/{username}/{lst[0]}", "r", encoding='utf-8')
    time.sleep(0.5)
    cmnts = []
    for line in fc:
        cmnts.append(line[:-1])
    fc.close()

    # the random choice of a comment
    comment = cmnts[random.randint(0, len(cmnts) - 1)]
    print(comment)
    time.sleep(2)

    # tags
    ft = open(f"files/{username}/{lst[n_tag]}", "r", encoding='utf-8')
    time.sleep(2)
    tags = []
    for line in ft:
        tags.append("#" + line[:-1])
    ft.close()
    time.sleep(3)
    print("# comment in the post")
    browser.find_element_by_css_selector("textarea").click()
    time.sleep(2)
    
    # input("-----Press-Enter-----")

    for c in comment:
        browser.find_element_by_css_selector("textarea").send_keys(c)
        time.sleep(.5)
    time.sleep(2)
    browser.find_element_by_css_selector('textarea+button').click()
    time.sleep(4)

    print("# find the biggest comment number")
    k = len(browser.find_elements_by_css_selector('ul > ul'))
    # print(f"n = {n}")
    s = lambda i: f'ul ul:nth-of-type({i}) [href="/{username}/"]'
    d = lambda i: browser.find_elements_by_css_selector(s(i))
    # k = n
    print(f"k = {k}")
    while not len(d(k)):
        k -= 1
    print(f"k = {k}")
    time.sleep(2)

    print("# click the replay button")
    browser.find_element_by_css_selector(f'ul ul:nth-of-type({k}) button:nth-child(2)').click()
    time.sleep(2)

    print("# type the replay comment")
    for c in tags:
        browser.find_element_by_css_selector('form textarea').send_keys(" " + c)
        time.sleep(.5)
    time.sleep(4)

    print("# click textarea button (tb)")
    browser.find_element_by_css_selector('textarea+button').click()
    time.sleep(5)

    print("# find the biggest comment number for popup")
    k = len(browser.find_elements_by_css_selector('ul > ul'))
    # print(f"n = {n}")
    s = lambda i: f'ul ul:nth-of-type({i}) [href="/{username}/"]'
    d = lambda i: browser.find_elements_by_css_selector(s(i))
    # k = n
    print(f"k = {k}")
    while not len(d(k)):
        k -= 1
    print(f"k = {k}")

    print("# click Popup button (pbn)")
    # pbn = browser.find_element_by_css_selector(f'ul:nth-of-type({k}) div:nth-child(2) button:first-child')
    time.sleep(3)
    # pbn.click()
    browser.execute_script(f"document.querySelector(`ul:nth-of-type({k}) div:nth-child(2) button:first-child`).click();")
    time.sleep(5)

    # input("Press Enter")

    print("# click Delete on Popup (dbn)")
    # dbn = document.querySelector(`[role="presentation"] button:nth-child(2)`)
    # dbn.click()
    browser.find_element_by_css_selector(f'[role="presentation"] button:nth-child(2)').click()
    
    n_tag -= 1

# input("Press Enter")

browser.delete_all_cookies()
browser.quit()
print("# end")