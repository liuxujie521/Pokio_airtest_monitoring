# -*- encoding=utf8 -*-
__author__ = "Morrow"

import traceback
import pickle
from Requests_pokio import *
from decorator import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# dev1 = connect_device("Android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH")#夜神模拟器1
# set_current(0)
# use javacap:解决IDE中手机画面黑屏的问题
# use ADB orientation ：解决屏幕旋转问题
# use ADB touch：解决无法点击的问题

def Email_login():
    try:
        poco("com.qfun.pokio:id/tv_email_address").click()
        poco("com.qfun.pokio:id/et_email").set_text(Email_Account)
        poco("com.qfun.pokio:id/et_password").set_text('Qq12345.')
        poco("com.qfun.pokio:id/btn_login").click()
        #===========登陆账号密码固定===============
        poco("android.widget.FrameLayout").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").offspring("com.qfun.pokio:id/main_footbar_minebtn").offspring("com.qfun.pokio:id/foot_img_icon").wait(20).click()
        poco("com.qfun.pokio:id/iv_user_icon").click()
        Nickname=poco("com.qfun.pokio:id/tv_user_nickname").get_text()
        #===========获取Nikename===============
        print('--'*30)
        print("获取到Nickname：",Nickname)
        print("测试点：邮箱登陆成功")
        if Nickname==Namecheck_Email:
        #===========断言：获取的昵称==给定的昵称===============
            print("测试点：登陆账号数据验证成功")
            print('--'*30)
            poco("com.qfun.pokio:id/iv_title_left").click()
            poco(text="Settings").click()
            poco("android.widget.ScrollView").swipe([0.0236, -0.2116])
            poco("com.qfun.pokio:id/tv_logout").click()
            poco("com.qfun.pokio:id/btn_select_exit").click()
            #===========成功后直接登出===============
        else:
            raise AssertionError("测试点：登陆账号数据验证失败")
            # ===========断言失败则推送钉钉===============
    except:
        print('\n'*5+'===========   运行失败     ===============')
        traceback.print_exc()
        raise
        #===========try语句运行失败，需要用raise抛出异常===============
    sleep(5)
        
        
def Mobile_login():
    try:
        poco("com.qfun.pokio:id/tv_mobile_number").click()
        poco("com.qfun.pokio:id/et_mobile_number").set_text(Mobile_Account)
        poco("com.qfun.pokio:id/et_password").set_text('Qq12345.')
        poco("com.qfun.pokio:id/btn_login").click()
        #===========登陆账号密码固定===============
        poco("android.widget.FrameLayout").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").offspring("com.qfun.pokio:id/main_footbar_minebtn").offspring("com.qfun.pokio:id/foot_img_icon").wait(20).click()
        poco("com.qfun.pokio:id/iv_user_icon").click()
        Nickname=poco("com.qfun.pokio:id/tv_user_nickname").get_text()
        #===========获取Nikename===============
        print('--'*30)
        print("获取到Nickname：",Nickname)
        print("测试点：手机登陆成功")
        if Nickname==Namecheck_Mobile:
        #===========断言：获取的昵称==给定的昵称===============
            print("测试点：登陆账号数据验证成功")
            print('--'*30)
            poco("com.qfun.pokio:id/iv_title_left").click()
            poco(text="Settings").click()
            poco("android.widget.ScrollView").swipe([0.0236, -0.2116])
            poco("com.qfun.pokio:id/tv_logout").click()
            poco("com.qfun.pokio:id/btn_select_exit").click()
            #===========成功后直接登出===============
        else:
            raise AssertionError("测试点：登陆账号数据验证失败")
            # ===========断言失败则推送钉钉===============
    except:
        print('\n'*5+'===========   运行失败     ===============')
        traceback.print_exc()
        raise
        #===========try语句运行失败，需要用raise抛出异常===============
    sleep(5)
        
        
