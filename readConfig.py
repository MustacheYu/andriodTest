# encoding=utf-8
import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")


class ReadConfig(object):
    def __init__(self):
        fd = open(configPath)
        try:
            data = fd.read()
            # 移除 BOM
            if data[:3] == codecs.BOM_UTF8:
                data = data[3:]
                datafile = codecs.open(configPath, "w")
                datafile.write(data)
                datafile.close()
        finally:
            fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding="utf-8-sig")

    def get_de(self, name):
        value = self.cf.get("DRIVER", name)
        return value

    def get_cmd(self, name):
        value = self.cf.get("CMD", name)
        return value

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value


