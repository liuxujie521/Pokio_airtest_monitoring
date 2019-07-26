# -*- encoding=utf8 -*-
__author__ = "zhouming"

from test_one import *
from airtest.core.api import *

dev1 = connect_device("Android://127.0.0.1:5037/127.0.0.1:62026?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH")#
dev2 = connect_device("Android://127.0.0.1:5037/127.0.0.1:62027?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH")#


def gemetable_test_01():
    """流程进桌打牌流程"""
    set_current(0)  # 切换到一台机器
    pocos = StdPoco(15004, dev1)
    po1 = GameOperationMethod(pocos)
    wallet1=po1._Game_table_walletget() #获取余额
    po1._Game_table_sitdown()           #坐下来
    print("切换第二台")
    set_current(1)  # 切换到一台机器
    pocos = StdPoco(15004, dev2)
    po2 = GameOperationMethod(pocos)
    wallet2=po2._Game_table_walletget() #获取余额
    po2._Game_table_sitdown()           #坐下来

    set_current(0)  # 切换到一台机器
    pocos = StdPoco(15004, dev1)
    pocos("btn_begingame").wait(1).click()#点击开始
    if pocos("<Layer | Tag = -1>").child("<Layer | Tag = -1>")[1].child("default_user")[0].offspring("<Node | Tag = 136").wait(8).exists():
        #判断大小盲是否出现来断定是否发牌了
        for i in range(3):
            set_current(0)  # 切换到一台机器
            pocos = StdPoco(15004, dev1)
            if pocos("btn_fold").wait(1.5).exists():
                print("找到设备01玩家flod元素")
                chips = po1._Game_table_chipget()
                print("当前下注所剩筹码是", chips)
                if i == 1:
                    po1._Game_table_raise()  # 加注全推
                else:
                    po1._Game_table_check()  # 平跟
            else:
                set_current(1)
                pocos = StdPoco(15004, dev2)
                if pocos("btn_fold").wait(1).exists():
                    print("找到设备02玩家flod元素")
                    chipss = po2._Game_table_chipget()
                    print("当前下注所剩筹码是", chipss)
                    if i == 1:
                        po2._Game_table_raise()  # 加注全
                    else:
                        po2._Game_table_check()  # 平跟
        sleep(3)  # 等待弹窗

        for i in range(2):
            # ====弹窗处理=============================================
            set_current(0)  # 切换到一台机器
            pocos = StdPoco(15004, dev1)
            if pocos("main_panel").wait(1).exists():
                print("在玩家111上找到弹窗")
                po1.test_dddd()
                print("1111弹窗已经处理")
            else:
                set_current(1)
                pocos = StdPoco(15004, dev2)
                if pocos("main_panel").wait(1).exists():
                    print("在玩家222上找到弹窗")
                    po2.test_dddd()
                    print("2222弹窗已经处理")
                else:
                    print("胜率50%,不做弹窗处理")
            sleep(3)  # 处理完后等待加载后面一次弹窗
    
    set_current(0)  # 切换到一台机器
    pocos = StdPoco(15004, dev1)
    if pocos("dialog_bg_9scale").wait(2).exists():  #判断Add chips继续加注弹窗
        pocos("panel_tip").child("btn_cancel").click()  #取消加注        
        po1._Game_table_observe()   #站起
        set_current(1)  # 切换到一台机器
        po2._Game_table_observe()   #站起
    else:
        set_current(1)  # 切换到一台机器
        pocos = StdPoco(15004, dev2)
        print("切换第二台")
        if pocos("dialog_bg_9scale").wait(2).exists():  #判断Add chips继续加注弹窗
            pocos("panel_tip").child("btn_cancel").click()  #取消加注      
            po2._Game_table_observe()   #站起
            set_current(0)  # 切换到一台机器
            po1._Game_table_observe()   #站起

    set_current(0)  # 切换到一台机器
    # pocos = StdPoco(15004, dev1)
    po1._Game_table_tablesettings()
    
    
if __name__ == '__main__':
    gemetable_test_01()