def Facebook_login():
    try:
        poco("com.qfun.pokio:id/tv_facebook_login").click()
        poco("m_login_email").wait(10).set_text(Facebook_Account)
        poco("m_login_password").set_text('a8164591')
        poco("u_0_4").click()
        #===========登陆账号密码固定===============
        poco("android.widget.FrameLayout").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").offspring("com.qfun.pokio:id/main_footbar_minebtn").offspring("com.qfun.pokio:id/foot_img_icon").wait(20).click()
        poco("com.qfun.pokio:id/iv_user_icon").click()
        Nickname=poco("com.qfun.pokio:id/tv_user_nickname").get_text()
        #===========获取Nikename===============
        print('--'*30)
        print("获取到Nickname：",Nickname)
        print("测试点：第三方登陆成功")
        if Nickname==Namecheck_Facebook:
        #===========断言：获取的昵称==给定的昵称===============
            print("测试点：登陆账号数据验证成功")
            print('--' * 30)
            poco("com.qfun.pokio:id/iv_title_left").click()
            poco(text="Settings").click()
            poco("android.widget.ScrollView").swipe([0.0236, -0.2116])
            poco("com.qfun.pokio:id/tv_logout").click()
            poco("com.qfun.pokio:id/btn_select_exit").click()
            #===========成功后直接登出===============
        else:
            raise AssertionError("测试点：登陆账号数据验证失败")
            # ===========断言失败则推送钉钉===============
    except:
        print('\n'*5+'===========   运行失败     ===============')
        traceback.print_exc()
        raise
        #===========try语句运行失败，需要用raise抛出异常===============
    sleep(5)

def skip_fingerprint():
    pass

#===========以上为逻辑层===============


@time_consuming
def login_control_count():
    global login_counter
    f = open('D:\GitHub\Pokio_airtest_monitoring\pickle.txt', 'rb')
    login_counter = pickle.load(f)
    f.close()
    #读取pickle文件中的counter变量值
    Maker_Error=0
    while Maker_Error<3:
        try:
            start_app("com.qfun.pokio")
            Email_login()
            Mobile_login()
            Facebook_login()
            stop_app("com.qfun.pokio")
            login_counter = login_counter + 1
            print('登陆模块已连续成功运行%d次！' % login_counter)
        except:
            Maker_Error=Maker_Error+1
            print('连续失败：', Maker_Error)
            login_counter = 0
            stop_app("com.qfun.pokio")
        else:
            if login_counter % 100==0:
                dingding_Disaster(webhook,'登陆模块已连续成功运行%d次！！！' % login_counter, user=None, Atall=False)
            break
    else:
        print('登陆模块连续运行%d次后失败了！' % login_counter)
        login_counter=0
        dingding_Disaster(webhook, '连续运行失败3次，需要检查注登陆模块！', user=jianyu, Atall=False)
        return
    #运行成功count+1
    #运行失败count重置为0
    #设置count为每N次推送一次进度
    f = open('D:\GitHub\Pokio_airtest_monitoring\pickle.txt', 'wb')
    pickle.dump(login_counter, f)
    f.close()
    #保存counter最终的值保存至pickle
#===========以上为控制函数===============


if __name__ == '__main__' :
    Email_Account='test0130@163.com'
    Mobile_Account='18566787073'
    Facebook_Account='babysme@vip.qq.com'
    jianyu='18675279268'# 被@人的手机号，不需要填 None
    control=False# @所有人时：true，否则为：false
    content1='邮箱登陆成功\n但角色信息验证失败\n'
    content2='邮箱登陆运行失败\n'
    content3='手机登陆成功\n但角色信息验证失败\n'
    content4='手机登陆运行失败\n'
    content5='第三方登陆成功\n但角色信息验证失败\n'
    content6='第三方登陆运行失败\n'
    Namecheck_Email='test0130'
    Namecheck_Mobile='test0133'
    Namecheck_Facebook='Airtest'
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=2ee4f0ee8a67ede67d75488aa2dff98a5ef827b1e76d20bc463e8836584ae0d4'
    #该推送为测试群，request模块记录了正式群的钉钉url
# ===========以上为本地参数===============

login_control_count()
'''
运行开关
默认==method=3跑所有登陆
2，1，0分别对应邮箱，手机，facebook登陆
'''
#===========以上为运行脚本===============
# while True:
#     login_control_count()
#     sleep(20)
#===========循环验证，上线后屏蔽===============