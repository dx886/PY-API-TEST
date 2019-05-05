import logging

from python_study.zuoye import doconfig
from python_study.zuoye.zuoye_22.common import contants


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel('DEBUG')
    fmt = "%(asctime)s -  %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d ]"
    formatter = logging.Formatter(fmt=fmt)
    level1 = doconfig.get('Level', 'level1')
    level2= doconfig.get('Level', 'level2')
    console_handler = logging.StreamHandler()  # 控制台
    console_handler.setLevel(level2)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(contants.log_dir + '/case.log')
    file_handler.setLevel(level2)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


logger = get_logger('case')
logger.info('测试开始啦')
logger.error('测试报错')
logger.debug('测试数据')
logger.info('测试结束')
