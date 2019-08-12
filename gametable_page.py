# -*- encoding=utf8 -*-
__author__ = "zhouming"

from Requests_pokio import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco   #调用实例化
from poco.drivers.std import StdPoco    #调用实例化

import time

class GameOperationMethod(object):
    """游戏内操作的所有方法"""
    def __init__(self,pocos,poco):
        self.pocos = pocos
        self.poco = poco
        self.webhook="https://oapi.dingtalk.com/robot/send?access_token=74d0a1bdec607b9f7e302f3d8654c5e88bca602c31e72584da9e918ba40a2e7b"
        self.zm='18818778156'
    def _Entrance_table(self, tablesna):
        """指定入桌"""
        try:
            for i in range(3):
                if self.poco("com.qfun.pokio:id/main_footbar_lobbydbtn").wait(2).exists():## 判断是否Play页面
                    print("首页面找到Play元素")
                    break  # 找到了就跳出循环
                else:
                    keyevent("BACK")  # 使页面回来首页
            self.poco("com.qfun.pokio:id/main_footbar_lobbydbtn").wait(2).click()  # Play页面
            self.poco(text="Ring").wait(2).click()  # 确认是在Ring现金桌操作
            sleep(0.2)
            self.poco(text=tablesna).click()  # 点击指定的牌桌
            print("指定入桌验证成功")
        except:
            print("入桌异常日志记录")
            dingding_Disaster(self.webhook, "入桌异常告警", user=self.zm, Atall=False)

    def _Game_table_check(self):
        """平跟"""
        try:
            if self.pocos("btn_call").wait(1).exists():  #小盲位平跟
                self.pocos("btn_call").click()
                print("平跟")
            elif self.pocos("btn_allin").wait(1).exists():
                self.pocos("btn_allin").click()
                print("全推平跟")
            else:
                self.pocos("btn_look").wait(1).click()
                print("btnlook")
        except:
            print("平跟异常日志记录")
            dingding_Disaster(self.webhook, "平跟异常告警", user=self.zm, Atall=False)

    def _Game_table_raise(self):
        """加注"""
        try:
            self.pocos("btn_add").wait(1).click()
            self.pocos("point_bar_end").click()   #ALL IN  全推
            self.pocos("btn_sure").click()        #DONE   确认
            print("加注全推")
        except:
            print("加注异常日志记录")
            dingding_Disaster(self.webhook, "加注异常告警", user=self.zm, Atall=False)

    def _Game_table_fold(self):
        """弃牌"""
        self.pocos("btn_fold").wait(1).click()

    # ============================================================================================
    def _Game_table_sitdown(self):
        """桌内坐下来"""
        try:
            sleep(1)
            self.pocos("<Layer | Tag = -1>").child("<Layer | Tag = -1>")[1].child("Button")[0].click('center')  #选择座位
            self.pocos("panel_tip").child("btn_ok").click('center') #点击坐下

            if self.pocos("panel_expand_touch").wait(1).exists():   #For BB元素一直存在，判断是不是展开，通过遮罩元素来判断               
                print("确认成功并成功弹出Wait for BB")
                self.pocos("lbl_daytime").wait(1).click()

            elif self.pocos("panel_warn").child("lbl_tip_warn").wait().exists():#余额不足判断
                print("余额不足，玩家无法坐下验证成功")
                return True
            else:
                print("坐下失败")
                dingding_Disaster(self.webhook, "桌内坐下失败告警", user=self.zm, Atall=False)
                return True
        except:
            print("桌内坐下来异常日志记录")
            dingding_Disaster(self.webhook, "桌内坐下异常告警", user=self.zm, Atall=False)
            return True
    def _Game_table_observe(self):
        """桌内站起"""
        try:
            sleep(2)
            self.pocos("lbl_daytime").wait(2).click()
            self.pocos("bnt_menu").wait(15).click('center')
            lenns=len(self.pocos("<LayerColor | Tag = -1>").child("Button"))
            self.pocos("<LayerColor | Tag = -1>").child("Button")[0].click('center')
            if self.pocos("dialog_bg_9scale").wait(3).exists():
                print("Tips弹窗")
                self.pocos("btn_ok").wait(2).click()  # Yes
        except:
            print("桌内站起异常日志记录")
            dingding_Disaster(self.webhook, "桌内站起异常告警", user=self.zm, Atall=False)

    def _Game_table_leave(self):
        """退出牌局"""
        try:
            sleep(5)
            self.pocos("bnt_menu").wait(15).click('center')
            lenns=len(self.pocos("<LayerColor | Tag = -1>").child("Button"))
            self.pocos("<LayerColor | Tag = -1>").child("Button")[lenns-1].click('center')
        except:
            print("退出牌局异常日志记录")
            dingding_Disaster(self.webhook, "退出牌局异常告警", user=self.zm, Atall=False)

    def _Game_table_tablesettings(self):
        """解散牌局"""
        try:
            sleep(5)
            self.pocos("bnt_menu").wait(15).click('center')
            lenns=len(self.pocos("<LayerColor | Tag = -1>").child("Button"))
            self.pocos("<LayerColor | Tag = -1>").child("Button")[0].click('center')
            self.pocos("btn_end").wait(3).click('center')
            self.pocos("dialog_bg_9scale").child("btn_ok").click()
            print("解散现金牌桌成功")
        except:
            print("解散现金牌桌异常日志记录")
            dingding_Disaster(self.webhook, "解散现金牌桌异常告警", user=self.zm, Atall=False)

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
        try:
            sleep(0.5)
            if  self.pocos("panel_wallet_close").wait(5).exists():#如果钱包隐藏
                self.pocos("img_wallet_bg").click("center")  #显示钱包余额
            welletstr=self.pocos("<Layer | Tag = -1>").child("<Layer | Tag = -1>")[0].offspring("lbl_wallet").get_text()
            welletfloat = self.Wallet_string_processing(welletstr)     #str类型转换f
            print("welletfloat:",welletfloat)
            return welletfloat
        except:
            print("桌内钱包金额获取异常")
            return

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

    def _Tablesend_achievement_dataget(self):
        """结算Achievement页面数据获取"""
        print("Achievement页面数据")
        sleep(2)
        date = self.poco("com.qfun.pokio:id/tv_game_date").get_text()  # 日期
        tablename = self.poco("com.qfun.pokio:id/tv_game_name").get_text()  # 牌桌名
        stakes = self.poco("com.qfun.pokio:id/tv_game_binds").get_text()  # 大小盲
        handsplayed = self.poco("com.qfun.pokio:id/tv_game_total_hands").get_text()  # 多少手牌
        biggestpot = self.poco("com.qfun.pokio:id/tv_game_big_pot").get_text()  # 最大奖池

        username_01 = self.poco("android:id/list").child("android.widget.RelativeLayout")[0].child(
            "com.qfun.pokio:id/tv_user_name").get_text()  # 玩家1名称
        profit_01 = self.poco("android:id/list").child("android.widget.RelativeLayout")[0].child(
            "com.qfun.pokio:id/tv_profit").get_text()  # 玩家1输赢金额
        username_02 = self.poco("android:id/list").child("android.widget.RelativeLayout")[1].child(
            "com.qfun.pokio:id/tv_user_name").get_text()  # 玩家2名称
        profit_02 = self.poco("android:id/list").child("android.widget.RelativeLayout")[1].child(
            "com.qfun.pokio:id/tv_profit").get_text()  # 玩家2输赢金额
        print("日期：",date,type(date))
        print("==============================================")
        print("桌名：",tablename,type(tablename))
        print("==============================================")
        print("盲注：",stakes,type(stakes))
        print("==============================================")
        print("牌次：",handsplayed,type(handsplayed))
        print("==============================================")
        print("奖池：",biggestpot,type(biggestpot))
        print("==============================================")
        print("username_01:::",username_01)
        print("profit_01:::",profit_01)
        print("username_01:::",username_02)
        print("profit_02:::",profit_02)
        #
        return date, tablename, biggestpot, username_01, profit_01, username_02, profit_02

    def _Wallet_Netrevenue_dataget(self,clubna):
        """
        钱包俱乐部净收益最新数据获取
        :param clubna: 俱乐部名称
        :return:返回收益的时间（time_m）、净收入（revenue）
        """
        if self.poco("com.qfun.pokio:id/main_footbar_cashierbtn").wait(2).exists(): #没有在首页，进行返回操作处理
            print("已经切换到首页")
        else:
            keyevent("BACK")

        self.poco("com.qfun.pokio:id/main_footbar_cashierbtn").click()  # 钱包模块
        self.poco(text=clubna).wait(2).click()
        sleep(1)
        poco_item = self.poco("com.qfun.pokio:id/lv_club_latest").child("com.qfun.pokio:id/rl_record_item")[0]  # 第一个净收入
        time_s = poco_item.child("com.qfun.pokio:id/tv_record_time").wait(2).get_text()  # 获取收入的时间（核对的条件）
        revenue = poco_item.offspring("com.qfun.pokio:id/tv_club_revenue").wait(1).get_text()  # 获取俱乐部收入（抽水的核对）
        print("获取收入的最新时间time_s",time_s)
        time_ms = time.strptime(time_s,'%d/%m/%Y %H:%M:%S') #分解成元组
        print("time_ms:",time_ms)
        time_m = time.strftime('%d/%m/%Y %H:%M',time_ms)  #去掉秒精度
        print("收益time：：",time_m)
        print("收益Rake::", revenue)
        keyevent("BACK")    #返回到主页
        return time_m, revenue  # r返回时间与净收入

#验证流程操作
#=======================================================================
# walletago=  _Game_table_walletget()   #坐前余额获取
# #坐下来，
# walletlater=  _Game_table_walletget()  #坐下后余额获取

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

