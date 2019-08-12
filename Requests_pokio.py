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
    """
    钉钉异常告警
    :param webhook: 钉钉组中创建机器人的时候给出的webhook（API地址）
    :param content: 告警的内容
    :param user: 抄送@的人，可以指定谁
    :param Atall:True是@所有人，有指定用户也会@所有人、False不@人，但是有指定用户会@指定用户
    :return:
    """
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
    if R1 == None:
        raise Exception('验证码没有给出')
    #判空时抛出错误
    print('当前验证码为：',R1)
    return R1

# a='https://oapi.dingtalk.com/robot/send?access_token=859982b9d50aef0c502af69287842b9b10dda4673c717a21a54c6813bc689448'
# dingding_Disaster(a,'辣鸡!!!!',user=17789104200,Atall=False)
