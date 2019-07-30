# -*- encoding=utf8 -*-
__author__ = "Morrow"

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
def Normol_sign_up(email_normol,url_normol):
    try:
        start_app("com.qfun.pokio")
        poco("com.qfun.pokio:id/tv_sign_up").wait(10).click()
        poco("com.qfun.pokio:id/et_email_address").set_text(email_normol)
        poco("com.qfun.pokio:id/cb_terms").click()
        poco("com.qfun.pokio:id/btn_continue").click()
        poco("com.qfun.pokio:id/tv_confirm").click()
        code_details=captcha(url_normol)#获取验证码
        code_sort=0
        for i in code_details:
            if code_sort<6:
                poco("android:id/content").offspring("com.qfun.pokio:id/et_code").child("android.widget.EditText")[code_sort].set_text(i)
                code_sort=code_sort+1
        #===========6个格子填6个验证码===============
        poco("com.qfun.pokio:id/et_new_password").wait(4).set_text('Qq12345.')
        poco("com.qfun.pokio:id/et_confirm_password").set_text('Qq12345.')
        #===========密码固定‘Qq12345.’===============
        poco("com.qfun.pokio:id/btn_continue").click()
        poco("com.qfun.pokio:id/txt_title_right").click()
        #===========跳过推荐导流===============
        poco("com.qfun.pokio:id/tv_country").click()
        poco("com.qfun.pokio:id/et_search").set_text('Ice')
        poco(text="Iceland").click()
        #===========国家固定‘Iceland’===============
        poco("com.qfun.pokio:id/et_first_name").set_text('Airtest')
        poco("com.qfun.pokio:id/et_last_name").set_text('Pokio')
        poco("com.qfun.pokio:id/rb_male").click()
        poco("com.qfun.pokio:id/txt_date_of_birth").click()
        for i in range(1):
            poco("com.qfun.pokio:id/year").swipe([-0.001, 0.2])
        poco("com.qfun.pokio:id/tv_sure").click()
        #===========出生日期调整===============
        poco("android.widget.ScrollView").swipe([-0.005, -0.8388])
        poco("com.qfun.pokio:id/et_house_number").set_text("po001")
        poco("com.qfun.pokio:id/et_street").set_text("zhuanquanquan")
        poco("com.qfun.pokio:id/et_city").set_text("aidemoli")
        poco("android.widget.ScrollView").swipe([-0.005, -0.8388])
        poco("com.qfun.pokio:id/et_postal_code").wait(4).set_text('1234567890')
        poco("com.qfun.pokio:id/btn_continues").click() 
        poco("com.qfun.pokio:id/cb_agree").wait(5).click()
        poco("com.qfun.pokio:id/tv_confirm").click() 
        username=poco("com.qfun.pokio:id/tv_user_name").wait(20).get_text()
        #===========获取username===============
        print('--'*30)
        print("获取到昵称：",username)
        print("测试点：注册成功")
        if username=='Airtest':
            print("测试点：用户数据验证无误")
            print('--'*30)
            poco("com.qfun.pokio:id/btn_start").click()
            stop_app("com.qfun.pokio") 
        else:
            print("测试点：用户数据错误")
            print('--'*30)
            dingding_Disaster(webhook,content1,user=jianyu,Atall=control)
        # ===========断言失败则推送钉钉===============
    except:
        print('\n'*5+'===========   运行失败     ===============')
        dingding_Disaster(webhook,content2,user=jianyu,Atall=control)
        raise
    sleep(5)


