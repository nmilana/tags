from selenium import webdriver
import selenium.webdriver.support.expected_conditions as EC
import time

# log/pass
f = open("files/sign.txt", "r", encoding='utf-8')
time.sleep(0.5)
for line in f:
    x = line[:-1].split(":")
    print(x)
    username = x[0]
    password = x[1]
f.close()
time.sleep(.5)

# comment
fc = open("files/cat_comment_rus.txt", "r", encoding='utf-8')
time.sleep(0.5)
for line in fc:
    comment = line[:-1]
fc.close()
print(comment)
time.sleep(2)

# tags
ft = open("files/cat_tags_rus.txt", "r", encoding='utf-8')
time.sleep(2)
tags = []
for line in ft:
    tags.append("#" + line[:-1])
ft.close()
time.sleep(2)

browser = webdriver.Chrome(executable_path="driver/chromedriver")

# input("Go to accounts login")
browser.get("https://www.instagram.com/accounts/login/")
time.sleep(2)

print(f"The URL of the current page: {browser.current_url}")

# input("Go to login")
# username / password / Log in

path_form = "//section/main/div/article/div/div[1]/div/form/"
for c in username:
    browser.find_element_by_xpath(
        xpath=path_form + "div[2]/div/label/input").send_keys(c)
    time.sleep(.4)
time.sleep(1)
for c in password:
    browser.find_element_by_xpath(
        xpath=path_form + "div[3]/div/label/input").send_keys(c)
    time.sleep(.3)
time.sleep(1)
browser.find_element_by_xpath(
    xpath="//section/main/div/article/div/div[1]/div/form/div[4]/button").click()
time.sleep(5)

# input("Go? Press Enter!")
print("# Action on the site with the selfname")
browser.get("https://www.instagram.com/" + username + "/")
time.sleep(3)

print(f"The URL of the current page: {browser.current_url}")
print(f"The current page title: {browser.title}")

print("# go to the first post")
browser.find_element_by_xpath(
    xpath="//section/main/div/div[2]/article/div/div/div[1]/div[1]/a").click()
time.sleep(2)

print("# comment in the post")
browser.find_element_by_css_selector("textarea").click()
time.sleep(1)

for c in comment:
    browser.find_element_by_css_selector("textarea").send_keys(c)
    time.sleep(.5)
time.sleep(1)
browser.find_element_by_css_selector('textarea+button').click()
time.sleep(2)

input("Wait a new post of an other user")
browser.refresh()
time.sleep(1)

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
time.sleep(1)

print("# click the replay button")
browser.find_element_by_css_selector(f'ul ul:nth-of-type({k}) button:nth-child(2)').click()
time.sleep(1)

print("# type the replay comment")
for c in tags:
    browser.find_element_by_css_selector('form textarea').send_keys(" " + c)
    time.sleep(.5)
time.sleep(3)

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
time.sleep(1)
# pbn.click()
browser.execute_script(f"document.querySelector(`ul:nth-of-type({k}) div:nth-child(2) button:first-child`).click();")
time.sleep(5)

# input("Press Enter")

print("# click Delete on Popup (dbn)")
# dbn = document.querySelector(`[role="presentation"] button:nth-child(2)`)
# dbn.click()
browser.find_element_by_css_selector(f'[role="presentation"] button:nth-child(2)').click()

# input("Press Enter")

browser.delete_all_cookies()
browser.quit()
print("# end")