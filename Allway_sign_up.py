# -*- encoding=utf8 -*-
__author__ = "Morrow"

import time
import traceback
import pickle
import skip_error
from Requests_pokio import *
from decorator import *
from airtest.core.api import *
from airtest.core.api import connect_device
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
dev = connect_device("Android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH")#夜神模拟器1
# dev1 = connect_device("Android://127.0.0.1:5037/ORYTDMMB5PJRDE7D")  # OPPO R1
poco = AndroidUiautomationPoco(dev)
# set_current(0)
# use javacap:解决IDE中手机画面黑屏的问题
# use ADB orientation ：解决屏幕旋转问题
# use ADB touch：解决无法点击的问题

def Normol_sign_up():
    try:
        start_app("com.qfun.pokio")
        poco("com.qfun.pokio:id/tv_sign_up").wait(10).click()
        #===========进入注册界面===============
        poco("com.qfun.pokio:id/et_email_address").wait(10).set_text(email_normol)
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
        poco("com.qfun.pokio:id/tv_commit").click()
        #===========转入第二界面===============
        poco("com.qfun.pokio:id/tv_country").click()
        sleep(1)
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
        poco("com.qfun.pokio:id/tv_commit").click() 
        poco("com.qfun.pokio:id/cb_agree").wait(5).click()
        poco("com.qfun.pokio:id/tv_confirm").click()
        print("注册使用昵称：",first_name)
        print("注册完成，等待验证")
        print("进行弹窗处理")
        start_time=time.time()
        #===========注册完成===============
        if poco("com.qfun.pokio:id/txt_title_right").wait(15).exists():
            print("等元素处理")
            poco("com.qfun.pokio:id/txt_title_right").wait(15).click()
        #===========跳过导流===============
        skip_error.skip_guide()
        #===========过新手引导===============
        skip_error.skip_pop_up()
        #===========如果存在登陆弹框，跳过===============
        end_time = time.time()
        check_time = round(end_time - start_time,2)
        print('注册时间成功到点击username时间为：', check_time)
        if check_time < 60:
            poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.LinearLayout").child(
                "android.widget.RelativeLayout").offspring("com.qfun.pokio:id/main_footbar_minebtn").offspring(
                "com.qfun.pokio:id/foot_img_icon").click()
            sleep(7)
            username = poco("com.qfun.pokio:id/tv_user_name").get_text()
            # ===========进入个人信息获取角色名================
            if username == first_name:
                print(content4)
                stop_app("com.qfun.pokio")
                sleep(5)
            elif username == 'Username':
                stop_app("com.qfun.pokio")
                raise AssertionError(content1)
            # ===========角色名没有展示：可能是账号被提前删了===============
            elif username != first_name:
                stop_app("com.qfun.pokio")
                raise AssertionError(content2)
            #============错误点：角色名与创建使用的不同===============
            else:
                stop_app("com.qfun.pokio")
                sleep(5)
                print('--' * 30)
                raise AssertionError('其他用户名显示错误')
        # ===========断言成功：角色名与创建使用的相同===============
        else:
            print('由于注册时间过长（超过了60S），本次不继续验证防止触发服务器报错')
            return
    except:
        stop_app("com.qfun.pokio")
        sleep(5)
        print('--' * 30)
        traceback.print_exc()#只记录报错，不跳出
        raise#跳出，但是没有直接打印错误



