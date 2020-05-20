#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = "Morrow"

import pytest
import traceback
import skip_error
from airtest.core.api import *
from airtest.core.api import connect_device
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
dev_yeshen = connect_device("Android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH")#夜神模拟器1
# dev1 = connect_device("Android://127.0.0.1:5037/ORYTDMMB5PJRDE7D")  # OPPO R1
poco = AndroidUiautomationPoco(dev_yeshen)
# set_current(0)
# use javacap:解决IDE中手机画面黑屏的问题
# use ADB orientation ：解决屏幕旋转问题
# use ADB touch：解决无法点击的问题


@pytest.fixture(scope='function')
def start_stop():
    start_app("com.qfun.pokio")
    yield
    stop_app("com.qfun.pokio")
#前置条件：启动app
#后置条件：关闭app

def test_Emaillogin(start_stop):
    Email_Account = 'test20097@163.com'
    # 测试账号
    Mima = 'Qq12345.'
    # 账号密码
    Namecheck_Email = 'Niubi'
    # 测试点：账号昵称，需要对比
    try:
        poco("com.qfun.pokio:id/tv_email_address").click()
        poco("com.qfun.pokio:id/et_email").set_text(Email_Account)
        poco("com.qfun.pokio:id/et_password").set_text(Mima)
        poco("com.qfun.pokio:id/btn_login").click()
        sleep(5)
        #===========登陆账号密码固定===============
        skip_error.SkipMethod()
        #===========有登陆后的其他操作，跳过===============
        poco("android.widget.FrameLayout").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").offspring("com.qfun.pokio:id/main_footbar_minebtn").offspring("com.qfun.pokio:id/foot_img_icon").wait(20).click()
        poco("com.qfun.pokio:id/iv_user_icon").click()
        Nickname=poco("com.qfun.pokio:id/tv_user_nickname").get_text()
        #===========获取Nikename===============
        print('--'*30)
        print("获取到Nickname：",Nickname)
        print("测试点：邮箱登陆成功")
        assert Nickname==Namecheck_Email,print('测试点：登陆账号数据验证成功')
        #===========断言：获取的昵称==给定的昵称===============
        print('--'*30)
            #===========成功后直接登出===============
    except:
        print('\n'*5+'===========   运行失败     ===============')
        traceback.print_exc()
        raise
        #===========try语句运行失败，需要用raise抛出异常===============
    sleep(5)

def test_Mobilelogin(start_stop):
    Mobile_Account = '110'
    # 测试账号
    Mima = 'Qq12345.'
    # 账号密码
    Namecheck_Mobile = 'Niubi'
    # 测试点：账号昵称，需要对比
    try:
        poco("com.qfun.pokio:id/tv_mobile_number").click()
        poco("com.qfun.pokio:id/et_mobile_number").set_text(Mobile_Account)
        poco("com.qfun.pokio:id/et_password").set_text(Mima)
        poco("com.qfun.pokio:id/btn_login").click()
        sleep(5)
        #===========登陆账号密码固定===============
        skip_error.SkipMethod()
        #===========有登陆后的其他操作，跳过===============
        poco("android.widget.FrameLayout").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").offspring("com.qfun.pokio:id/main_footbar_minebtn").offspring("com.qfun.pokio:id/foot_img_icon").wait(20).click()
        poco("com.qfun.pokio:id/iv_user_icon").click()
        Nickname=poco("com.qfun.pokio:id/tv_user_nickname").get_text()
        # ===========获取Nikename===============
        print('--' * 30)
        print("获取到Nickname：", Nickname)
        print("测试点：邮箱登陆成功")
        assert Nickname == Namecheck_Mobile, print('测试点：登陆账号数据验证成功')
        # ===========断言：获取的昵称==给定的昵称===============
        print('--' * 30)
        # ===========成功后直接登出===============
    except:
        print('\n' * 5 + '===========   运行失败     ===============')
        traceback.print_exc()
        raise
        # ===========try语句运行失败，需要用raise抛出异常===============
    sleep(5)

def __test_Facebooklogin(start_stop):
    Facebook_Account = 'test20097@163.com'
    # 测试账号
    Mima = 'Qq12345.'
    # 账号密码
    Facebook_Mobile = 'Niubi'
    try:
        poco("com.qfun.pokio:id/tv_facebook_login").click()
        poco("m_login_email").wait(10).set_text(Facebook_Account)
        poco("m_login_password").set_text(Mima)
        poco("u_0_4").click()
        sleep(5)
        #===========登陆账号密码固定===============
        skip_error.SkipMethod()
        #===========有登陆后的其他操作，跳过===============
        poco("android.widget.FrameLayout").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").offspring("com.qfun.pokio:id/main_footbar_minebtn").offspring("com.qfun.pokio:id/foot_img_icon").wait(20).click()
        poco("com.qfun.pokio:id/iv_user_icon").click()
        Nickname=poco("com.qfun.pokio:id/tv_user_nickname").get_text()
        # ===========获取Nikename===============
        print('--' * 30)
        print("获取到Nickname：", Nickname)
        print("测试点：邮箱登陆成功")
        assert Nickname == Facebook_Mobile, print('测试点：登陆账号数据验证成功')
        # ===========断言：获取的昵称==给定的昵称===============
        print('--' * 30)
        # ===========成功后直接登出===============
    except:
        print('\n' * 5 + '===========   运行失败     ===============')
        traceback.print_exc()
        raise
        # ===========try语句运行失败，需要用raise抛出异常===============
    sleep(5)

if __name__ == '__main__':
    pytest.main(['test_py.py','-s','-v'])


