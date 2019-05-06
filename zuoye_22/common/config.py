
import configparser

from zuoye_022.common import contants

class ReadConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(contants.global_file)  # 先加载global
        switch = self.config.getboolean('switch', 'on')
        if switch:  # 开关打开的时候，使用online的配置
            self.config.read(contants.online_file, encoding='utf-8')
        else:  # 开关关闭的时候，使用test的配置
            self.config.read(contants.test_file, encoding='utf-8')

    def get(self, section, option):
        return self.config.get(section, option)
    def get_int(self, section, option):
        return self.config.getint(section, option)

doconfig = ReadConfig()
