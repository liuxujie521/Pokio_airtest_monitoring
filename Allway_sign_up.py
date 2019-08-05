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
def Normol_sign_up():
    global result
    result=True
    try:
        start_app("com.qfun.pokio")
        poco("com.qfun.pokio:id/tv_sign_up").wait(10).click()
        #===========进入注册界面===============
        poco("com.qfun.pokio:id/et_email_address").set_text(email_normol)
        poco("com.qfun.pokio:id/et_pwd").set_text('Qq12345.')
        poco("com.qfun.pokio:id/et_confirm_pwd").set_text('Qq12345.')
        #===========密码固定‘Qq12345.’===============
        poco("com.qfun.pokio:id/tv_send_code").click()
        poco("com.qfun.pokio:id/tv_confirm").click()
        #===========发送验证码===============
        code_details=captcha(url_normol)#captcha函数调用接口直接获取验证码
        poco("com.qfun.pokio:id/et_code").set_text(code_details)
        #===========填入验证码===============
        poco("com.qfun.pokio:id/cb_terms").click()#勾选协议
        poco("com.qfun.pokio:id/btn_continue").click()
        #===========转入第二界面===============
        poco("com.qfun.pokio:id/tv_country").click()
        poco("com.qfun.pokio:id/et_search").set_text('Ice')
        poco(text="Iceland").click()
        #===========国家固定‘Iceland’===============
        poco("com.qfun.pokio:id/et_first_name").set_text(first_name)
        poco("com.qfun.pokio:id/et_last_name").set_text('Pokio')
        poco("com.qfun.pokio:id/rb_male").click()
        poco("com.qfun.pokio:id/txt_date_of_birth").click()
        for i in range(1):
            poco("com.qfun.pokio:id/year").swipe([-0.001, 0.2])
        poco("com.qfun.pokio:id/tv_sure").click()
        #===========出生日期调整===============
        poco("android.widget.ScrollView").swipe([-0.005, -0.8388])#多次下滑操作，防止小分配率机型无法显示下半部分
        poco("com.qfun.pokio:id/et_house_number").set_text("po001")
        poco("com.qfun.pokio:id/et_street").set_text("zhuanquanquan")
        poco("com.qfun.pokio:id/et_city").set_text("aidemoli")
        poco("android.widget.ScrollView").swipe([-0.005, -0.8388])#多次下滑操作，防止小分配率机型无法显示下半部分
        poco("com.qfun.pokio:id/et_postal_code").wait(4).set_text('1234567890')
        poco("com.qfun.pokio:id/btn_continues").click() 
        poco("com.qfun.pokio:id/cb_agree").wait(5).click()
        poco("com.qfun.pokio:id/tv_confirm").click()
        print('--'*30)
        print("注册使用昵称：",first_name)
        print("注册完成，等待验证")
        print('--'*30)
        #===========注册完成===============
        poco("com.qfun.pokio:id/txt_title_right").wait(15).click()
        #===========跳过导流===============
        sleep(5)
        while poco("com.qfun.pokio:id/iv_next").exists():
            poco("com.qfun.pokio:id/iv_next").click()
        #===========通过新手引导===============
        poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").offspring("com.qfun.pokio:id/main_footbar_minebtn").offspring("com.qfun.pokio:id/foot_img_icon").click()
        username=poco("com.qfun.pokio:id/tv_user_name").wait(20).get_text()
        if username == 'Username':
            result=False
            dingding_Disaster(webhook, content1, user=jianyu, Atall=control)
            raise AssertionError(content1)
        #===========角色名没有展示：可能是账号被提前删了===============
        elif username != first_name:
            result=False
            dingding_Disaster(webhook, content2, user=jianyu, Atall=control)
            raise AssertionError(content2)
        #===========断言失败：角色名与创建使用的不同===============
        else:
            print(content4)
            print('--' * 30)
            stop_app("com.qfun.pokio")
            sleep(5)
        #===========断言成功：角色名与创建使用的相同===============
    except:
        result = False
        print('--' * 30)
        print('运行失败，请检查traceback')
        dingding_Disaster(webhook, content3, user=jianyu, Atall=control)
        traceback.print_exc()
        stop_app("com.qfun.pokio")
        sleep(5)
        # ===========运行失败：其他一切因素都可能导致===============


