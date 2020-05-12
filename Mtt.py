# -*- encoding=utf8 -*-
__author__ = "Morrow"

import time
import requests
from airtest.core.api import *
from airtest.cli.parser import cli_setup

# if not cli_setup():
#     auto_setup(__file__, logdir="D:/Pokio_airtest_monitoring/log", devices=[
#             "Android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI",
#     ], project_root="D:/Pokio_airtest_monitoring")


def Create_Mtt():
    datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    list = []
    for i in datetime:
        list.append(i)
    # 转化为数组切片修改十位数分钟和个位数分钟
    print(list)
    list[-5] = str(int(list[-5]) + 2)
    # 十位数分钟固定+2
    list[-4] = '0'
    list[-1] = '0'
    list[-2] = '0'
    # 个位数分钟和秒数固定改成0
    if int(list[-5]) >= 6:
        list[-5] = '0'
        list[-4] = '0'
        list[-7] = str(int(list[-7]) + 1)
    # 当十位数分钟大于等于6的时候，都设置为下一个小时整点开赛，55分~60分无法开赛，暂时不管
    datetime = ''.join(list)
    # 再次变化为字符串
    print(datetime)
    data = {
        'event_name': 'zhoumingSB',
        'event_desc': 'test12345678901234567890123456789012345678901234567890',
        'game_type': 'Holdem',
        'binds_up': '5',
        'start_stakes': '100',
        'event_fee': '1',
        'service_fee': '0',
        'start_time': datetime,
        'player_min': '11',
        'late_reg': '10',
        'rebuy_times': '5',
        'prize_guranteed': '',
        'blind_structure': 'standard',
        'table_size': '9',
        'add_on': '1',
        'is_halftime': '0',
        'restrict_gps_ip': '0',
        'hide_players_stats': '0',
        'ticket_only': '0',
        'custom_payout_structure': '1',
        'custom_payout_info': '[]'
    }
    #post参数
    webhook = 'http://192.168.101.180:8109/mg/mtt_official'
    #post url
    headers = {
        'Origin': 'http://192.168.101.180:8109',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Referer': 'http://192.168.101.180:8109/mg/mtt_official?tag1=mtt&tag2=match',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }
    result = requests.post(webhook, data=data, headers=headers)
    #发送请求
    print('比赛开始时间为%s'%datetime)
    print(result)
    result1=result.json()
    print(result1)
    event_id=result1['error_msg']['event_id']
    event_uuid=result1['error_msg']['event_uuid']
    print(event_id,event_uuid)
    '''
    json.dumps() 编码成json格式数据
    json.loads() 对json格式的数据进行解码
    '''
    return event_id,event_uuid

def Join_Mtt(event_id,event_uuid):
    data = {
        'method': 'enroll',
        'event_id': event_id,
        'uid': '20000,20001,20002,20003,20004,20005,20006,20007,20008,20009,20010,20011,20012,20013,20014,20015,20016,20017,20018,20019,20020,20021,20022,20023,20024,20025,20026,20027,20028,20029,20030,20031,20032,20033,20034,20035,20036,20037,20038,20039,20040,20041,20042,20043,20044,20045,20046,20047,20048,20049,20050,20051,20052,20053,20054,20055,20056,20057,20058,20059,20060,20061,20062,20063,20064,20065,20066,20067,20068,20069,20070,20071,20072,20073,20074,20075,20076,20077,20078,20079,20080,20081,20082,20083,20084,20085,20086,20087,20088,20089,20090,20091,20092,20093,20094,20095,20096,20097,20098,20099,20100,20101,20102,20103,20104,20105,20106,20107,20108,20109',
        'ticket_no': '',
        'event_uuid': event_uuid
    }
    headers = {
        'Origin': 'http://192.168.101.180:8109',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Referer': 'http://192.168.101.180:8109/mg/mtt_event_list?tag1=mtt&tag2=event',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }
    url='http://192.168.101.180:8109/mg/mtt_event_list'
    response = requests.post(url, headers=headers,data=data)
    print(response)
    print(response.json())
    print('成员添加成功')
    '''
    json.dumps() 编码成json格式数据
    json.loads() 对json格式的数据进行解码
    '''

Create_Mtt()
Join_Mtt()
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath="D:/Pokio_airtest_monitoring/log")