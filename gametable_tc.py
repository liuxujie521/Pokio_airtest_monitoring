# -*- encoding=utf8 -*-
__author__ = "zhouming"

from gametable_page import *
from airtest.core.api import *

dev1 = connect_device("Android://127.0.0.1:5037/127.0.0.1:62026?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH")#
dev2 = connect_device("Android://127.0.0.1:5037/127.0.0.1:62027?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH")#


def	gemetable_test_01():
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
    po1 = GameOperationMethod(pocos)
    pocos("btn_begingame").wait(1).click()#点击开始
    if pocos("<Layer | Tag = -1>").child("<Layer | Tag = -1>")[1].child("default_user")[0].offspring("<Node | Tag = 136").wait(8).exists():
        #判断大小盲是否出现来断定是否发牌了
        for i in range(3):
            set_current(0)  # 切换到一台机器
            pocos = StdPoco(15004, dev1)
            aa = GameOperationMethod(pocos)
            if pocos("btn_fold").wait(1.5).exists():
                print("找到111玩家flod元素")
                chips = aa._Game_table_chipget()
                print("当前下注所剩筹码是", chips)
                if i == 1:
                    aa._Game_table_raise()  # 加注全推
                else:
                    aa._Game_table_check()  # 平跟
            else:
                set_current(1)
                pocos = StdPoco(15004, dev2)
                bb = GameOperationMethod(pocos)
                if pocos("btn_fold").wait(1).exists():
                    print("找到222玩家flod元素")
                    chipss = bb._Game_table_chipget()
                    print("当前下注所剩筹码是", chipss)
                    if i == 1:
                        bb._Game_table_raise()  # 加注全
                    else:
                        bb._Game_table_check()  # 平跟
        sleep(3)  # 等待弹窗

        for i in range(2):
            # ====弹窗处理=============================================
            set_current(0)  # 切换到一台机器
            pocos = StdPoco(15004, dev1)
            paa = GameOperationMethod(pocos)
            if pocos("main_panel").wait(1).exists():
                print("在玩家111上找到弹窗")
                paa.Close_Windows_processing()
                print("1111弹窗已经处理")
            else:
                set_current(1)
                pocos = StdPoco(15004, dev2)
                print("===============else")
                pbb = GameOperationMethod(pocos)
                if pocos("main_panel").wait(1).exists():
                    print("在玩家222上找到弹窗")
                    pbb.Close_Windows_processing()
                    print("2222弹窗已经处理")
                else:
                    print("胜率50%,不做弹窗处理")
            sleep(3)  # 处理完后等待加载后面一次弹窗

if __name__ == '__main__':
    gemetable_test_01()