def Sweden_sign_up():
    try:
        start_app("com.qfun.pokio")
        poco("com.qfun.pokio:id/tv_sign_up").wait(10).click()
        # ===========进入注册界面===============
        poco("com.qfun.pokio:id/et_email_address").wait(10).set_text(email_sweden)
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
        poco("com.qfun.pokio:id/tv_commit").click()
        # ===========转入第二界面===============
        poco("com.qfun.pokio:id/tv_country").click()
        sleep(1)
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
        poco("com.qfun.pokio:id/tv_commit").click()
        poco("com.qfun.pokio:id/cb_agree").wait(5).click()
        poco("com.qfun.pokio:id/tv_confirm").click()
        print("注册使用昵称：", 'Tomer')
        print("注册完成，等待验证")
        print("进行弹窗处理")
        start_time=time.time()
        #===========注册完成===============
        poco("com.qfun.pokio:id/txt_title_right").wait(15).click()
        #===========跳过导流===============
        skip_error.skip_guide()
        #===========通过新手引导===============
        skip_error.skip_pop_up()
        #===========如果存在登陆弹框，跳过===============
        end_time=time.time()
        check_time = round(end_time - start_time, 2)
        print('注册时间成功到点击username时间为：',check_time)
        if check_time < 60:
            poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.LinearLayout").child(
                "android.widget.RelativeLayout").offspring("com.qfun.pokio:id/main_footbar_minebtn").offspring(
                "com.qfun.pokio:id/foot_img_icon").click()
            sleep(7)
            username = poco("com.qfun.pokio:id/tv_user_name").get_text()
        # ===========进入个人信息获取角色名================
            if username == 'Tomer':
                print(content4)
                stop_app("com.qfun.pokio")
                sleep(5)
            elif username == 'Username':
                stop_app("com.qfun.pokio")
                raise AssertionError(content1)
            # ===========角色名没有展示：可能是账号被提前删了===============
            elif username != 'Tomer':
                stop_app("com.qfun.pokio")
                raise AssertionError(content2)
            # ============错误点：角色名与创建使用的不同===============
            else:
                stop_app("com.qfun.pokio")
                sleep(5)
                print('--' * 30)
                raise AssertionError('其他用户名显示错误')
        #===========断言成功：角色名与创建使用的相同===============
        else:
            print('由于注册时间过长（超过了60S），本次不继续验证防止触发服务器报错')
            return
        # ===========断言成功：角色名与创建使用的相同===============
    except:
        stop_app("com.qfun.pokio")
        sleep(5)
        traceback.print_exc()#只记录报错，不跳出
        raise#跳出，但是没有直接打印错误
#===========以上为逻辑层===============


@time_consuming
def sign_up_control_count():
    global sign_up_counter
    f = open('D:\Pokio_airtest_monitoring\pickle.txt', 'rb')
    sign_up_counter = pickle.load(f)
    f.close()
    #读取pickle文件中的counter变量值
    Maker_Error=0
    while Maker_Error<3:
        try:
            Normol_sign_up()
            Sweden_sign_up()
            sign_up_counter = sign_up_counter + 1
            print('注册模块已连续成功运行%d次！' % sign_up_counter)
        except:
            Maker_Error=Maker_Error+1
            print('连续失败：',Maker_Error)
            sleep(120)
        else:
            if sign_up_counter % 100==0:
                dingding_Disaster(offwebhook,'恭喜，注册模块已连续成功运行%d次！！！' % sign_up_counter, user=None, Atall=False)
            break
    else:
        print('注册模块连续运行%d次后失败了！' % sign_up_counter)
        sign_up_counter=0
        dingding_Disaster(webhook,'连续运行失败3次，需要检查注册模块！',user=jianyu, Atall=False)

    #运行成功count+1
    #运行失败count重置为0
    #设置count为每N次推送一次进度
    f = open('D:\Pokio_airtest_monitoring\pickle.txt', 'wb')
    pickle.dump(sign_up_counter, f)
    f.close()
    #保存counter最终的值保存至pickle
#===========以上为控制函数===============


if __name__ == '__main__' :
    # url_normol='https://app-test2.pokio.com/pybigshare/login/captcha/?email=pokioairtest@163.net'
    # url_sweden='https://app-test2.pokio.com/pybigshare/login/captcha/?email=pokiobankid@yeah.net'
    #正式服
    url_normol='https://app.pokio.com/pybigshare/login/captcha/?email=pokioairtest@163.net'
    url_sweden='https://app.pokio.com/pybigshare/login/captcha/?email=pokiobankid@yeah.net'
    #正式服域名：app.pokio.com
    email_normol='pokioairtest@163.net'
    email_sweden='pokiobankid@yeah.net'
    first_name='Airtest'
    jianyu='18675279268'# 被@人的手机号，不需要填 None
    control=False# @所有人时：true，否则为：false
    content1='用户数据没有展示'
    content2='用户数据不对应'
    content3='注册脚本运行失败'
    content4='测试点,注册验证通过'
    webhook ='https://oapi.dingtalk.com/robot/send?access_token=2ee4f0ee8a67ede67d75488aa2dff98a5ef827b1e76d20bc463e8836584ae0d4'
    # 正式服监控告警url：
    offwebhook='https: // oapi.dingtalk.com / robot / send?access_token = cb7ba6766aaef974374b305ab042650983d7b0a14384f93fa38931ba583aaa39'
    #request模块记录了所有的钉钉url
# ===========以上为本地参数===============

# sign_up_control_count()
'''
运行开关
默认==method=2跑所有注册
1，0分别对应邮箱，bankid注册
'''
#===========以上为运行脚本===============

while True:
    sign_up_control_count()
    sleep(60)
#===========循环验证，上线后屏蔽===============