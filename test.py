#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "Morrow"

import json
import pickle
import requests
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# https://app-test2.pokio.com/pybigshare/login/captcha/?email=pokioairtest@yeah.net
# r = requests.get('https://app-test2.pokio.com/pybigshare/login/captcha/?email=pokiobankid@yeah.net')
R={"time":1234567890,"code":1,"data":{"captcha":"123456"},"method":"null","server":"python"}

def captcha():
    # r = requests.get('https://app-test2.pokio.com/pybigshare/login/captcha/?email=pokiobankid@yeah.net')
    # #get协议请求
    # R=r.text
    #调取内容
    R = {"time": 1234567890, "code": 1, "data": {"captcha": '503784'}, "method": "null", "server": "python"}
    if type(R).__name__ != 'dict':
        R = json.loads(R)
    #转换为“dict”
    R1=R["data"]["captcha"]
    #取字典中的字典的值
    if R1 == 'null':
        raise Exception('验证码没有给出')
    #判空时抛出错误
    code_details=[]
    for i in R1:
        code_details.append(i)
    #转换成列表赋值给code_details
    return code_details


# sign_up_counter = 0
# login_counter = 0
# f = open('pickle.txt', 'wb')
# pickle.dump(sign_up_counter, f)
# f.close()
# #手动重置计数器

while poco("com.qfun.pokio:id/iv_content").exists():
    poco("com.qfun.pokio:id/iv_close_ad").click()