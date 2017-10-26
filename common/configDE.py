# encoding=utf-8
import os
from selenium import webdriver
import readConfig as readConfig
from Log import Log

log = Log(logger="DriverEngine")
logger = log.get_logger()
localReadConfig = readConfig.ReadConfig()

checkPhone = localReadConfig.get_cmd("checkPhone")
viewPhone = localReadConfig.get_cmd("viewPhone")
viewAndroid = localReadConfig.get_cmd("viewAndroid")
installSoftware = localReadConfig.get_cmd("installSoftware")
uninstallSoftware = localReadConfig.get_cmd("uninstallSoftware")


# 检查手机是否连接
def connect_phone():
    value = os.popen(checkPhone)
    for data in value.readline():
        s_date = str(data)
        if s_date.find("device"):
            return True
    return False


# 获取设备名称
def get_device_name():
    device_list = []
    return_value = os.popen(viewPhone)
    for value in return_value.readlines():
        s_value = str(value)
        if s_value.rfind('device'):
            if not s_value.startswith("List"):
                device_list.append(s_value[:s_value.find('device')].strip())
    if len(device_list) != 0:
        return device_list[0]
    else:
        return None


# 获取安卓版本号
def get_android_version():
    return_value = str(os.popen(viewAndroid).read())
    if return_value != '':
        pop = return_value.rfind(str('='))
        return return_value[pop + 1:].strip()
    else:
        return None


# noinspection PyGlobalUndefined
class DriverEngine(object):

    def __init__(self):
        global baseurl, desired_caps
        platformname = localReadConfig.get_de("platformName")
        platformversion = get_android_version()
        devicename = get_device_name()
        apppackage = localReadConfig.get_de("appPackage")
        appactivity = localReadConfig.get_de("appActivity")
        unicodekeyboard = localReadConfig.get_de("unicodeKeyboard")
        resetkeyboard = localReadConfig.get_de("resetKeyboard")
        baseurl = localReadConfig.get_de("baseUrl")
        desired_caps = {"platformName": platformname, "platformVersion": platformversion, "deviceName": devicename,
                        "appPackage": apppackage, "appActivity": appactivity, "unicodeKeyboard": unicodekeyboard,
                        "resetKeyboard": resetkeyboard}

    @staticmethod
    def open_driver():
        driver = webdriver.Remote(baseurl, desired_caps)
        return driver
