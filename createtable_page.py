# -*- encoding=utf8 -*-
__author__ = "zhouming"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from poco.drivers.std import StdPoco
pocos = StdPoco()


def _Clubs_Tables_process(clubn):
    """进入俱乐部的桌子创建"""
    poco("com.qfun.pokio:id/main_footbar_clubsdbtn").wait(1).click('center')  # 确认在Club页面
    poco(text=clubn).wait(1).click()  # 注意：不能出现同名的俱乐部,
    sleep(1)  # 加载时间等待
    poco("com.qfun.pokio:id/rb_tab_table").click('center')  # Table


def Create_Table_settings(tables):
    """创桌的相关子设置"""
    # 牌局设置（滑动设置）
    # =========================================================================================
    if tables == "OFC":  # 只有OFC的创桌所填的信息不一样
        poco(text="Stakes (€)").swipe([0.0, -0.35])  # 滑动动使元素可见
    #         point_a = [0.0, 0.0]
    #         center = [0.5, 0.0]
    #         # Table size
    #         poco("com.qfun.pokio:id/rb_player_3").click()
    #         poco("com.qfun.pokio:id/rb_player_2").click()
    #         # Stakes (€)
    #         poco("com.qfun.pokio:id/bar_blinds").swipe(point_a, center)
    #         # #Minimum buy-in (€)
    #         poco("com.qfun.pokio:id/bar_min_buy_in").swipe(point_a, center)
    #         # #Maximum buy-in (€)
    #         poco("com.qfun.pokio:id/bar_max_buy_in").swipe(point_a, center)
    #         poco(text="Maximum buy-in (€)").swipe([0.0, -0.5])
    #         # Time bank
    #         poco("com.qfun.pokio:id/rb_time_bank_20s").click()
    #         # 同时发牌
    #         #         poco("com.qfun.pokio:id/rb_dealing_concurrent")
    #         # 按顺序发
    #         poco("com.qfun.pokio:id/rb_dealing_sequence").click()

    #         # # GPS/IP restrictions
    #         poco("com.qfun.pokio:id/sb_std_gps_ip").click()
    #         # # Hide players stats
    #         poco("com.qfun.pokio:id/sb_stats_hide_players").click()
    #         # # Hide table stats
    #         poco("com.qfun.pokio:id/sb_stats_hide_table").click()

    else:
        poco(text="Stakes (€)").swipe([0.0, -0.45])  # 滑动动使元素可见

#         point_a = [0.0, 0.0]
#         center = [0.4, 0.0]
#         poco("com.qfun.pokio:id/bar_blinds").wait(2).swipe(point_a, center)       # Stakes (€)
#         poco("com.qfun.pokio:id/bar_min_buy_in").wait(2).swipe(point_a, center)   # Minimum buy-in (€)
#         poco("com.qfun.pokio:id/bar_max_buy_in").wait(2).swipe(point_a, center)   # Maximum buy-in (€)
#         poco("com.qfun.pokio:id/bar_ante").wait(2).swipe(point_a, center)     # Ante (€)
#         poco("com.qfun.pokio:id/bar_player").wait(2).swipe(point_a, center)   # Table size

#         poco(text="Table size").swipe([0.0, -0.48])  # 滑动动使元素可见
# 牌局设置（开关设置）
# ====================================================================
#         poco("com.qfun.pokio:id/sb_std_straddle").click() # Auto-straddle
#         poco("com.qfun.pokio:id/sb_std_muck").click()     # Auto-muck
#         poco("com.qfun.pokio:id/sb_std_gps_ip").click()   # GPS/IP restrictions
#         poco("com.qfun.pokio:id/sb_stats_hide_players").click()   # Hide players stats
#         poco("com.qfun.pokio:id/sb_stats_hide_table").click()     # Hide table stats


