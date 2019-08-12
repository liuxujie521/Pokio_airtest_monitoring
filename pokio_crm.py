# -*- encoding=utf8 -*-
__author__ = "zhouming"

# coding:utf-8

from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import time
from decorator import *

class PokioCRMDashboardMethod(object):
    """CRM后台玩家余额调整"""

    def __init__(self):
        """实例化driver"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def Wallet_string_processing(self,walletstr):
        """钱包字符串转换数值类型处理方法"""
        if '€' in walletstr:
            walletstr = walletstr.strip('€')
            walletstr = walletstr.replace(',', '')
            walletfloat = float(walletstr)
            number = round(walletfloat, 2)
            return number
    def CRM_User_Login(self):
        """CRM后台登录"""
        # CRM的Search User界面
        try:
            self.driver.get("https://crm-test2.pokio.com/crm/") # URL
            # driver.get("http://192.168.100.196:8119/crm/")  # URL
            sleep(2)
            self.driver.find_element_by_name('username').send_keys("zhouming")
            self.driver.find_element_by_name('password').send_keys('evtb6i8cpv')
            # driver.find_element_by_id('id_pin').send_keys('808287')
            self.driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/input').click() #登录按键
            sleep(1)
        except:
            print("CRM登录异常")
        else:
            print("CRM登录成功")

    def CRM_user_screen(self,userid):
        """筛选要操作的用户跳转个人资料页"""
        sleep(2)
        print("进入了CRM搜索筛选页")
        sreach_window = self.driver.current_window_handle
        print("当前切换的widowid：", sreach_window)
        print("11111111111111")
        self.driver.find_element_by_id('id_uid').clear()  # 清空搜索框数据
        self.driver.find_element_by_id('id_uid').send_keys(userid)  # 对Search Users的ID输入框输入21202
        self.driver.find_element_by_xpath('//*[@id="id_crm_index"]/div[2]/div[8]/button').click()  # 点击Search确认
        # sreach_window = driver.current_window_handle
        self.driver.find_element_by_link_text(userid).click()  # 点击搜索出的21202进入个人详情面》》跳转到第二页
        # sreach_window = driver.current_window_handle
        # print("sreach_window: ",sreach_window)
        sleep(3)
        print("多窗口定位切换处理")
        all_window = self.driver.window_handles
        print("all[0]:::", all_window[0])
        print("all[1]:::", all_window[1])
        # for window in all_window:
        #     print("----------------------")
        #     print("window:::",window)
        #     if window != sreach_window:
        #         driver.switch_to.window(window)
        # sreach_window = driver.current_window_handle
        self.driver.switch_to.window(all_window[1])  #切换到第二个窗口

        walletstr = self.driver.find_element_by_xpath("/*//span[@id='gold']").text  # 获取当前用户的余额值
        print("字符类型余额：", walletstr, type(walletstr))
        numfloat = self.Wallet_string_processing(walletstr)
        print("数字类型余额: ", numfloat, type(numfloat))
        sleep(2)
        return numfloat     #返回用户当前余额数据

    def CRM_money_adjustment(self,usermoney):#带入用户当前的余额进行调整操作
        """后台对相应账号的余额调整"""
        # 账号筛选功能
        if usermoney !=0.00:  #如果余额不是为0
            print("当前用户余额非0")
            self.driver.find_element_by_xpath("/*//span[@id='gold']/../button").click()
            sleep(2)
            strnumtt="-"+ str(usermoney)    #类型转换成str
            print("填入要减的余额::",strnumtt)
            self.driver.find_element_by_id("id_gold").clear()
            self.driver.find_element_by_id("id_gold").send_keys(strnumtt)  # 对Real Money Balance输入框输入
            self.driver.implicitly_wait(10)
            Select(self.driver.find_element_by_id('modify_reason')).select_by_visible_text('Test')
            self.driver.find_element_by_id("remarks_gold").clear()  # 备注清空
            self.driver.find_element_by_id("remarks_gold").send_keys("python automatied testing ")  # 备注输入框输入
            self.driver.find_element_by_id("confirmA").click()           # 点击确认
            self.driver.find_element_by_id("confirm_save").click()     # 点击Yes确认
            ####################################
            sleep(3)
            self.driver.find_element_by_xpath("/*//span[@id='gold']/../button").click()
            print(self.driver.find_element_by_xpath("/*//span[@id='gold']").text)
            sleep(2)
            self.driver.find_element_by_id("id_gold").clear()
            self.driver.find_element_by_id("id_gold").send_keys("+25")  # 对Real Money Balance输入框输入+25
            self.driver.implicitly_wait(10)
            Select(self.driver.find_element_by_id('modify_reason')).select_by_visible_text('Test')
            self.driver.find_element_by_id("remarks_gold").clear()
            self.driver.find_element_by_id("remarks_gold").send_keys("python automatied testing ")  # 备注输入框输入
            self.driver.find_element_by_id("confirmA").click()  # 点击确认
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_id("confirm_save").click()  # 点击Yes确认
        else:   #用户余额为0.00时，直接加钱到25
            print("当前用户余额为0")
            self.driver.find_element_by_xpath("/*//span[@id='gold']/../button").click()
            print(self.driver.find_element_by_xpath("/*//span[@id='gold']").text)
            sleep(2)
            self.driver.find_element_by_id("id_gold").clear()  # 清空输入框
            self.driver.find_element_by_id("id_gold").send_keys("+25")  # 对Real Money Balance输入框输入+25
            self.driver.implicitly_wait(10)
            Select(self.driver.find_element_by_id('modify_reason')).select_by_visible_text('Test')
            self.driver.find_element_by_id("remarks_gold").clear()  # 备注清空
            self.driver.find_element_by_id("remarks_gold").send_keys("python automatied testing ")  # 备注输入框输入
            self.driver.find_element_by_id("confirmA").click()           # 点击确认
            print("Yes确认")
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_id("confirm_save").click()     # 点击Yes确认
        all_window = self.driver.window_handles
        print("all[0]:::", all_window[0])
        print("all[1]:::", all_window[1])
        # for window in all_window:
        #     print("----------------------")
        #     print("window:::",window)
        #     if window != sreach_window:
        #         driver.switch_to.window(window)
        # sreach_window = driver.current_window_handle
        print("关闭前打印：",all_window)
        self.driver.close()  #关闭当前窗口
        self.driver.switch_to.window(all_window[0])  # 切换到第二个窗口
        sreach_window = self.driver.current_window_handle
        print("当前切换的：",sreach_window)

    @time_consuming
    def CRM_main(slef):
        """初始要修改的玩家"""
        user_id11="21091"   #ming333@163.com
        user_id22="21101"   #ming444@qq.com
        # driver.get("http://192.168.100.196:8119/crm/")  # URL
        print("CRM登录")

        slef.CRM_User_Login()  #登录CRM后台
        sleep(1)
        print("调整第一个用户余额")
        moneyfloat = slef.CRM_user_screen(user_id11) # 通过ID筛选要操作的用户并跳转个人资料页
        slef.CRM_money_adjustment(moneyfloat)        # 调整用户的余额（25）
        print("调整第二个用户余额")
        moneyfloat = slef.CRM_user_screen(user_id22)
        slef.CRM_money_adjustment(moneyfloat)
        slef.driver.quit()

