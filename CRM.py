# coding:utf-8

from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import time
driver = webdriver.Chrome()
driver.maximize_window()


def Wallet_string_processing(walletstr):
    """钱包字符串转换数值类型处理方法"""
    if '€' in walletstr:
        walletstr = walletstr.strip('€')
        walletstr = walletstr.replace(',', '')
        walletfloat = float(walletstr)
        number = round(walletfloat, 2)
        return number

def CRM_money_adjustment():
    # CRM的Search User界面
    # driver.get("https://crm-test2.pokio.com/crm/")
    driver.get("http://192.168.100.196:8119/crm/")
    #
    # sleep(2)

    # CRM登录界面
    #
    # driver.find_element_by_name('username').send_keys("fengjiacheng")
    # driver.find_element_by_name('password').send_keys('fengjc123..')
    # driver.find_element_by_id('id_pin').send_keys('808287')
    # driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/input').click()
    # sleep(1)

    # 账号筛选功能
    driver.find_element_by_id('id_uid').send_keys("20455") # 对Search Users的ID输入框输入21202
    driver.find_element_by_xpath('//*[@id="id_crm_index"]/div[2]/div[8]/button').click() # 点击Search确认
    sreach_window = driver.current_window_handle
    driver.find_element_by_link_text("20455").click() # 点击搜索出的21202进入个人详情面》》跳转到第二页
    sleep(3)
    print("多窗口定位切换处理")
    all_window = driver.window_handles
    for window in all_window:
        if window != sreach_window:
            driver.switch_to.window(window)
    sreach_window = driver.current_window_handle
    walletstrtt=driver.find_element_by_xpath("/*//span[@id='gold']").text   #获取当前用户的余额值
    print("字符类型余额：",walletstrtt,type(walletstrtt))
    numtttt=Wallet_string_processing(walletstrtt)
    print("数字类型余额: ",numtttt,type(numtttt))
    sleep(2)
    if numtttt !=0.00:  #如果余额不是为0
        driver.find_element_by_xpath("/*//span[@id='gold']/../button").click()
        sleep(2)
        strnumtt="-"+ str(numtttt)
        print("填入要减的余额::",strnumtt)
        driver.find_element_by_id("id_gold").clear()
        driver.find_element_by_id("id_gold").send_keys(strnumtt)  # 对Real Money Balance输入框输入+100
        driver.implicitly_wait(10)
        Select(driver.find_element_by_id('modify_reason')).select_by_visible_text('Test')
        driver.find_element_by_id("remarks_gold").clear()  # 备注清空
        driver.find_element_by_id("remarks_gold").send_keys("python automatied testing ")  # 备注输入框输入
        driver.find_element_by_id("confirmA").click()           # 点击确认
        driver.find_element_by_id("confirm_save").click()     # 点击Yes确认
        ####################################
        sleep(3)
        driver.find_element_by_xpath("/*//span[@id='gold']/../button").click()
        print(driver.find_element_by_xpath("/*//span[@id='gold']").text)
        sleep(2)
        driver.find_element_by_id("id_gold").clear()
        driver.find_element_by_id("id_gold").send_keys("+25")  # 对Real Money Balance输入框输入+25
        driver.implicitly_wait(10)
        Select(driver.find_element_by_id('modify_reason')).select_by_visible_text('Test')
        driver.find_element_by_id("remarks_gold").clear()
        driver.find_element_by_id("remarks_gold").send_keys("python automatied testing ")  # 备注输入框输入
        driver.find_element_by_id("confirmA").click()  # 点击确认
        driver.implicitly_wait(10)
        driver.find_element_by_id("confirm_save").click()  # 点击Yes确认
    else:   #用户余额为0.00时，直接加钱到25
        driver.find_element_by_xpath("/*//span[@id='gold']/../button").click()
        print(driver.find_element_by_xpath("/*//span[@id='gold']").text)
        sleep(2)
        driver.find_element_by_id("id_gold").clear()  # 清空输入框
        driver.find_element_by_id("id_gold").send_keys("+25")  # 对Real Money Balance输入框输入+25
        driver.implicitly_wait(10)
        Select(driver.find_element_by_id('modify_reason')).select_by_visible_text('Test')
        driver.find_element_by_id("remarks_gold").clear()  # 备注清空
        driver.find_element_by_id("remarks_gold").send_keys("python automatied testing ")  # 备注输入框输入
        driver.find_element_by_id("confirmA").click()           # 点击确认
        print("Yes确认")
        driver.implicitly_wait(10)
        driver.find_element_by_id("confirm_save").click()     # 点击Yes确认


if __name__ == '__main__':
    """初始要修改的玩家"""
    user_id11="20455"   #ming101@qq.com
    user_id22="20442"   #ming999@qq.com
    CRM_money_adjustment()