# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from airtest.core.api import connect_device
dev = connect_device("Android://127.0.0.1:5037/ORYTDMMB5PJRDE7D")  # OPPO R15
poco = AndroidUiautomationPoco(dev)

def skip_fingerprint():
    print("skip_fingerprint")
    while poco("com.qfun.pokio:id/checkbox").wait(5).exists():
        print("AAA")
        poco("com.qfun.pokio:id/checkbox").click()
        poco("com.qfun.pokio:id/tv_cancel").click()
# ===========如果存在指纹绑定，跳过===============
def skip_pop_up():
    print("skip_pop_up")
    while poco("com.qfun.pokio:id/iv_content").wait(5).exists():
        print("BBB")
        poco("com.qfun.pokio:id/iv_close_ad").click()
# ===========如果存在登陆弹框，跳过===============
def skip_guide():
    print("skip_guide")
    while poco("com.qfun.pokio:id/iv_next").wait(5).exists():
        poco("com.qfun.pokio:id/iv_next").click()



