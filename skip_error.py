# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
# from airtest.core.api import connect_device
# dev = connect_device("Android://127.0.0.1:5037/ORYTDMMB5PJRDE7D")  # OPPO R15
# poco = AndroidUiautomationPoco(dev)

def SkipMethod():
    isGuide = True
    Fingerprint=poco("com.qfun.pokio:id/checkbox")#指纹登陆
    PopUp=poco("com.qfun.pokio:id/iv_content")#登陆弹框
    Guide=poco("com.qfun.pokio:id/iv_next")#新手引导
    KycPop=Pass #KYC弹框
    while isGuide:
        try:
            ui=poco.wait_for_any([Fingerprint,PopUp,Guide],timeout=60)
            #   没找到以上内容则不进行操作
        except:
            isGuide = False
            print('没有需要跳过的内容')
            break
        if ui is Fingerprint:
            Fingerprint.click()
            print('已跳过指纹引导')
        elif ui is PopUp:
            PopUp.click()
            print('已跳过弹框')
        elif ui is Guide:
            Guide.click()
            print('已跳过新手引导')
        #   找到则进行点击跳过