# -*- encoding=utf8 -*-
__author__ = "zhouming"

import traceback
from Requests_pokio import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from decorator import *
from poco.drivers.std import StdPoco
import time
#全局初始化
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
dev1 = connect_device("Android://127.0.0.1:5037/3SC5T16B29008638")  # 华为P9
pocos = StdPoco(15004, dev1)
# dev1 = connect_device("Android://127.0.0.1:5037/3SC5T16B29008638")  # 华为P9
# dev1 = connect_device("Android://127.0.0.1:5037/ORYTDMMB5PJRDE7D")  # OPPO  R15
webhook = "https://oapi.dingtalk.com/robot/send?access_token=74d0a1bdec607b9f7e302f3d8654c5e88bca602c31e72584da9e918ba40a2e7b"
zm = '18818778156'
holdem = "Hold'em"
omaha = "Omaha"
drawma = "Drawmaha"
ofc = "OFC"
plo5 = "PLO5"
ring = "Ring"
sng = "SNG"
mtt = "MTT"


class TableOperationMethod(object):
    """桌子操作所有方法封装"""
    # dev1 = connect_device("Android://127.0.0.1:5037/3SC5T16B29008638")  # 华为P9
    # webhook = "https://oapi.dingtalk.com/robot/send?access_token=74d0a1bdec607b9f7e302f3d8654c5e88bca602c31e72584da9e918ba40a2e7b"
    # zm = '18818778156'
    # holdem = "Hold'em"
    # omaha = "Omaha"
    # drawma = "Drawmaha"
    # ofc = "OFC"
    # plo5 = "PLO5"
    # ring = "Ring"
    # sng = "SNG"
    # mtt = "MTT"
    # def __init__(self):
    #     self.dev1 = connect_device("Android://127.0.0.1:5037/3SC5T16B29008638")  #华为P9
    #     self.webhook="https://oapi.dingtalk.com/robot/send?access_token=74d0a1bdec607b9f7e302f3d8654c5e88bca602c31e72584da9e918ba40a2e7b"
    #     self.zm='18818778156'
    #     self.holdem = "Hold'em"
    #     self.omaha = "Omaha"
    #     self.drawma = "Drawmaha"
    #     self.ofc = "OFC"
    #     self.plo5 = "PLO5"
    #     self.ring = "Ring"
    #     self.sng = "SNG"
    #     self.mtt = "MTT"

    def _Clubs_Tables_process(self,clubn):
        """
        进入俱乐部的桌子创建
        :param clubn: 指定的俱乐部名
        :return:
        """
        if poco("com.qfun.pokio:id/main_footbar_clubsdbtn").wait(1).exists():
            poco("com.qfun.pokio:id/main_footbar_clubsdbtn").wait(1).click('center')  # 确认在Club页面
        else:
            keyevent("BACK")
        poco(text=clubn).wait(1).click()  # 注意：不能出现同名的俱乐部,
        sleep(1)  # 加载时间等待
        poco("com.qfun.pokio:id/rb_tab_table").click('center')  # Table


    def Create_Table_settings(self,tables):
        """创桌的相关子设置"""
        # 牌局设置（滑动设置）一般不设置，选择默认值
        if tables == "OFC":  # 只有OFC的创桌所填的信息不一样
            poco(text="Stakes (€)").swipe([0.0, -0.35])  # 滑动动使元素可见
            point_a = [0.0, 0.0]
            center = [0.5, 0.0]
            poco("com.qfun.pokio:id/rb_player_3").click()# Table size
            poco("com.qfun.pokio:id/rb_player_2").click()
            poco("com.qfun.pokio:id/bar_blinds").swipe(point_a, center)# Stakes (€)
            poco("com.qfun.pokio:id/bar_min_buy_in").swipe(point_a, center)# #Minimum buy-in (€)
            poco("com.qfun.pokio:id/bar_max_buy_in").swipe(point_a, center)# #Maximum buy-in (€)
            poco(text="Maximum buy-in (€)").swipe([0.0, -0.5])
            poco("com.qfun.pokio:id/rb_time_bank_20s").click()# Time bank
            # 同时发牌
            # poco("com.qfun.pokio:id/rb_dealing_concurrent")
            poco("com.qfun.pokio:id/rb_dealing_sequence").click()   # 按顺序发
            poco("com.qfun.pokio:id/sb_std_gps_ip").click()      # GPS/IP restrictions
            poco("com.qfun.pokio:id/sb_stats_hide_players").click()# # Hide players stats
            poco("com.qfun.pokio:id/sb_stats_hide_table").click()# # Hide table stats
        else:
            poco(text="Stakes (€)").swipe([0.0, -0.45])  # 滑动动使元素可见
            point_a = [0.0, 0.0]
            center = [0.4, 0.0]
            poco("com.qfun.pokio:id/bar_blinds").wait(2).swipe(point_a, center)       # Stakes (€)
            poco("com.qfun.pokio:id/bar_min_buy_in").wait(2).swipe(point_a, center)   # Minimum buy-in (€)
            poco("com.qfun.pokio:id/bar_max_buy_in").wait(2).swipe(point_a, center)   # Maximum buy-in (€)
            poco("com.qfun.pokio:id/bar_ante").wait(2).swipe(point_a, center)     # Ante (€)
            poco("com.qfun.pokio:id/bar_player").wait(2).swipe(point_a, center)   # Table size

            poco(text="Table size").swipe([0.0, -0.48])  # 滑动动使元素可见
            #牌局设置（开关设置）
            poco("com.qfun.pokio:id/sb_std_straddle").click() # Auto-straddle
            poco("com.qfun.pokio:id/sb_std_muck").click()     # Auto-muck
            poco("com.qfun.pokio:id/sb_std_gps_ip").click()   # GPS/IP restrictions
            poco("com.qfun.pokio:id/sb_stats_hide_players").click()   # Hide players stats
            poco("com.qfun.pokio:id/sb_stats_hide_table").click()     # Hide table stats


    # 各种玩法牌桌创建
    # =========================================================================================
    def Create_Ring_table_process(self,tables):
        """
        现金牌桌创建的流程
        :param tables: 所创的桌子名称
        :return:
        """
        try:
            poco.wait_stable()  # 等待元素加载稳定
            poco("com.qfun.pokio:id/tv_create_game").wait(2).click()  # Create table按钮
            sleep(0.2)
            # 牌局设置（滑动设置）
            # =========================================================================================
            if tables == "Hold'em":
                print("Hold'em")
                poco("com.qfun.pokio:id/rb_play_type_hold").wait(5).click()  #
            elif tables == "Omaha":
                print("Omaha")
                poco("com.qfun.pokio:id/rb_play_type_omaha").wait(5).click()
            elif tables == "Drawmaha":
                print("Drawmaha")
                poco("com.qfun.pokio:id/rb_play_type_draw").wait(5).click()
            elif tables == "PLO5":
                print("PLO5")
                poco("com.qfun.pokio:id/rb_play_type_plo5").wait(5).click()
            elif tables == "OFC":
                print("OFC")
                poco("com.qfun.pokio:id/rb_play_type_ofc").wait(5).click()
            else:
                print("没有该玩法，请重新选择！！！")

            poco("com.qfun.pokio:id/et_table_name").wait(5).set_text(tables)  # 填写所创建的桌子名称
            # sleep(0.2)
            poco("com.qfun.pokio:id/tv_create").wait(5).click()  # Create创建
            print("已经点击Create创建")
            sleep(2)
            if pocos("<Layer | Tag = -1>").wait(10).exists():#首先确认游戏内框架是否加载成功
                print("确认Create创建已跳转")
                pass
            else:
                print("中断")
                return  #中断
            if pocos("btn_begingame").wait(15).exists():#创建完后的桌子是有一个Start按钮的
                print("创建完成，准备退出该桌子")
                self._Game_table_leave(tables) #创桌正确才可退出牌局
            else:   #如果没有进桌或找不到该元素，创桌失败
                tablestr=tables+"现金桌子创建失败异常告警"
                print(tablestr)
                dingding_Disaster(webhook, tablestr, user=zm, Atall=False)
        except:
            tablestr = tables + "现金桌子创建失败异常告警"
            print(tablestr)
            dingding_Disaster(webhook, tablestr, user=zm, Atall=False)
            traceback.print_exc()  # 只记录报错，不跳出

    def Create_Tournament_table_process(self,tables, formats):
        """
        赛事牌桌创建的流程
        :param tables: 所创的玩法类型，目前只Hold'em
        :param formats: 赛事玩法名字（SNG、MTT）
        :return:
        """
        try:
            sleep(2)
            print("Hold'em", formats)   #显示下当前要操作的赛事
            poco("com.qfun.pokio:id/tv_create_game").wait(15).click()  # Create table按钮
            poco.wait_stable()  #
            poco("com.qfun.pokio:id/rb_play_type_hold").wait(5).click() #
            if formats == "SNG":
                poco("com.qfun.pokio:id/rb_game_type_sng").click()
                poco("com.qfun.pokio:id/et_table_name").wait(2).set_text(tables + formats)  # 填写所创建的赛事桌子名称
                poco("com.qfun.pokio:id/et_game_desc").set_text(
                    "This Hold'em-SNG event is for automated testing only,please do not Register")  # 50描述限制
                # 其他设置省得
                poco("com.qfun.pokio:id/tv_create").wait(5).click()  # Create创建

            elif formats == "MTT":
                poco("com.qfun.pokio:id/rb_game_type_mtt").click()
                poco("com.qfun.pokio:id/et_table_name").wait(2).set_text(tables + formats)  # 填写所创建的赛事桌子名称
                poco("com.qfun.pokio:id/et_game_desc").set_text(
                    "This Hold'em-MTT event is for automated testing only,please do not Register")  # 50描述限制
                poco(text="Description").swipe([0.0, -0.50])  # 滑动动使元素可见
                sleep(1)
                if poco("com.qfun.pokio:id/tv_mtt_start_time").wait(2).exists():  # 时间修改元素未显示就继续滑动
                    pass
                else:
                    print("没找到该时间元素再滑动一次1")
                    poco(text="Start stacks (BB)").swipe([0.0, -0.50])  # 滑动动使元素可见
                if poco("com.qfun.pokio:id/tv_mtt_start_time").wait(2).exists():
                    pass
                else:
                    print("没找到该时间元素再滑动一次2")
                    poco(text="Rebuy(times)").swipe([0.0, -0.40])
                poco("com.qfun.pokio:id/tv_mtt_start_time").wait(2).click('center')  # 点击时间设置
                poco("com.qfun.pokio:id/month").wait(3).swipe([0.0, -0.06])  # 滑动月份就行
                poco("com.qfun.pokio:id/tv_sure").click()  # Done确认时间
                poco("com.qfun.pokio:id/tv_create").click()  # Create创建
                poco.wait_stable()
            elif formats == "Ring":
                print("该方法无法创建现金桌")
            else:
                print("请填写正常赛事名称")
                dingding_Disaster(webhook, "请填写正常赛事名称", user=zm, Atall=False)
        except:
            tournament = "Hold'em"+formats+"赛事创建失败异常告警"
            print(tournament)
            self.Create_Tournament_table_process(tables, formats)
            dingding_Disaster(webhook,tournament, user=zm, Atall=False)
            traceback.print_exc()  # 只记录报错，不跳出
        else:
            print(formats,"赛事创建成功")

    def Register_Tournament_table(self,tourname):
        """
        根据提供的赛事名称进行报名
        :param tourname: 创建的赛事名称
        :return:
        """
        try:
            poco(text="Tournament").wait(10).click()  # 点击Tournament查看赛事桌子
            poco(text=tourname).wait(5).click()  # 点击赛事进行详情页
            if poco("com.qfun.pokio:id/tv_title_center").wait(2).get_text() == tourname:  # 标题栏赛事名字
                if poco(text="Structure").wait(1).exists():  # SNG赛事独有的元素
                    print("SNG")
                    self.tourtype = "SNG"    #赛事的类型（SNG）
                else:
                    print("MTT")
                    self.tourtype = "MTT"
                if poco("com.qfun.pokio:id/tv_apply").get_text() == "Register":  # 赛事报名
                    poco("com.qfun.pokio:id/layout_opera").click()  # 报名Register报名
                    poco("com.qfun.pokio:id/tv_confirm").click()  # 确认报名弹窗Yes
                    sleep(0.2)
                    if poco(text="Deposit").wait(2).exists():  # 余额不足提示充值
                        poco("com.qfun.pokio:id/tv_cancel").wait(2).click()
                        print("余额不足，取消报名")
                    elif self.tourtype == "MTT":  # MTT赛事类型有一个时间提示的弹窗
                        poco(text="Got it").click()  # 注销成功
                if poco("com.qfun.pokio:id/tv_apply").get_text() != "Register":  # 状态发生变化判断验证成功
                    print(tourname,"赛事报名成功")
        except:
            register=tourname + "赛事报名失败异常告警"
            print(register)
            dingding_Disaster(webhook, register, user=zm, Atall=False)
            traceback.print_exc()  # 只记录报错，不跳出

    def Unregister_Tournament_table(self,tourname):
        """取消报名"""
        # 取消赛事报名
        poco.wait_stable()  # 等待元素加载稳定
        try:
            if poco("com.qfun.pokio:id/tv_apply").get_text() == "Unregister":  # 取消报名
                poco("com.qfun.pokio:id/layout_opera").click()  # 取消报名
                poco("com.qfun.pokio:id/tv_confirm").click()  # 确认报名弹窗Yes
                poco(text="Got it").wait(1).click()  # 注销成功
                sleep(0.2)
                if poco("com.qfun.pokio:id/tv_apply").get_text() != "Unregister":  # 验证状态是否变更来判断是否取消
                    print(tourname,"取消报名验证成功")
            elif poco("com.qfun.pokio:id/tv_apply").get_text() == "MTT is preparing":
                print("MTT开赛倒计时两分钟，无法取消报名")
            elif poco("com.qfun.pokio:id/tv_apply").get_text() == "Join the tournament":
                print("MTT进入赛事桌子准备，无法取消报名")
            elif poco("com.qfun.pokio:id/tv_apply").get_text() == "Register":
                print("MTT赛事还未报名成功，无法取消报名")
        except:
            unregister = tourname + "赛事取消报名失败异常告警"
            print(unregister)
            dingding_Disaster(webhook, unregister, user=zm, Atall=False)
            traceback.print_exc()  # 只记录报错，不跳出

    def Cancel_Tournament_table(self,tourname):
        """解散赛事牌桌"""
        # 解散赛事比赛
        poco.wait_stable()  # 等待元素加载稳定
        try:
            sleep(1)
            poco("com.qfun.pokio:id/fl_title_right").click()  # Cancel赛事
            poco("com.qfun.pokio:id/tv_confirm").wait(5).click()  # Yes确认取消赛事
            if poco(text="OK").wait(15).exists():  # 提示解散成功弹窗
                print(tourname,"赛事解散提示OK确认弹窗")
                poco(text="OK").wait(2).click()
                poco.wait_stable()  # 等待元素加载稳定
                # if #验证下赛事桌子是否还在
                poco(text="Tournament").wait(2).click()  # 点击Tournament查看赛事桌子
                if poco(text=tourname).wait(1).exists(): # 点击赛事进行详情页
                    print("解散失败请查看原因")
                else:
                    print(tourname,"赛事解散验证成功")
            elif poco("com.qfun.pokio:id/layout_opera").exists():  # 解散
                print("赛事取消失败了。请稍后再试")
                # 异常抛出
                keyevent("BACK")  # 返回不要影响其他流程
            else:
                print("其他隐性错误请查看")
        except:
            cancel=tourname + "赛事牌桌解散异常告警"
            print(cancel)
            dingding_Disaster(webhook, cancel, user=zm, Atall=False)

    def _Game_table_leave(self,tables):
        """退出牌局"""
        pocos.wait_stable()  # 等待元素加载稳定
        try:
            sleep(3)
            pocos("bnt_menu").wait(15).click('center')
            lenns=len(pocos("<LayerColor | Tag = -1>").child("Button"))
            pocos("<LayerColor | Tag = -1>").child("Button")[lenns-1].click('center')
            print("退出成功")
        except:
            leave = tables + "牌局退出异常告警"
            print(leave)
            dingding_Disaster(webhook, leave, user=zm, Atall=False)
            traceback.print_exc()  # 只记录报错，不跳出

    def _Terminate_table_tablesettings(self,table):
        """
        结束指定的现金桌子
        :param table: 现金桌名字
        :return:
        """
        poco.wait_stable()  # 等待元素加载稳定
        try:
            poco(text="Ring").wait(2).click()  # 点击Ring查看赛事桌子
            if poco(text=table).wait(1).exists():
                poco(text=table).wait(1).click()
            else:   #桌子太多，需要滑动来找
                swipe([0.0, -0.30])
                poco(text=table).wait(1).click()
            sleep(2)
            pocos("bnt_menu").wait(15).click('center')
            # lenns=len(pocos("<LayerColor | Tag = -1>").child("Button"))
            pocos("<LayerColor | Tag = -1>").child("Button")[0].click('center')
            pocos("btn_end").wait(3).click('center')
            pocos("dialog_bg_9scale").child("btn_ok").click()
            print(table,"现金牌桌解散成功")
        except:
            terminate = table + "现金牌桌解散失败异常告警"
            print(terminate)
            dingding_Disaster(webhook,terminate, user=zm, Atall=False)
            traceback.print_exc()  # 只记录报错，不跳出

    def All_Create_Ring_table(self):
        """创建所有类型的现金桌"""
        self.Create_Ring_table_process(holdem)  # # ===创建Hold'em玩法牌桌=================
        self.Create_Ring_table_process(omaha)   # # ===创建Omaha玩法牌桌===================
        self.Create_Ring_table_process(drawma)  # # ===创建Drawmaha玩法牌桌================
        self.Create_Ring_table_process(plo5)    # # ===创建PLO5玩法牌桌====================
        self.Create_Ring_table_process(ofc)     # # ===创建OFC玩法牌桌=====================

    def All_Terminate_Ring_table(self):
        """结束所选的桌子"""
        # self._Terminate_table_tablesettings(holdem)
        self._Terminate_table_tablesettings(omaha)
        self._Terminate_table_tablesettings(drawma)
        self._Terminate_table_tablesettings(plo5)
        self._Terminate_table_tablesettings(ofc)
    # 解散以上桌子，留下Holdem桌子供打牌

    def All_Create_Tournament_table(self):
        """创建所有玩法的赛事桌"""
        self.Create_Tournament_table_process(holdem, sng)  # # ===创建Hold'em玩法SNG牌桌=============
        print("继续创建赛事")
        keyevent("BACK")
        print("返回tables创建页面")
        self.Create_Tournament_table_process(holdem, mtt)  # # ===创建Hold'em玩法MMT牌桌=============
        keyevent("BACK")

    def All_Register_Unregister_Cancel(self,tourname):
        """报名、取消报名、结束赛事"""
        self.Register_Tournament_table(tourname)  # 报名
        self.Unregister_Tournament_table(tourname)  # 取消
        self.Cancel_Tournament_table(tourname)  # 结束赛事桌子

    # 解散以上桌子，留下Holdem桌子供打牌

    def main_createtable(self):
        """"""
        print("开始")
        self._Clubs_Tables_process("EEE")  # 选择操作的俱乐部
        self.All_Create_Ring_table()  # 创建所有的现金桌
        self.All_Terminate_Ring_table()  # 结束多个指定的现金桌子
        self.All_Create_Tournament_table()  # 创建所有的赛事
        self.All_Register_Unregister_Cancel(holdem + sng)  # 操作名字为Hold'emSNG赛事-报名、取消报名、结束赛事
        self.All_Register_Unregister_Cancel(holdem + mtt)  # 操作名字为Hold'emMTT赛事-报名、取消报名、结束赛事

# if __name__ == '__main__':
#     po=TableOperationMethod()
#     for i in range(10):
#         print("第%d次开始执行"%i)
#         po.main_createtable()
#         print("第%d次结束了"%i)
#         sleep(3)

# if __name__ == '__main__':
#     holdem = "Hold'em"
#     omaha = "Omaha"
#     drawma = "Drawmaha"
#     ofc = "OFC"
#     plo5 = "PLO5"
#     ring = "Ring"
#     sng = "SNG"
#     mtt = "MTT"
#     print("开始")
#     _Clubs_Tables_process("EEE")  # 选择操作的俱乐部
#     All_Create_Ring_table()  # 创建所有的现金桌
#     All_Terminate_Ring_table()  # 结束多个指定的现金桌子
#     All_Create_Tournament_table()  # 创建所有的赛事
#     All_Register_Unregister_Cancel(holdem + sng)#操作名字为Hold'emSNG赛事-报名、取消报名、结束赛事
# #     All_Register_Unregister_Cancel(holdem + mtt)#操作名字为Hold'emMTT赛事-报名、取消报名、结束赛事