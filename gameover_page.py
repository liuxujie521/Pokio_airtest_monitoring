# -*- encoding=utf8 -*-
__author__ = "zhouming"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def _Tablesend_achievement_dataget():
    """结算Achievement页面数据获取"""
    pass
    date = poco("com.qfun.pokio:id/tv_game_date").get_text()                #日期
    tablename = poco("com.qfun.pokio:id/tv_game_name").get_text()           #牌桌名
    stakes = poco("com.qfun.pokio:id/tv_game_binds").get_text()             #大小盲
    handsplayed = poco("com.qfun.pokio:id/tv_game_total_hands").get_text()  #多少手牌
    biggestpot = poco("com.qfun.pokio:id/tv_game_big_pot").get_text()       #最大奖池
    
    print(type(date))
    print(date)    
    print("==============================================")
    print(type(tablename))
    print(tablename)
    print("==============================================")
    print(type(stakes))
    print(stakes)
    print("==============================================")
    print(type(handsplayed))
    print(handsplayed)    
    print("==============================================")
    print(type(biggestpot))
    print(biggestpot)    
    print("==============================================")
    
    username_01 = poco("android:id/list").child("android.widget.RelativeLayout")[0].child("com.qfun.pokio:id/tv_user_name").get_text()   #玩家1名称
    profit_01 = poco("android:id/list").child("android.widget.RelativeLayout")[0].child("com.qfun.pokio:id/tv_profit").get_text()      #玩家1输赢金额
       
    username_02 = poco("android:id/list").child("android.widget.RelativeLayout")[1].child("com.qfun.pokio:id/tv_user_name").get_text()   #玩家2名称
    profit_02 = poco("android:id/list").child("android.widget.RelativeLayout")[1].child("com.qfun.pokio:id/tv_profit").get_text()      #玩家2输赢金额
    
    print("username_01",username_01)
    print("profit_01",profit_01)
    print("username_01",username_02)
    print("profit_02",profit_02)    
    
    return date,tablename,biggestpot,username_01,profit_01,username_02,profit_02

    
    
def _Wallet_Netrevenue_dataget(clubna):
    """钱包俱乐部净收益最新数据获取"""
    pass
    poco("com.qfun.pokio:id/main_footbar_cashierbtn").click()   #钱包模块
    poco(text=clubna).wait(2).click()
    sleep(1)
    
    poco_item=poco("com.qfun.pokio:id/lv_club_latest").child("com.qfun.pokio:id/rl_record_item")[0]#第一个净收入
    time_t=poco_item.child("com.qfun.pokio:id/tv_record_time").get_text()
    print(time_t)
    ttt=poco_item.offspring("com.qfun.pokio:id/tv_club_revenue").get_text()
    print("ttt:",ttt)


# clubna="EEE"
# _Wallet_Netrevenue_dataget(clubna)    #最新净收入

# _Tablesend_achievement_dataget()  #结算页面数据

date,tablename,biggestpot,username_01,profit_01,username_02,profit_02 =_Tablesend_achievement_dataget()
print("返回结算数据")
print(date,tablename,biggestpot,username_01,profit_01,username_02,profit_02)
keyevent("BACK")
