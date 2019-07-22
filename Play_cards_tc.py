# -*- encoding=utf8 -*-
__author__ = "Admin"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from poco.drivers.std import StdPoco
pocos=StdPoco()
# from untitled import *

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# script content
print("start...")



#============================================================================================
class MING_POKIO:
    @classmethod
    def _Game_table_check(cls):
        """平跟"""
        try:
            if pocos("btn_call").wait(1).exists():  #小盲位平跟
                pocos("btn_call").wait(2).click()
            else:
                pocos("btn_look").wait(1).click()
        except:
            print("平跟异常日志写入")

    def _Game_table_raise(slef):
        """加注"""
        try:
            pocos("btn_add").wait(19).click()
            pocos("point_bar_end").click()   #ALL IN  全推
            pocos("btn_sure").click()        #DONE   确认
        except:
            print("加注异常日志写入")

    def _Game_table_fold(slef):
        """弃牌"""
        poco("btn_fold").wait(19).click()


# ============================================================================================
    def _Game_table_sitdown():
        """桌内坐下来"""
        try:
            sleep(1)
            pocos("<Layer | Tag = -1>").child("<Layer | Tag = -1>")[1].child("Button")[0].click('center')
            pocos("panel_tip").child("btn_ok").click('center')
        except:
            print("桌内坐下来异常日志写入")

    def _Game_table_observe():
        """桌内站起"""
        try:
            sleep(5)
            pocos("lbl_daytime").click()
            pocos("bnt_menu").wait(15).click('center')
            lenns=len(pocos("<LayerColor | Tag = -1>").child("Button"))
            pocos("<LayerColor | Tag = -1>").child("Button")[0].click('center')
        except:
            print("桌内站起异常日志写入")

    def _Game_table_leave():
        """退出牌局"""
        try:
            sleep(5)
            pocos("bnt_menu").wait(15).click('center')
            lenns=len(pocos("<LayerColor | Tag = -1>").child("Button"))
            pocos("<LayerColor | Tag = -1>").child("Button")[lenns-1].click('center')
            pocos("dialog_bg_9scale").child("btn_ok").click()
        except:
            print("退出牌局异常日志写入")

    def _Game_table_tablesettings():
        """解散牌局"""
        try:
            sleep(5)
            pocos("bnt_menu").wait(15).click('center')
            lenns=len(pocos("<LayerColor | Tag = -1>").child("Button"))
            pocos("<LayerColor | Tag = -1>").child("Button")[0].click('center')
            pocos("btn_end").wait(3).click('center')
            pocos("dialog_bg_9scale").child("btn_ok").click()
        except:
            print("解散牌局异常日志写入")

    def Wallet_string_processing(walletstr):
        """钱包字符串转换数值类型处理方法"""
        if '€' in walletstr:
            walletstr = walletstr.strip('€')
            walletstr=walletstr.replace(',','')
            walletfloat=float(walletstr)
            number=round(walletfloat,2)
            return number



    def _Game_table_walletget(dfdfsdf):
        """桌内钱包金额获取"""
        if  pocos("panel_wallet_close").wait(5).exists():#如果钱包隐藏
            pocos("img_wallet_bg").click("center")  #显示钱包余额
        welletstr=pocos("<Layer | Tag = -1>").child("<Layer | Tag = -1>")[0].offspring("lbl_wallet").get_text()
        welletfloat = Wallet_string_processing(welletstr)     #str类型转换f
        print("welletfloat:",welletfloat)
        return welletfloat



    def _Game_table_chipget():
        """桌内当前用户筹码获取"""
        usernum=len(pocos("<Layer | Tag = -1>").child("<Layer | Tag = -1>")[1].child("default_user"))   #当前桌子人数
        chips=pocos("<Layer | Tag = -1>").child("<Layer | Tag = -1>")[1].child("default_user")[usernum-1].offspring("lbl_money").get_text()
        # print("usernum",usernum)
        chipfloat=Wallet_string_processing(chips)
        # print("chipfloat",chipfloat)
        return chipfloat

#验证流程操作
#=======================================================================
# walletago=  _Game_table_walletget()   #坐前余额获取
# #坐下来，
# walletlater=  _Game_table_walletget()  #坐下后余额获取

#============================================================
# 进桌

# 退出牌桌
# _Game_table_leave()  
# # 解散牌桌
# _Game_table_tablesettings()
# # 坐下来
# _Game_table_sitdown()
# # 站起来
# _Game_table_observe()
# # 平跟
# _Game_table_check()    
# # 加注
# _Game_table_raise()
# # 弃牌
# _Game_table_fold()
# 桌内钱包金额获取
# _Game_table_walletget()
# 桌内筹码获取
# _Game_table_chipget()

#=========算法调试========================
# wallet11=_Game_table_walletget()    #未坐下前获取钱包值
# if wallet11==48.65:
#     print("未坐下前获取钱包值")
# _Game_table_sitdown()               #操作坐下
#
# wallet22=_Game_table_walletget()    #坐下后再获取钱包值
# if wallet22==23.65:
#     print("坐下后再获取钱包值")
# chip11=_Game_table_chipget()        #获取坐下的筹码值
# if chip11==25:
#     print("获取坐下的筹码值")

