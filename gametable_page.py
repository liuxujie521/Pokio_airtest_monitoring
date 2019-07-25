# -*- encoding=utf8 -*-
__author__ = "zhouming"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from poco.drivers.std import StdPoco

class GameOperationMethod(object):
    """游戏内操作的所有方法"""
    def __init__(self,pocos):
        self.pocos = pocos

    def _Game_table_check(self):
        """平跟"""
        try:
            if self.pocos("btn_call").wait(1).exists():  #小盲位平跟
                self.pocos("btn_call").click()
            elif self.pocos("btn_allin").wait(1).exists():
                self.pocos("btn_allin").click()
            else:
                self.pocos("btn_look").wait(1).click()
        except:
            print("平跟异常日志写入")

    def _Game_table_raise(self):
        """加注"""
        try:
            self.pocos("btn_add").wait(1).click()
            self.pocos("point_bar_end").click()   #ALL IN  全推
            self.pocos("btn_sure").click()        #DONE   确认
        except:
            print("加注异常日志写入")

    def _Game_table_fold(self):
        """弃牌"""
        self.pocos("btn_fold").wait(1).click()


    # ============================================================================================
    def _Game_table_sitdown(self):
        """桌内坐下来"""
        try:
            sleep(1)
            self.pocos("<Layer | Tag = -1>").child("<Layer | Tag = -1>")[1].child("Button")[0].click('center')
            self.pocos("panel_tip").child("btn_ok").click('center') #点击

            if self.pocos("panel_expand").child("btn_find_bb").wait(2).exists():
                print("确认成功并成功弹出Wait for BB")
                self.pocos("lbl_daytime").wait(1).click()
            
            elif self.pocos("panel_warn").child("lbl_tip_warn").wait().exists():#余额不足判断
                print("余额不足，玩家无法坐下验证成功")
            else:
                print("坐下失败")
        except:
            print("桌内坐下来异常日志写入")

    def _Game_table_observe(self):
        """桌内站起"""
        try:
            sleep(5)
            self.pocos("lbl_daytime").click()
            self.pocos("bnt_menu").wait(15).click('center')
            lenns=len(self.pocos("<LayerColor | Tag = -1>").child("Button"))
            self.pocos("<LayerColor | Tag = -1>").child("Button")[0].click('center')
        except:
            print("桌内站起异常日志写入")

    def _Game_table_leave(self):
        """退出牌局"""
        try:
            sleep(5)
            self.pocos("bnt_menu").wait(15).click('center')
            lenns=len(self.pocos("<LayerColor | Tag = -1>").child("Button"))
            self.pocos("<LayerColor | Tag = -1>").child("Button")[lenns-1].click('center')
            self.pocos("dialog_bg_9scale").child("btn_ok").click()
        except:
            print("退出牌局异常日志写入")

    def _Game_table_tablesettings(self):
        """解散牌局"""
        try:
            sleep(5)
            self.pocos("bnt_menu").wait(15).click('center')
            lenns=len(self.pocos("<LayerColor | Tag = -1>").child("Button"))
            self.pocos("<LayerColor | Tag = -1>").child("Button")[0].click('center')
            self.pocos("btn_end").wait(3).click('center')
            self.pocos("dialog_bg_9scale").child("btn_ok").click()
        except:
            print("解散牌局异常日志写入")

    def Wallet_string_processing(self,walletstr):
        """钱包字符串转换数值类型处理方法"""
        if '€' in walletstr:
            walletstr = walletstr.strip('€')
            walletstr=walletstr.replace(',','')
            walletfloat=float(walletstr)
            number=round(walletfloat,2)
            return number


    def _Game_table_walletget(self):
        """桌内钱包金额获取"""
        if  self.pocos("panel_wallet_close").wait(5).exists():#如果钱包隐藏
            self.pocos("img_wallet_bg").click("center")  #显示钱包余额
        welletstr=self.pocos("<Layer | Tag = -1>").child("<Layer | Tag = -1>")[0].offspring("lbl_wallet").get_text()
        welletfloat = self.Wallet_string_processing(welletstr)     #str类型转换f
        print("welletfloat:",welletfloat)
        return welletfloat


    def _Game_table_chipget(self):
        """桌内当前用户筹码获取"""
        usernum=len(self.pocos("<Layer | Tag = -1>").child("<Layer | Tag = -1>")[1].child("default_user"))   #当前桌子人数
        chips=self.pocos("<Layer | Tag = -1>").child("<Layer | Tag = -1>")[1].child("default_user")[usernum-1].offspring("lbl_money").get_text()
        # print("usernum",usernum)
        chipfloat=self.Wallet_string_processing(chips)
        # print("chipfloat",chipfloat)
        return chipfloat
    

    def Close_Windows_processing(self):
        """保险与多次牌处理"""
        if self.pocos("panel_content").wait(2).exists(): #保险与多次牌处理
            print("选择性弹窗关闭")
            self.pocos("btn_close").wait(0.5).click()       #叉处理按钮
        else:
            print("多次牌弹窗关闭")
            self.pocos("btn_close").wait(0.5).click()

            
            
            
#         poco("panel_content") #保险与多次牌处理
#         poco("btn_close")       #叉处理按钮
#         poco("buyinsurance")    #Insurance保险按钮
#         poco("faduocipai")      #Run Mor Times多次牌按钮

# # if 出现弹窗（或关系统）


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