# 各种玩法牌桌创建
# =========================================================================================
def Create_Ring_table_process(tables):
    """现金牌桌创建的流程"""
    poco("com.qfun.pokio:id/tv_create_game").click()  # Create table按钮
    # 牌局设置（滑动设置）
    # =========================================================================================
    if tables == "Hold'em":
        print("Hold'em")
        poco("com.qfun.pokio:id/rb_play_type_hold").click()  #

    elif tables == "Omaha":
        print("Omaha")
        poco("com.qfun.pokio:id/rb_play_type_omaha").click()

    elif tables == "Drawmaha":
        print("Drawmaha")
        poco("com.qfun.pokio:id/rb_play_type_draw").click()

    elif tables == "PLO5":
        print("PLO5")
        poco("com.qfun.pokio:id/rb_play_type_plo5").click()
        
    elif tables == "OFC":
        print("OFC")
        poco("com.qfun.pokio:id/rb_play_type_ofc").click()
    poco("com.qfun.pokio:id/et_table_name").set_text(tables)  # 填写所创建的桌子名称
    poco("com.qfun.pokio:id/tv_create").click()  # Create创建
    print("创建完成，准备退出")
    _Game_table_leave() #退出牌局
    # _Terminate_table_tablesettings()


def Create_Tournament_table_process(tables, formats):
    """赛事牌桌创建的流程"""
    try:
        poco("com.qfun.pokio:id/tv_create_game").click()  # Create table按钮
        print("Hold'em", formats)
        poco("com.qfun.pokio:id/rb_play_type_hold").click()
        if formats == "SNG":
            poco("com.qfun.pokio:id/rb_game_type_sng").click()
            poco("com.qfun.pokio:id/et_table_name").wait(2).set_text(tables + formats)  # 填写所创建的赛事桌子名称
            poco("com.qfun.pokio:id/et_game_desc").set_text(
                "This Hold'em event is for automated testing only,please do not Register")  # 50描述限制
            # 其他设置省得
            poco("com.qfun.pokio:id/tv_create").click()  # Create创建
        elif formats == "MTT":
            poco("com.qfun.pokio:id/rb_game_type_mtt").click()
            poco("com.qfun.pokio:id/et_table_name").wait(2).set_text(tables + formats)  # 填写所创建的赛事桌子名称
            poco("com.qfun.pokio:id/et_game_desc").set_text(
                "This Hold'em event is for automated testing only,please do not Register")  # 50描述限制
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
        elif formats == "Ring":
            print("现金桌不在该方法创建")
        else:
            print()
    except:
        print("赛事创建失败异常告警")
    else:
        print("赛事创建成功")
    # 赛事报名


def Register_Tournament_table():
    """赛事报名"""
    # 取消赛事报名
    try:
        if poco(text="Structure").wait(1).exists():  # SNG赛事独有的
            print("SNG")
            tournamen = "SNG"
        else:
            print("MTT")
            tournamen = "MTT"
        if poco("com.qfun.pokio:id/tv_apply").get_text() == "Register":  # 赛事报名
            poco("com.qfun.pokio:id/layout_opera").click()  # 报名Register报名
            poco("com.qfun.pokio:id/tv_confirm").click()  # 确认报名弹窗Yes
            sleep(0.2)
            if poco(text="Deposit").wait(2).exists():  # 余额不足提示充值
                poco("com.qfun.pokio:id/tv_cancel").wait(2).click()
                print("余额不足，取消报名")
            elif tournamen == "MTT":  # MTT有一个时间提示的弹窗
                poco(text="Got it").click()  # 注销成功
        if poco("com.qfun.pokio:id/tv_apply").get_text() != "Register":  # 状态发生变化判断验证成功
            print("赛事报名成功")
    except:
        print("赛事报名失败异常告警")

def Unregister_Tournament_table():
    """取消报名"""
    # 取消赛事报名
    try:
        if poco("com.qfun.pokio:id/tv_apply").get_text() == "Unregister":  # 取消报名
            poco("com.qfun.pokio:id/layout_opera").click()  # 取消报名
            poco("com.qfun.pokio:id/tv_confirm").click()  # 确认报名弹窗Yes
            poco(text="Got it").click()  # 注销成功
            sleep(0.2)
            if poco("com.qfun.pokio:id/tv_apply").get_text() == "Register":  # 验证状态是否变更来判断是否取消
                print("取消报名验证成功")

        elif poco("com.qfun.pokio:id/tv_apply").get_text() == "MTT is preparing":
            print("开赛倒计时两分钟，无法取消报名")
        elif poco("com.qfun.pokio:id/tv_apply").get_text() == "Join the tournament":
            print("进入赛事桌子准备，无法取消报名")
        elif poco("com.qfun.pokio:id/tv_apply").get_text() == "Register":
            print("赛事还未报名成功，无法取消报名")
    except:
        print("取消赛事报名异常告警")

