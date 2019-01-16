import time 
from selenium import webdriver
import re
import requests
from http import cookiejar
def login():
         browser = webdriver.Chrome()
         browser.get('https://i.qq.com/')
         browser.maximize_window()
         time.sleep(2)
         browser.switch_to.frame("login_frame")
         browser.find_element_by_id('switcher_plogin').click()
         browser.find_element_by_id('u').clear()
         browser.find_element_by_id("u").send_keys("你的QQ账号")
         browser.find_element_by_id('p').clear()
         browser.find_element_by_id("p").send_keys("你的QQ密码")
         browser.find_element_by_id("login_button").click()
         time.sleep(2)
         print("空间登陆成功")
         browser.switch_to.default_content()
         return browser
def back_session(browser):
 
    #创建一个session对象
    my_session = requests.session()
    #获取网页的cookie
    cooikes = browser.get_cookies()
    #创建一个空的cookie字典
    cookie = {}
    #将登陆后网页的cookies以字典的形式保存
    for elem in cooikes:
        cookie[elem['name']] = elem['value']
    headers = {
        'host': 'h5.qzone.qq.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    #将字典转为cookiejar，这样就可以将cookie赋给session
    c = requests.utils.cookiejar_from_dict(
        cookie, cookiejar=None, overwrite=True)
    my_session.headers = headers
    #将cookie赋给session
    my_session.cookies.update(c)
    return my_session