def Sweden_sign_up(email_sweden,url_sweden):
    try:
        start_app("com.qfun.pokio")
        poco("com.qfun.pokio:id/tv_sign_up").wait(10).click()
        poco("com.qfun.pokio:id/et_email_address").set_text(email_sweden)
        poco("com.qfun.pokio:id/cb_terms").click()
        poco("com.qfun.pokio:id/btn_continue").click()
        poco("com.qfun.pokio:id/tv_confirm").click()
        code_details = captcha(url_sweden)
        code_sort = 0
        for i in code_details:
            if code_sort < 6:
                poco("android:id/content").offspring("com.qfun.pokio:id/et_code").child("android.widget.EditText")[
                    code_sort].set_text(i)
                code_sort = code_sort + 1
        # ===========6个格子填6个验证码===============
        poco("com.qfun.pokio:id/et_new_password").wait(4).set_text('Qq12345.')
        poco("com.qfun.pokio:id/et_confirm_password").set_text('Qq12345.')
        # ===========密码固定‘Qq12345.’===============
        poco("com.qfun.pokio:id/btn_continue").click()
        poco("com.qfun.pokio:id/txt_title_right").click()
        # ===========跳过推荐导流===============
        poco("com.qfun.pokio:id/tv_country").click()
        poco("com.qfun.pokio:id/et_search").set_text('swe')
        poco(text="Sweden").click()
        poco("com.qfun.pokio:id/tv_confirm").click()
        # ===========国家固定‘Sweden’=============== 
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
        username = poco("com.qfun.pokio:id/tv_user_name").wait(20).get_text()
        # ===========获取username===============
        print('--' * 30)
        print("获取到昵称：", username)
        print("测试点：注册成功")
        if username == 'Tomer':
            print("测试点：用户数据验证无误")
            print('--' * 30)
            poco("com.qfun.pokio:id/btn_start").click()
            stop_app("com.qfun.pokio")
        else:
            print("测试点：用户数据错误")
            print('--' * 30)
            dingding_Disaster(webhook,content3, user=jianyu, Atall=control)
        # ===========断言失败则推送钉钉===============
    except:
        print('\n' * 5 + '===========   运行失败     ===============')
        dingding_Disaster(webhook,content4, user=jianyu, Atall=control)
        raise
    sleep(5)
#===========以上为逻辑层===============


@time_consuming
def sign_up_control_count(method=2):
    f = open('pickle.txt', 'rb')
    sign_up_counter = pickle.load(f)
    f.close()
    #读取pickle文件中的counter变量值
    try:
        if method == 2:
            Normol_sign_up(email_normol, url_normol)
            Sweden_sign_up(email_sweden, url_sweden)
        if method == 1:
            Normol_sign_up(email_normol, url_normol)
        if method == 0:
            Sweden_sign_up(email_sweden, url_sweden)
        sign_up_counter = sign_up_counter + 1
        print('注册模块已连续成功运行%d次！' % sign_up_counter)
    except:
        sign_up_counter = 0
    else:
        if sign_up_counter % 100==0:
            dingding_Disaster(webhook,'恭喜，注册模块已连续成功运行%d次！！！' % sign_up_counter, user=None, Atall=False)
    #运行成功count+1
    #运行失败count重置为0
    #设置count为每N次推送一次进度
    f = open('pickle.txt', 'wb')
    pickle.dump(sign_up_counter, f)
    f.close()
    #保存counter最终的值保存至pickle
#===========以上为控制函数===============


if __name__ == '__main__' :
    url_normol='http://192.168.100.196:8109/pybigshare/login/captcha/?email=pokioairtest@yeah.net'
    url_sweden='http://192.168.100.196:8109/pybigshare/login/captcha/?email=pokiobankid@yeah.net'
    #正式服域名：app.pokio.com
    email_normol='pokioairtest@yeah.net'
    email_sweden='pokiobankid@yeah.net'
    jianyu='18675279268'# 被@人的手机号，不需要填 None
    control=False# @所有人时：true，否则为：false
    content1='邮箱注册后成功\n但角色验证失败\n'#推送内容
    content2='邮箱注册运行失败\n'
    content3='bankid注册成功\n但角色验证失败\n'
    content4='bankid注册运行失败\n'
    webhook ='https://oapi.dingtalk.com/robot/send?access_token=2ee4f0ee8a67ede67d75488aa2dff98a5ef827b1e76d20bc463e8836584ae0d4'
    #request模块记录了所有的钉钉url
    # ===========以上为本地参数===============
    sign_up_control_count()
    '''
    运行开关
    默认==method=2跑所有注册
    1，0分别对应邮箱，bankid注册
    '''