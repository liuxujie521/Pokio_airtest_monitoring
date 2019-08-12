# -*- encoding=utf8 -*-
__author__ = "zhouming"

from gametable_tc import *
from createtable_page import *
from decorator import *
#webhookq=""	#主报告群
@time_consuming
def main_Run():
    """主执行"""
    cret = TableOperationMethod()
    cret.main_createtable()
    main_gametable()#执行游戏内的打牌流程操作

if __name__ == '__main__':
    count = 0
    for i in range(3):
        print("自动化执行第%d次"%i)
        try:
            main_Run()
        except:
            count =0
            print("测试操作流程出现异常")
        else:
            count +=1   #自增
            bogou=str(i)+ "所写流程执行都已验证通过"
            dingding_Disaster(webhook,bogou, user=zm, Atall=False)
            print("所写流程执行都已验证通过")
            if count%3==0:
                numcount="连续执行 "+str(count)+" 次运行成功了"
                print(numcount)
                dingding_Disaster(webhook, numcount, user=zm, Atall=False)