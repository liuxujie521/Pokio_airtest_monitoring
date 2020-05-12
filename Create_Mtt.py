# -*- encoding=utf8 -*-
__author__ = "Morrow"

import requests
import time
import json
from lxml import etree

class Mtt_control(object):
    #Mtt相关操作

    def __init__(self,
            url,
            game_type,
            binds_up,
            event_fee,
            service_fee,
            player_min,
            late_reg,
            rebuy_times,
            prize_guranteed,
            add_on,
            break_time,
            first_break_time_blind_level,
            break_time_interval_level,
            event_uuid,
            event_id):
        self.url=url,#地址，只需要输入后3位数
        self.game_type=game_type,#游戏模式
        self.binds_up = binds_up,#涨盲时间
        self.event_fee = event_fee,#报名费
        self.service_fee = service_fee,#服务费
        self.player_min = player_min,#开赛最小人数
        self.late_reg = late_reg,#延长报名等级
        self.rebuy_times = rebuy_times,#重构次数，1~99
        self.prize_guranteed = prize_guranteed,#保证金，可以不填
        self.add_on = add_on,#增购次数，只有1或0
        self.break_time = break_time,#休息时间开关，1或0
        self.first_break_time_blind_level = first_break_time_blind_level,#仅Break_time打开后生效，设置最小休息级别
        self.break_time_interval_level = break_time_interval_level,#仅Break_time打开后生效，设置休息间隔
        self.event_uuid=event_uuid,#赛事的UUID
        self.event_id=event_id,#赛事的ID
    '''
    Test2服的相关登陆操作
    暂时没有调通，不会使用
    '''
    # def Sent_ma(self):
    #     cookies = {
    #         'csrftoken': 's8e9RhFzue2Cy8IT0bNzOZZtTuSgwUYA77SaXD9x26Wu09NiNAMZWkWMPWwu274X',
    #     }
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Accept': '*/*',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68',
    #         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #         'Origin': 'https://team.pokio.com',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'cors',
    #         'Sec-Fetch-Dest': 'empty',
    #         'Referer': 'https://team.pokio.com/open/user/login?callback=https%3A%2F%2Fapp-test2.pokio.com%3A443%2Fadmin%2Fremote_login%3Fnext%3D%2Fmg%2Foperation%2Fupload_package&sign=e1f972b61de682c91a9df357f91a3c3c&source=pokio.app.DEV.admin',
    #         'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    #     }
    #
    #     data = {
    #         'source': 'pokio.app.DEV.admin',
    #         'username': username
    #     }
    #
    #     Re_ma = requests.post('https://team.pokio.com/admin/pin/send', headers=headers, cookies=cookies, data=data)
    #     print(
    #         '===================================================\n',
    #         Re_ma,
    #         '\n',
    #         #json.loads(response.text))
    #         Re_ma.text,
    #         '\n',
    #         '===================================================\n',
    #         )

    # def get_sign(self):
    #     Re_get = requests.get('https://team.pokio.com/open/user/login?callback=https%3A%2F%2Fapp-test2.pokio.com%3A443%2Fadmin%2Fremote_login%3Fnext%3D%2Fmg%2Fmtt_official&sign=e9b3ac5709fc9432fbc83b67608d4dff&source=pokio.app.DEV.admin')
    #     html=etree.HTML(Re_get.text)
    #     # 初始化生成一个XPath解析对象
    #     # 初始元素 = <input type="hidden" name="csrfmiddlewaretoken" value="q7g6Nfo2Vs5kp25QXSyGBgGChvRz29UE56U7TBS0tkZcR3afKhx6JBDVdXvNym01">
    #     # 获取到Value的path = //*[@id="login-form"]/input/@value
    #
    #     Token_dict=html.xpath('//*[@id="login-form"]/input/@value')
    #     for i in Token_dict:#提取字典内容
    #         csrfmiddlewaretoken=str(i)#转化成str格式
    #         print(csrfmiddlewaretoken)
    #         return csrfmiddlewaretoken#赋值csrfmiddlewaretoken

    # def Crm_login(self,csrfmiddlewaretoken):
    #     # cookies = {
    #     #     'csrftoken': 's8e9RhFzue2Cy8IT0bNzOZZtTuSgwUYA77SaXD9x26Wu09NiNAMZWkWMPWwu274X',
    #     # }
    #
    #     headers = {
    #         'Connection': 'keep-alive',
    #         'Cache-Control': 'max-age=0',
    #         'Upgrade-Insecure-Requests': '1',
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68',
    #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #         'Sec-Fetch-Site': 'same-origin',
    #         'Sec-Fetch-Mode': 'navigate',
    #         'Sec-Fetch-User': '?1',
    #         'Sec-Fetch-Dest': 'document',
    #         'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    #         'Referer': 'https://team.pokio.com/open/user/login?callback=https%3A%2F%2Fapp-test2.pokio.com%3A443%2Fadmin%2Fremote_login%3Fnext%3D%2Fmg%2Foperation%2Fupload_package&sign=e1f972b61de682c91a9df357f91a3c3c&source=pokio.app.DEV.admin',
    #         'Origin': 'https://team.pokio.com',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'Content-Type': 'application/x-www-form-urlencoded',
    #         'authority': 'app-test2.pokio.com',
    #         'cache-control': 'max-age=0',
    #         'upgrade-insecure-requests': '1',
    #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68',
    #         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #         'sec-fetch-site': 'same-site',
    #         'sec-fetch-mode': 'navigate',
    #         'sec-fetch-user': '?1',
    #         'sec-fetch-dest': 'document',
    #         'referer': 'https://team.pokio.com/open/user/login?callback=https%3A%2F%2Fapp-test2.pokio.com%3A443%2Fadmin%2Fremote_login%3Fnext%3D%2Fmg%2Foperation%2Fupload_package&sign=e1f972b61de682c91a9df357f91a3c3c&source=pokio.app.DEV.admin',
    #         'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    #         'cookie': 'sessionid=vbo3n4st6w7b2t58io8du32tcgzfiybu',
    #     }
    #
    #     params = (
    #         ('callback', 'https://app-test2.pokio.com:443/admin/remote_login?next=/mg/operation/upload_package'),
    #         ('sign', 'e1f972b61de682c91a9df357f91a3c3c'),
    #         ('source', 'pokio.app.DEV.admin'),
    #     )
    #
    #     data = [
    #         ('source', 'pokio.app.DEV.admin'),
    #         ('source', 'pokio.app.DEV.admin'),
    #         ('username', username),
    #         ('username', username),
    #         ('username', username),
    #         ('csrfmiddlewaretoken', csrfmiddlewaretoken),
    #         ('password', password),
    #         ('next', ''),
    #         ('pin', input('请输入钉钉收到的6位数验证码：')),
    #     ]
    #
    #     Re_login = requests.post('https://team.pokio.com/open/user/login', headers=headers, params=params, #cookies=cookies,
    #                              data=data)
    #     print(
    #         '===================================================\n',
    #         Re_login,
    #         '\n',
    #         #json.loads(response.text))
    #         Re_login.text,
    #         '\n',
    #         '===================================================\n',
    #         )

    def Mtt_Create(
            self,
            url,
            game_type='Holdem',
            binds_up='3',
            event_fee='2',
            service_fee='1',
            player_min='11',
            late_reg='10',
            rebuy_times='2',
            prize_guranteed='',
            add_on='1',
            break_time='0',
            first_break_time_blind_level='0',
            break_time_interval_level='0'):
        #默认值
        T1 = time.gmtime(time.time() + 1800)  # 获取当前时间+30分钟
        start_time = time.strftime("%Y-%m-%d %H:%M", T1)
        # 转换成服务器接收的格式，目前固定+1天保证可以创建成功
        cookies = {
            # if host == 'test2':
            #     'csrftoken': csrftoken,
            #     'sessionid': sessionid,
            # else:
                'csrftoken': 'wubwx3esdkk5bnNd3m93N4ejVIj8A7hc3nMKqsk89doummxag8aACXBJPeHOPXDS',
                'sessionid': 'yrzua5tvxcnm4vwat6045n4uuyfym411',
        }

        headers = {
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36 Edg/81.0.416.64',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': url,
            'Referer': f'{url}/mg/mtt_official?tag1=mtt&tag2=match',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        }

        data = {
          'event_name': f'赛事{time.time()}',
          'event_desc': '不需要支持手动输入，也暂不支持手动，如需要支持，你自己去创建吧hhh，烦死了要50个字符还差几个好吧',
          'game_type': game_type,
          'binds_up': binds_up,
          'start_stakes': '100',
          'event_fee': event_fee,
          'service_fee': service_fee,
          'start_time': start_time,
          'player_min': player_min,
          'late_reg': late_reg,
          'rebuy_times': rebuy_times,
          'prize_guranteed': prize_guranteed,
          'visibility': '3',
          'alliance_id': '',
          'club_id': '',
          'blind_structure': 'Turbo',
          'table_size': '9',
          'add_on': add_on,
          'is_halftime': '0',
          'restrict_gps_ip': '0',
          'hide_players_stats': '0',
          'ticket_only': '0',
          'break_time': break_time,
          'first_break_time_blind_level': first_break_time_blind_level,
          'break_time_interval_level': break_time_interval_level,
          'custom_payout_structure': '1',
          'clone_switch': '0',
          'custom_payout_info': '[]'
        }

        Re_Create = requests.post(f'{url}/mg/mtt_official', headers=headers, cookies=cookies, data=data, verify=False,timeout=10)
        msg = json.loads(Re_Create.text)#json化
        print(
            '===================================================\n',
            Re_Create,
            '\n',
            #json.loads(response.text))
            Re_Create.text,
            '\n',
            '===================================================\n',
            )
        #输出发送的回包内容
        if Re_Create.status_code == 200:
            if msg["error_msg"] == '':#error_msg为空时，赛事已满
                print('等会！！服务器赛事上限又满了，去删一点')
            else:
                print('创建成功，请去游戏内检查赛事')
                event_uuid = msg["error_msg"]['event_uuid']
                event_id = msg["error_msg"]['event_id']
                print('event_uuid,event_id为：', event_uuid, event_id)
                #获取2个赛事id
                Mtt_control.register_MTT(self, url, event_uuid, event_id)
        else:
            print('消息发送失败，请根据信息检查参数')
        #判断信息是否发送成功，或者服务器MTT进程已满

    def register_MTT(self,url,event_uuid,event_id):
        uid = input('请输入UID，按照后台报名格式提交，输入0退出：')
        headers = {
            'Connection': 'keep-alive',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 Edg/81.0.416.68',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': f'{url}',
            'Referer': f'{url}/mg/mtt_event_list?tag1=mtt&tag2=event',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        }

        data = {
            'method': 'enroll',
            'event_id': event_id,
            'uid': uid,
            'ticket_no': '',
            'event_uuid': event_uuid
        }

        Re_re = requests.post(f'{url}/mg/mtt_event_list', headers=headers, data=data, verify=False)
        if uid == '0':
            print(
                '===================================================\n',
                Re_re,
                '\n',
                '===================================================\n',
                '拜拜'
                )
            #输出发送的回包内容
        else:
            Mtt_control.register_MTT(self,url,event_uuid, event_id)

if __name__=='__main__':
    print(
        '创建说明：\n'
        '1、此脚本只能执行内网官方赛事的创建\n'
        '2、时间默认+30分钟，由于内容有缩短开赛配置，故一般为3分钟后开赛\n'
        '3、赛事名称和详情暂不支持手动输入，后续有需求开放\n'
        '4、默认都是测试赛，其他方式的请手动创建\n'
        '5、默认是浮动现金，其他方式请手动创建\n'
        '6、已支持同步报名\n'
    )
    # 开局提示
    host = input("请输入服务器地址后3位，例如 180：")
    # 第一步获取服务器
    if host == "test2":
        # url = 'https://app-test2.pokio.com'#test2地址有域名
        # username=input('请输入你的账号：')
        # password=input('请输入你的密码：')
        # Sent_ma()    #执行发送验证码
        # Crm_login(get_sign())    #执行登陆验证   #获取csrfmiddlewaretoken
        print('别整些没用的')
    else:
        url = f'http://192.168.101.{host}:8109'
    # 第二部给出创桌的url
    mode = input("请选择创建方式，输入0为默认德州，输入1为默认PLO，输入2为自定义配置：")
    # 选择模式
    if mode == "0":
        game_type = 'Holdem'
    elif mode == "1":
        game_type = 'Omaha'
    else:
        if mode == "2":
            game_type = input("请输入模式'Holdem'或者'Omaha':")
            # 自定义情况下需要自己输入模式
            binds_up = input("请输入涨盲时间(min)，需要整数:")
            event_fee = input("请输入报名费,最多支持2位小数:")
            service_fee = input("请输入服务费,最多支持2位小数:")
            player_min = input('请输入最小开赛人数，需要整数：')
            late_reg = input("请输入延迟报名级别，最多15:")
            rebuy_times = input("请输入重构次数，1~5或者99:")
            prize_guranteed = input("请输入保底奖池:")
            add_on = input("请输入增购次数，0或1:")
            break_time = input("请输入是否打开BT，0或1（关闭或打开）:")
            if break_time == "1":  # BT时间选择0的时候直接跳过
                first_break_time_blind_level = input("请按规则输入开始的休息时间级别:")
                break_time_interval_level = input("请按规则输入休息时间间隔:")
    RunMtt=Mtt_control(
        url,
        game_type,
        binds_up,
        event_fee,
        service_fee,
        player_min,
        late_reg,
        rebuy_times,
        prize_guranteed,
        add_on,
        break_time,
        first_break_time_blind_level,
        break_time_interval_level,
        event_uuid,
        event_id
    )
    RunMtt.Mtt_Create()