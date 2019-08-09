# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def skip_fingerprint():
    while poco("com.qfun.pokio:id/checkbox").wait(3).exists():
        poco("com.qfun.pokio:id/checkbox").click()
        poco("com.qfun.pokio:id/tv_cancel").click()
# ===========如果存在指纹绑定，跳过===============
def skip_pop_up():
    while poco("com.qfun.pokio:id/iv_content").wait(3).exists():
        poco("com.qfun.pokio:id/iv_close_ad").click()
# ===========如果存在登陆弹框，跳过===============
def skip_guide():
    while poco("com.qfun.pokio:id/iv_next").wait(3).exists():
        poco("com.qfun.pokio:id/iv_next").click()