def Sweden_sign_up():
    global result
    result=True
    try:
        start_app("com.qfun.pokio")
        poco("com.qfun.pokio:id/tv_sign_up").wait(10).click()
        # ===========进入注册界面===============
        poco("com.qfun.pokio:id/et_email_address").set_text(email_sweden)
        poco("com.qfun.pokio:id/et_pwd").set_text('Qq12345.')
        poco("com.qfun.pokio:id/et_confirm_pwd").set_text('Qq12345.')
        # ===========密码固定‘Qq12345.’===============
        poco("com.qfun.pokio:id/tv_send_code").click()
        poco("com.qfun.pokio:id/tv_confirm").click()
        # ===========发送验证码===============
        code_details = captcha(url_sweden)  # captcha函数调用接口直接获取验证码
        poco("com.qfun.pokio:id/et_code").set_text(code_details)
        # ===========填入验证码===============
        poco("com.qfun.pokio:id/cb_terms").click()  # 勾选协议
        poco("com.qfun.pokio:id/btn_continue").click()
        # ===========转入第二界面===============
        poco("com.qfun.pokio:id/tv_country").click()
        poco("com.qfun.pokio:id/et_search").set_text('swe')
        poco(text="Sweden").click()
        poco("com.qfun.pokio:id/tv_confirm").click()
        # ===========国家固定‘Iceland’===============
        poco("com.qfun.pokio:id/iv_title_left").click()
        poco("com.qfun.pokio:id/tv_confirm").click()
        poco("android.widget.ScrollView").swipe([-0.005, -0.8388])
        poco("com.qfun.pokio:id/et_house_number").set_text("po001")
        poco("com.qfun.pokio:id/et_street").set_text("zhuanquanquan")
        poco("com.qfun.pokio:id/et_city").set_text("aidemoli")
        poco("android.widget.ScrollView").swipe([-0.005, -0.8388])
        poco("com.qfun.pokio:id/et_postal_code").wait(4).set_text('1234567890')
        poco("com.qfun.pokio:id/btn_continues").click()
        poco("com.qfun.pokio:id/cb_agree").wait(5).click()
        poco("com.qfun.pokio:id/tv_confirm").click()
        print('--' * 30)
        print("注册使用昵称：", 'Tomer')
        print("注册完成，等待验证")
        print('--' * 30)
        # ===========注册完成===============
        poco("com.qfun.pokio:id/txt_title_right").wait(15).click()
        # ===========跳过导流===============
        sleep(5)
        while poco("com.qfun.pokio:id/iv_next").exists():
            poco("com.qfun.pokio:id/iv_next").click()
        # ===========通过新手引导===============
        poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.LinearLayout").child(
            "android.widget.RelativeLayout").offspring("com.qfun.pokio:id/main_footbar_minebtn").offspring(
            "com.qfun.pokio:id/foot_img_icon").click()
        username = poco("com.qfun.pokio:id/tv_user_name").wait(20).get_text()
        # ===========获取username===============
        if username == 'Username':
            result=False
            dingding_Disaster(webhook, content1, user=jianyu, Atall=control)
            raise AssertionError(content1)
        #===========角色名没有展示：可能是账号被提前删了===============
        elif username != 'Tomer':
            result=False
            dingding_Disaster(webhook, content2, user=jianyu, Atall=control)
            raise AssertionError(content2)
        # ===========断言失败：角色名与创建使用的不同===============
        else:
            print(content4)
            print('--' * 30)
            stop_app("com.qfun.pokio")
            sleep(5)
        # ===========断言成功：角色名与创建使用的相同===============
    except:
        result = False
        print('--' * 30)
        print('运行失败，请检查traceback')
        dingding_Disaster(webhook, content3, user=jianyu, Atall=control)
        traceback.print_exc()
        stop_app("com.qfun.pokio")
        sleep(5)
        # ===========运行失败：其他一切因素都可能导致===============

#===========以上为逻辑层===============


@time_consuming
def sign_up_control_count(method=2):
    f = open('D:\GitHub\Pokio_airtest_monitoring\pickle.txt', 'rb')
    sign_up_counter = pickle.load(f)
    f.close()
    #读取pickle文件中的counter变量值
    try:
        if method == 2:
            Normol_sign_up()
            Sweden_sign_up()
        if method == 1:
            Normol_sign_up()
        if method == 0:
            Sweden_sign_up()
        if result == False:
            raise AssertionError('连续运行记录中断')
        sign_up_counter = sign_up_counter + 1
        print('注册模块已连续成功运行%d次！' % sign_up_counter)
    except:
        print('注册模块连续运行%d次后失败了！' % sign_up_counter)
        sign_up_counter = 0
    else:
        if sign_up_counter % 100==0:
            dingding_Disaster(webhook,'恭喜，注册模块已连续成功运行%d次！！！' % sign_up_counter, user=None, Atall=False)
    #运行成功count+1
    #运行失败count重置为0
    #设置count为每N次推送一次进度
    f = open('D:\GitHub\Pokio_airtest_monitoring\pickle.txt', 'wb')
    pickle.dump(sign_up_counter, f)
    f.close()
    #保存counter最终的值保存至pickle
#===========以上为控制函数===============


if __name__ == '__main__' :
    url_normol='https://app-test2.pokio.com/pybigshare/login/captcha/?email=pokioairtest@yeah.net'
    url_sweden='https://app-test2.pokio.com/pybigshare/login/captcha/?email=pokiobankid@yeah.net'
    #正式服域名：app.pokio.com
    email_normol='pokioairtest@yeah.net'
    email_sweden='pokiobankid@yeah.net'
    first_name='Airtest'
    jianyu='18675279268'# 被@人的手机号，不需要填 None
    control=False# @所有人时：true，否则为：false
    content1='用户数据没有展示'
    content2='用户数据不对应'
    content3='注册脚本运行失败'
    content4='测试点,注册验证通过'
    webhook ='https://oapi.dingtalk.com/robot/send?access_token=2ee4f0ee8a67ede67d75488aa2dff98a5ef827b1e76d20bc463e8836584ae0d4'
    #request模块记录了所有的钉钉url
# ===========以上为本地参数===============

sign_up_control_count()
'''
运行开关
默认==method=2跑所有注册
1，0分别对应邮箱，bankid注册
'''
#===========以上为运行脚本===============

# while True:
#     sign_up_control_count()
#     sleep(20)
#===========循环验证，上线后屏蔽===============