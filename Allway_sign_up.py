# -*- encoding=utf8 -*-
__author__ = "Morrow"

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
def Normol_sign_up(email):
    try:
        poco("com.qfun.pokio:id/tv_sign_up").click()
        poco("com.qfun.pokio:id/et_email_address").set_text(email)
        poco("com.qfun.pokio:id/cb_terms").click()
        poco("com.qfun.pokio:id/btn_continue").click()
        poco("com.qfun.pokio:id/tv_confirm").click()
        code_details=captcha()#获取验证码
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
        poco("com.qfun.pokio:id/et_house_number").set_text("po001")
        poco("com.qfun.pokio:id/et_street").set_text("zhuanquanquan")
        poco("com.qfun.pokio:id/et_city").set_text("aidemoli")
        poco("android.widget.ScrollView").swipe([0.0236, -0.2116])
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
        #===========断言注册结果,失败钉钉告警===============
    except:
        print('\n'*5+'===========   运行失败     ===============')
        dingding_Disaster(webhook,content2,user=jianyu,Atall=control)
        raise
    sleep(5)


def Sweden_sign_up(email1):
    try:
        poco("com.qfun.pokio:id/tv_sign_up").click()
        poco("com.qfun.pokio:id/et_email_address").set_text(email1)
        poco("com.qfun.pokio:id/cb_terms").click()
        poco("com.qfun.pokio:id/btn_continue").click()
        poco("com.qfun.pokio:id/tv_confirm").click()
        code_details = captcha()
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
        # ===========国家固定‘Sweden’===============         需要bankid服务器支持
        poco("com.qfun.pokio:id/et_first_name").set_text('Airtest')
        poco("com.qfun.pokio:id/et_last_name").set_text('Pokio')
        poco("com.qfun.pokio:id/rb_male").click()
        poco("com.qfun.pokio:id/txt_date_of_birth").click()
        for i in range(1):
            poco("com.qfun.pokio:id/year").swipe([-0.001, 0.2])
        poco("com.qfun.pokio:id/tv_sure").click()
        # ===========出生日期调整===============
        poco("com.qfun.pokio:id/et_house_number").set_text("po001")
        poco("com.qfun.pokio:id/et_street").set_text("zhuanquanquan")
        poco("com.qfun.pokio:id/et_city").set_text("aidemoli")
        poco("com.qfun.pokio:id/et_postal_code").wait(4).set_text('1234567890')

        poco("com.qfun.pokio:id/btn_continues").click()
        poco("com.qfun.pokio:id/cb_agree").wait(5).click()
        poco("com.qfun.pokio:id/tv_confirm").click()
        username = poco("com.qfun.pokio:id/tv_user_name").wait(20).get_text()
        # ===========获取username===============
        print('--' * 30)
        print("获取到昵称：", username)
        print("测试点：注册成功")
        if username == 'Airtest':
            print("测试点：用户数据验证无误")
            print('--' * 30)
            poco("com.qfun.pokio:id/btn_start").click()
            stop_app("com.qfun.pokio")
        else:
            print("测试点：用户数据错误")
            print('--' * 30)
            dingding_Disaster(webhook,content3, user=jianyu, Atall=control)
        # ===========断言注册结果,失败钉钉告警===============
    except:
        print('\n' * 5 + '===========   运行失败     ===============')
        dingding_Disaster(webhook,content4, user=jianyu, Atall=control)
        raise
    sleep(5)
#===========以上为逻辑层===============



if __name__ == '__main__' :
    email='pokioairtest@yeah.net'
    email1='pokiobankid@yeah.net'
    jianyu='18675279268'# 被@人的手机号，不需要填 None
    control=False# @所有人时：true，否则为：false
    content1='邮箱注册失败\nPlease check error'#推送内容
    content2='邮箱注册模块运行失败\nPlease check error'
    content3='bankid注册失败\nPlease check error'
    content4='bankid注册模块运行失败\nPlease check error'
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=2ee4f0ee8a67ede67d75488aa2dff98a5ef827b1e76d20bc463e8836584ae0d4'
# ===========以上为本地参数===============

@time_consuming
def sign_up_control_count(method=2):
    f = open('pickle.txt', 'rb')
    sign_up_counter = pickle.load(f)
    f.close()
    #读取pickle文件中的counter变量值
    try:
        if method == 2:
            Normol_sign_up(email)
            Sweden_sign_up(email)
        if method == 1:
            Normol_sign_up(email)
        if method == 0:
            Sweden_sign_up(email)
        sign_up_counter = sign_up_counter + 1
        print('注册模块已连续成功运行%d次！' % sign_up_counter)
    except:
        dingding_Disaster(webhook,'很遗憾，注册模块在运行%d次时出错了' % sign_up_counter, user=None, Atall=False)
        sign_up_counter = 0
    else:
        if sign_up_counter % 100==0:
            dingding_Disaster(webhook,'注册模块已连续成功运行%d次！！！' % sign_up_counter, user=None, Atall=False)
    #运行成功count+1
    #运行失败count重置为0
    #设置count为每N次推送一次进度
    f = open('pickle.txt', 'wb')
    pickle.dump(sign_up_counter, f)
    f.close()
    #保存counter最终的值保存至pickle
#===========以上为控制层===============

sign_up_control_count()
'''
运行开关
默认==method=2跑所有注册
1，0分别对应邮箱，bankid注册
'''
