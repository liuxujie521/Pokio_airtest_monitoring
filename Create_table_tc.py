# -*- encoding=utf8 -*-
__author__ = "Admin"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from poco.drivers.std import StdPoco
pocos = StdPoco()



if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android:///",
    ])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)


# 各种玩法牌桌创建
# # =========================================================================================
# def Create_table_process(tables, formats):
#     # #======判断当前俱乐部=============================================
#     #
#     # lens=len(poco("android:id/list").child("android.widget.LinearLayout"))

#     poco("com.qfun.pokio:id/tv_create_game").click()
#     # 牌局设置（滑动设置）
#     # =========================================================================================
#     if tables == "Hold'em":
#         print("Hold'em")
#         poco("com.qfun.pokio:id/rb_play_type_hold").click()
#         if formats == "Ring":
#             poco("com.qfun.pokio:id/rb_game_type_ring").click()
#         elif formats == "SNG":
#             poco("com.qfun.pokio:id/rb_game_type_sng").click()
#         elif formats == "MTT":
#             poco("com.qfun.pokio:id/rb_game_type_mtt").click()

#         poco("com.qfun.pokio:id/et_table_name").set_text(tables)

#     elif tables == "Omaha":
#         print("Omaha")
#         poco("com.qfun.pokio:id/rb_play_type_omaha").click()
#         poco("com.qfun.pokio:id/et_table_name").set_text(tables)

#     elif tables == "Drawmaha":
#         print("Drawmaha")
#         poco("com.qfun.pokio:id/rb_play_type_draw").click()
#         poco("com.qfun.pokio:id/et_table_name").set_text(tables)

#     elif tables == "OFC":
#         print("OFC")
#         poco("com.qfun.pokio:id/rb_play_type_ofc").click()
#         poco("com.qfun.pokio:id/et_table_name").set_text(tables)

#     elif tables == "PLO5":
#         print("PLO5")
#         poco("com.qfun.pokio:id/rb_play_type_plo5").click()
#         poco("com.qfun.pokio:id/et_table_name").set_text(tables)

#     # 牌局设置（滑动设置）
#     # =========================================================================================
#     if tables == "OFC":
#         poco(text="Stakes (€)").swipe([0.0, -0.35])  # 滑动动使元素可见
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

#     else:
#         poco(text="Stakes (€)").swipe([0.0, -0.45])  # 滑动动使元素可见
# #         point_a = [0.0, 0.0]
# #         center = [0.4, 0.0]

# #         # Stakes (€)
# #         poco("com.qfun.pokio:id/bar_blinds").wait(2).swipe(point_a, center)

# #         # #Minimum buy-in (€)
# #         poco("com.qfun.pokio:id/bar_min_buy_in").wait(2).swipe(point_a, center)

# #         # #Maximum buy-in (€)
# #         poco("com.qfun.pokio:id/bar_max_buy_in").wait(2).swipe(point_a, center)

# #         # #Ante (€)
# #         poco("com.qfun.pokio:id/bar_ante").wait(2).swipe(point_a, center)

# #         # #Table size
# #         poco("com.qfun.pokio:id/bar_player").wait(2).swipe(point_a, center)

#         poco(text="Table size").swipe([0.0, -0.48])  # 滑动动使元素可见
#         # 牌局设置（开关设置）
#         # ====================================================================
#         # Auto-straddle
#         # #----------------------------------------------
# #         poco("com.qfun.pokio:id/sb_std_straddle").click()

# #         # # Auto-muck
# #         # #----------------------------------------------
# #         poco("com.qfun.pokio:id/sb_std_muck").click()

# #         # # GPS/IP restrictions
# #         # #----------------------------------------------
# #         poco("com.qfun.pokio:id/sb_std_gps_ip").click()

# #         # # Hide players stats
# #         # #----------------------------------------------
# #         poco("com.qfun.pokio:id/sb_stats_hide_players").click()

# #         # # Hide table stats
# #         # #----------------------------------------------
# #         poco("com.qfun.pokio:id/sb_stats_hide_table").click()

#     poco("com.qfun.pokio:id/tv_create").click()  # Create创建
#     if poco("com.qfun.pokio:id/tv_cancel").exists():
#         poco("com.qfun.pokio:id/tv_cancel").click()
    
#     sleep(5)
#     pocos("bnt_menu").wait(15).click('center')
#     pocos("<LayerColor | Tag = -1>").child("Button")[3].click('center')
        
#     lenn = len(poco("android:id/list").child("android.widget.LinearLayout"))
#     for i in range(lenn):
#         actual = poco("android:id/list").child("android.widget.LinearLayout")[i].offspring(
#             "com.qfun.pokio:id/tv_game_name").get_text()
#         if actual == tables:
#             assert_equal(actual, tables, tables + "牌桌创建成功！！")
#             break
        
