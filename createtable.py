# -*- encoding=utf8 -*-
__author__ = "Admin"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from poco.drivers.std import StdPoco
pocos = StdPoco()


def _Clubs_Tables_process(clubn):
    """进入俱乐部的桌子创建"""
    poco("com.qfun.pokio:id/main_footbar_clubsdbtn").wait(1).click('center')    #确认在Club页面
    poco(text=clubn).wait(1).click()    #注意：不能出现同名的俱乐部,
    sleep(1)    #加载时间等待
    poco("com.qfun.pokio:id/rb_tab_table").click('center')  #Table
    
def _Table_settings(tables):
    """创桌的相关子设置"""
    # 牌局设置（滑动设置）
    # =========================================================================================
    if tables == "OFC":     #只有OFC的创桌所填的信息不一样
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

    poco("com.qfun.pokio:id/tv_create_game").click()    #Create table按钮
    # 牌局设置（滑动设置）
    # =========================================================================================
    if tables == "Hold'em":
        print("Hold'em")
        poco("com.qfun.pokio:id/rb_play_type_hold").click() #

    elif tables == "Omaha":
        print("Omaha")
        poco("com.qfun.pokio:id/rb_play_type_omaha").click()

    elif tables == "Drawmaha":
        print("Drawmaha")
        poco("com.qfun.pokio:id/rb_play_type_draw").click()

    elif tables == "OFC":
        print("OFC")
        poco("com.qfun.pokio:id/rb_play_type_ofc2").click()
        
    elif tables == "PLO5":
        print("PLO5")
        poco("com.qfun.pokio:id/rb_play_type_plo5").click()
        
    poco("com.qfun.pokio:id/et_table_name").set_text(tables)    #填写所创建的桌子名称
    
def Create_Tourmant_table_process(tables,formats):
    """赛事牌桌创建的流程"""
    try:
        poco("com.qfun.pokio:id/tv_create_game").click()    #Create table按钮
        print("Hold'em",formats)
        poco("com.qfun.pokio:id/rb_play_type_hold").click()
        if formats == "Ring":
            poco("com.qfun.pokio:id/rb_game_type_ring").click()
        elif formats == "SNG":
            poco("com.qfun.pokio:id/rb_game_type_sng").click()
        elif formats == "MTT":
            poco("com.qfun.pokio:id/rb_game_type_mtt").click()

        poco("com.qfun.pokio:id/et_table_name").wait(2).set_text(tables+formats)    #填写所创建的赛事桌子名称

        poco("com.qfun.pokio:id/et_game_desc").set_text("This Hold'em event is for automated testing only,please do not Register") #50描述限制

        poco(text="Buy-in (€)").swipe([0.0, -0.48]) #滑动动使元素可见
        sleep(1)
        poco("com.qfun.pokio:id/tv_mtt_start_time").wait(2).click('center')     #点击时间设置

        poco("com.qfun.pokio:id/month").wait(3).swipe([0.0,-0.06]) #滑动月份就行
        poco("com.qfun.pokio:id/tv_sure").click()   #Done确认时间
        poco("com.qfun.pokio:id/tv_create").click()  # Create创建
        
        poco("com.qfun.pokio:id/tv_cancel").click()
        poco("com.qfun.pokio:id/tv_confirm")
    except:
        print("赛事创建失败")
    else:
        print("赛事创建成功")
# 赛事报名
    try:
        poco("com.qfun.pokio:id/layout_opera").click() #Register报名  
        poco("com.qfun.pokio:id/tv_confirm").click()#确认报名弹窗Yes
        poco(text="Got it").click()
        sleep(2)        
        
    except:       
        print("赛事报名失败")
    else:
        print("报名成功")
#取消赛事报名       
    try:   
        poco("com.qfun.pokio:id/layout_opera").click()  #取消报名
        poco("com.qfun.pokio:id/tv_confirm").click()    #确认报名弹窗Yes
        poco(text="Got it").click() #注销成功
        
    except:       
        print("取消赛事报名失败")
    else:
        print("取消赛事报名成功")
        
#解散赛事比赛
    try:
        sleep(2)
        poco("com.qfun.pokio:id/fl_title_right").click() #Cancel赛事
        poco("com.qfun.pokio:id/tv_confirm").click()#Yes确认取消赛事
        poco(text="OK").click()
    except:
        print("解散赛事牌桌失败")
    else:
        print("解散赛事成功")
# ===========================================    


    poco("com.qfun.pokio:id/tv_create").click()  # Create创建
    if poco("com.qfun.pokio:id/tv_cancel").exists():    #重名弹窗处理
        poco("com.qfun.pokio:id/tv_cancel").click()     #OK，got it
    sleep(2)    #poco与pocos实例切换等待
    pocos("bnt_menu").wait(15).click('center')    
    lenpos=len(pocos("<Layer | Tag = -1>").child("<LayerColor | Tag = -1>").child("<LayerColor | Tag = -1>").child("Button"))   #统计有多少个按钮
    pocos("<LayerColor | Tag = -1>").child("Button")[lenpos-1].click('center') #最后一个按钮就是Leave退出游戏按钮

def kfkdf(tables):
    """判断俱乐部是否创建成功"""
        
    lenn = len(poco("android:id/list").child("android.widget.LinearLayout"))
    for i in range(lenn):
        actual = poco("android:id/list").child("android.widget.LinearLayout")[i].offspring(
            "com.qfun.pokio:id/tv_game_name").get_text()
        if actual == tables:
            print(tables, "牌桌创建成功！！")
            break
        
    else:
        x, y = poco("android.widget.LinearLayout").get_position()
        dir = [0, -0.5]
        poco.swipe([x, y], direction=dir)#元素滑动，使元素可见
        sleep(2)
        lenn = len(poco("android:id/list").child("android.widget.LinearLayout"))
        for i in range(lenn-1,1,-1):
            actual = poco("android:id/list").child("android.widget.LinearLayout")[i].offspring(
                "com.qfun.pokio:id/tv_game_name").get_text()
            if actual == tables:
                print(tables, "牌桌创建成功！！")
                break
        else:
            print(tables, "牌桌创建失败！！")

    
def _Tables_dissolve_process():
    """指定解散牌桌"""
    
    
    
#==设置控制层====================================================================

holdem = "Hold'em"
omaha = "Omaha"
drawma = "Drawmaha"
ofc = "OFC"
plo5 = "PLO5"

# Game format设置(该设置只对Hold'em有效)
# =========================================================================================
ring = "Ring"
sng = "SNG"
mtt = "MTT"


# ===创建Hold'em玩法牌桌=================================================
_Clubs_Tables_process("EEE")
Create_Tourmant_table_process(holdem,mtt)


# def Ring_table_process():
#     """现金桌创建"""
#     Create_table_process(holdem, ring)  # # ===创建Hold'em玩法牌桌===============================================
#     Create_table_process(omaha, ring)   # # ===创建Omaha玩法牌桌=================================================
#     Create_table_process(drawma, ring)  # # ===创建Drawmaha玩法牌桌===============================================
#     Create_table_process(ofc, ring)     # # ===创建OFC玩法牌桌=================================================
#     Create_table_process(plo5, ring)    # # ===创建PLO5玩法牌桌=================================================

# def Tourmant_table_process():
#     """赛事桌创建"""
#     Create_table_process(holdem, mtt)  # # ===创建Hold'em玩法牌桌=================================================
#     pass

# if __name__ == '__main__':
# #     _Clubs_Tables_process()
#     Ring_table_process()