def Cancel_Tournament_table(tname):
    """解散赛事牌桌"""
    # 解散赛事比赛
    try:
        poco(text=tname).wait(1).click()  # 点击赛事进行详情页
        sleep(1)
        if poco("com.qfun.pokio:id/tv_title_center").wait(2).get_text() == tname:  # 标题栏赛事名字
            poco("com.qfun.pokio:id/fl_title_right").click()  # Cancel赛事
            poco("com.qfun.pokio:id/tv_confirm").click()  # Yes确认取消赛事
            if poco(text="OK").wait(2).exists():  # 提示解散成功弹窗
                print("解散赛事验证成功")
                poco(text="OK").click()
            elif poco("com.qfun.pokio:id/layout_opera").exists():  # 解散
                print("赛事取消失败了。请稍后再试")
                # 异常抛出
                keyevent("BACK")  # 返回不要影响其他流程
    except:
        print("解散赛事牌桌异常告警")


def _Game_table_leave():
    """退出牌局"""
    try:
        sleep(3)
        pocos("bnt_menu").wait(15).click('center')
        lenns=len(pocos("<LayerColor | Tag = -1>").child("Button"))
        pocos("<LayerColor | Tag = -1>").child("Button")[lenns-1].click('center')
        print("退出成功")
        # pocos("dialog_bg_9scale").child("btn_ok").click()

    except:
        print("退出牌局异常日志写入")

def _Terminate_table_tablesettings(table):
    """结束指定的现金桌子"""
    try:
        if poco(text=table).wait(1).exists():
            poco(text=table).wait(1).click()
        else:   #桌子太多，需要滑动来找
            swipe([0.0, -0.50])
            poco(text=table).wait(1).click()
        sleep(2)
        pocos("bnt_menu").wait(15).click('center')
        lenns=len(pocos("<LayerColor | Tag = -1>").child("Button"))
        pocos("<LayerColor | Tag = -1>").child("Button")[0].click('center')
        pocos("btn_end").wait(3).click('center')
        pocos("dialog_bg_9scale").child("btn_ok").click()
        print("解散",table,"牌桌成功")
    except:
        print("解散牌局失败异常告警")


def All_Create_Ring_table():
    """创建所有类型的现金桌"""
    Create_Ring_table_process(holdem)  # # ===创建Hold'em玩法牌桌===============================================
    Create_Ring_table_process(omaha)   # # ===创建Omaha玩法牌桌=================================================
    Create_Ring_table_process(drawma)  # # ===创建Drawmaha玩法牌桌===============================================
    Create_Ring_table_process(plo5)    # # ===创建PLO5玩法牌桌=================================================
    Create_Ring_table_process(ofc)     # # ===创建OFC玩法牌桌=================================================

def All_Create_Tourmant_table():
    """创建所有玩法的赛事桌"""
    Create_Tournament_table_process(holdem, sng)  # # ===创建Hold'em玩法SNG牌桌=============
    print("继续创建赛事")
    keyevent("BACK")
    Create_Tournament_table_process(holdem, mtt)  # # ===创建Hold'em玩法MMT牌桌=============
    keyevent("BACK")

def All_Terminate_Ring_table():
    """结束所选的桌子"""
    _Terminate_table_tablesettings(omaha)
    _Terminate_table_tablesettings(drawma)
    _Terminate_table_tablesettings(plo5)
    _Terminate_table_tablesettings(ofc)
   #解散以上桌子，留下Holdem桌子供打牌
    
if __name__ == '__main__':
    holdem = "Hold'em"
    omaha = "Omaha"
    drawma = "Drawmaha"
    ofc = "OFC"
    plo5 = "PLO5"
    ring = "Ring"
    sng = "SNG"
    mtt = "MTT"
    print("开始")
    _Clubs_Tables_process("EEE") #选择操作的俱乐部
    All_Create_Ring_table() #创建所有的现金桌
    All_Terminate_Ring_table()  #结束多个指定的现金桌子
    # All_Create_Tourmant_table() #创建所有的赛事