#     else:
#         x, y = poco("android.widget.LinearLayout").get_position()
#         dir = [0, -0.5]
#         poco.swipe([x, y], direction=dir)#元素滑动，使元素可见
#         sleep(2)
#         lenn = len(poco("android:id/list").child("android.widget.LinearLayout"))
#         for i in range(lenn-1,1,-1):
#             actual = poco("android:id/list").child("android.widget.LinearLayout")[i].offspring(
#                 "com.qfun.pokio:id/tv_game_name").get_text()
#             if actual == tables:
#                 assert_equal(actual, tables, tables + "牌桌创建成功！！")
#                 break
#         else:
#             assert_equal(1, 1, tables + "牌桌创建失败！！")
            
#     pass





#============================================================================================

# def _Game_table_check():
#     """平跟"""
#     if pocos("btn_call").wait(1).exists():  #小盲位平跟
#         pocos("btn_call").wait(2).click()
#     else:
#         pocos("btn_look").wait(1).click()

# _Game_table_check()

# def _Game_table_raise():
#     """加注"""
#     pocos("btn_add").wait(19).click()
#     pocos("point_bar_end").click()   #ALL IN  全推
#     pocos("btn_sure").click()        #DONE   确认
    
# _Game_table_check()    
    
    
    
# def _Game_table_fold():
#     """弃牌"""
#     poco("btn_fold").wait(19).click()
    
    


#============================================================================================
# def _Game_table_sitdown():
#     """桌内坐下来"""
#     sleep(1)
#     pocos("<Layer | Tag = -1>").child("<Layer | Tag = -1>")[1].child("Button")[0].click('center')
#     pocos("panel_tip").child("btn_ok").click('center')
    
    
# _Game_table_sitdown()
    
    
    
    

# def _Game_table_leave():
#     """退出牌局"""
#     sleep(5)
#     pocos("bnt_menu").wait(15).click('center')    
#     lenns=len(pocos("<LayerColor | Tag = -1>").child("Button"))    
#     pocos("<LayerColor | Tag = -1>").child("Button")[lenns-1].click('center')     
# _Game_table_leave()    
# pocos("dialog_bg_9scale").child("btn_ok").click()

# def _Game_table_observe():
#     """桌内站起"""
#     sleep(5)
#     pocos("lbl_daytime").click()
#     pocos("bnt_menu").wait(15).click('center')    
#     lenns=len(pocos("<LayerColor | Tag = -1>").child("Button"))    
#     pocos("<LayerColor | Tag = -1>").child("Button")[0].click('center')     

# _Game_table_observe()

# def _Game_table_tablesettings():
#     """解散牌局"""
#     sleep(5)
#     pocos("bnt_menu").wait(15).click('center')    
#     lenns=len(pocos("<LayerColor | Tag = -1>").child("Button"))    
#     pocos("<LayerColor | Tag = -1>").child("Button")[0].click('center')    
#     pocos("btn_end").wait(3).click('center')
#     pocos("dialog_bg_9scale").child("btn_ok").click()
# _Game_table_tablesettings()




# def _Game_table_observe():
#     """桌内站起"""
#     sleep(5)
#     pocos("bnt_menu").wait(15).click('center')    
#     lenns=len(pocos("<LayerColor | Tag = -1>").child("Button"))    
#     pocos("<LayerColor | Tag = -1>").child("Button")[0].click('center')     
    
# _Game_table_observe()


# # 牌桌检查
# # =========================================================================================
# def Game_table_process():
#     quota_s=pocos("<Layer | Tag = -1>")[0].offspring("lbl_wallet").get_text()#获取总额度
#     pocos("<Layer | Tag = -1>")[0].child("<Layer | Tag = -1>")[1].child("Button")[7].click()
#     quot_a=pocos("<Layer | Tag = -1>")[0].child("<Layer | Tag = -1>")[3].offspring("lbl_carry_num").get_text()#获取Top up to数
#     pocos(text="Confirm").wait(2).click()
#     quot_b=pocos("<Layer | Tag = -1>")[0].offspring("lbl_wallet").get_text()
#     assert_equal(quot_b,quota_s-quot_a,"成功了")

    
    
#==设置控制层====================================================================
#-------------------------------------------------------------------------------
#Game type设置
# =========================================================================================
# holdem = "Hold'em"
# omaha = "Omaha"
# drawmaha = "Drawmaha"
# ofc = "OFC"
# plo5 = "PLO5"

# # Game format设置(该设置只对Hold'em有效)
# # =========================================================================================
# ring = "Ring"
# sng = "SNG"
# mtt = "MTT"


# # ===创建Hold'em玩法牌桌=================================================
# for i in range(50):
# Create_table_process(holdem, ring)  # 传参：牌桌类型、玩法

# # # ===创建Hold'em玩法牌桌=================================================
# Create_table_process(omaha, ring)

# # # ===创建Drawmaha玩法牌桌=================================================
# Create_table_process(drawmaha, ring)

# # # ===创建OFC玩法牌桌=================================================
# Create_table_process(ofc, ring)

# # # ===创建PLO5玩法牌桌=================================================
# Create_table_process(plo5, ring)


