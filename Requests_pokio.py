#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "Morrow"
#Date:
#Desc:

import os
import sys
import json
import datetime
import requests

def dingding_Disaster(webhook,content,user=None,Atall=True):
    # 钉钉组中创建机器人的时候给出的webhook
    # 告警测试
    # 测试推送url: https://oapi.dingtalk.com/robot/send?access_token=2ee4f0ee8a67ede67d75488aa2dff98a5ef827b1e76d20bc463e8836584ae0d4
    # 正式服监控告警url：https: // oapi.dingtalk.com / robot / send?access_token = cb7ba6766aaef974374b305ab042650983d7b0a14384f93fa38931ba583aaa39
    # 组装内容
    if webhook==None:
        pass
    else:
        data = {
            "msgtype": "text",
            "text": {
                "content": content
            },
            "at": {
                "atMobiles": [user],
                "isAtAll": Atall
            }
        }

        ## 调用request.post发送json格式的参数
        headers = {'Content-Type': 'application/json'}
        result = requests.post(url=webhook, data=json.dumps(data), headers=headers)
        '''
        json.dumps() 编码成json格式数据
        json.loads() 对json格式的数据进行解码
        '''

        print('=='*30+'\n')
        print(result)
        print(result.json())

        if result.json()["errcode"] == 0:
            print("告警信息已发送")
            print('\n'+'=='*30)

def captcha(url):
    r = requests.get(url)
    #get协议请求
    R=r.text
    #调取内容
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
    print(code_details)
    return code_details
