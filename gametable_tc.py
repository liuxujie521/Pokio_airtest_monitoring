# -*- encoding=utf8 -*-
__author__ = "zhouming"


from airtest.core.api import *
from gametable_page import *
from pokio_crm import *

dev1 = connect_device(
    "Android://127.0.0.1:5037/127.0.0.1:62026?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH")  #
dev2 = connect_device(
    "Android://127.0.0.1:5037/127.0.0.1:62027?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH")  #


def Gametable_test_01(table,clubs):
    """
    流程进桌打牌流程
    :param table: 需要操作的桌子名字
    :param clubs: 需要操作的俱乐部名字
    :return:
    """
    set_current(0)  # 切换到一台机器
    print("第一台")
    pocos = StdPoco(15004, dev1)  # 实例化游戏内元素指针
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)  # 实例化安卓原生指针
    po1 = GameOperationMethod(pocos,poco)
    po1._Entrance_table(table)  # 指定性入桌（桌子名）
    wallet1 = po1._Game_table_walletget()  # 获取余额
    print(wallet1)
    if po1._Game_table_sitdown():  # 坐下来
        print("===非正常执行中断===")
        return
    print("切换第二台")
    set_current(1)  # 切换到一台机器

    pocos = StdPoco(15004, dev2)  # 实例化游戏内元素指针
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)  # 实例化安卓原生指针
    po2 = GameOperationMethod(pocos, poco)
    po2._Entrance_table(table)
    wallet2 = po2._Game_table_walletget()  # 获取余额
    if po2._Game_table_sitdown():  # 坐下来
        print("===非正常执行中断===")
        return
    set_current(0)  # 切换到一台机器
    pocos = StdPoco(15004, dev1)
    pocos("btn_begingame").wait(1).click()  # 点击开始
    if pocos("<Layer | Tag = -1>").child("<Layer | Tag = -1>")[1].child("default_user")[0].offspring(
            "<Node | Tag = 136").wait(8).exists():
        # 判断大小盲注是否出现来断定是否发牌了
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

        for i in range(2):  # ==弹窗处理=============================================
            set_current(0)  # 切换到一台机器
            pocos = StdPoco(15004, dev1)
            if pocos("main_panel").wait(1).exists():
                print("在玩家111上找到弹窗")
                po1.Close_Windows_processing()
                print("1111弹窗已经处理")
            else:
                set_current(1)
                pocos = StdPoco(15004, dev2)
                if pocos("main_panel").wait(1).exists():
                    print("在玩家222上找到弹窗")
                    po2.Close_Windows_processing()
                    print("2222弹窗已经处理")
                else:
                    print("胜率50%,不做弹窗处理")
            sleep(3)  # 处理完后等待加载后面一次弹窗
    else:
        print("没有开牌")
    set_current(0)  # 切换到一台机器
    pocos = StdPoco(15004, dev1)
    if pocos("dialog_bg_9scale").wait(2).exists():  # 判断Add chips继续加注弹窗
        pocos("panel_tip").child("btn_cancel").click()  # 取消加注
        po1._Game_table_observe()  # 站起
        set_current(1)  # 切换到一台机器
        po2._Game_table_observe()  # 站起
    else:
        set_current(1)  # 切换到一台机器
        pocos = StdPoco(15004, dev2)
        print("切换第二台")
        if pocos("dialog_bg_9scale").wait(2).exists():  # 判断Add chips继续加注弹窗
            pocos("panel_tip").child("btn_cancel").click()  # 取消加注
            po2._Game_table_observe()  # 站起
            set_current(0)  # 切换到一台机器
            po1._Game_table_observe()  # 站起

    set_current(0)  # 切换到一台机器
    pocos = StdPoco(15004, dev1)
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    po1 = GameOperationMethod(pocos, poco)
    po1._Game_table_tablesettings()  # 结束该桌子
    sleep(2)#页面加载时间等待
    date, tablename, biggestpot, username_01, profit_01, username_02, profit_02=po1._Tablesend_achievement_dataget()  # 结算页面数据获取
    sleep(1)
    timett,dtattt=po1._Wallet_Netrevenue_dataget(clubs)

    if date==timett and dtattt=="+€1.20":
        print("俱乐部净收入正常")
    else:
        print("不")
if __name__ == '__main__':
    """初始化数据，执行"""
    table = "HHH"  # 桌子名字
    clubs = "EEE"
    print("开始")
    CRM_main()  #初始化用户余额为25
    print("CRM")
    Gametable_test_01(table,clubs)  # 从选择牌桌进入、余额获取、坐下、平跟、加注、保险弹窗处理、站起、结束牌桌，
    print("结束")