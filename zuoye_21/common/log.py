import  logging
class Mylog:
    def __init__(self,level1,level2,level3,level4,level5,logname,output):
        self.l1 = level1
        self.l2 = level2
        self.l3 = level3
        self.l4 = level4
        self.l5 = level5
        self.n=logname
        self.o=output
    def creatlog(self):
        self.my_logger=logging.getLogger(self.n) #新建一个名为routerlog的日志收集器，存到变量my_logger里
        self.my_logger.setLevel(self.l4) #指定收集级别
    def setformatter(self):
        self.fmt=logging.Formatter(self.o) #指定输出格式
    def setstream(self):
        self.LS=logging.StreamHandler() #指定输出渠道
        self.LS.setLevel(self.l4)#指定输出级别
        self.LS.setFormatter(self.fmt) #设置输出格式
    def setfile(self):
        self.file_handler=logging.FileHandler(self.n,encoding='utf-8') #指定输出文本渠道
        self.file_handler.setLevel(self.l4) #指定输出级别
        self.file_handler.setFormatter(self.fmt)
    def ADDhandlet(self): #配合
        self.my_logger.addHandler(self.LS)
        self.my_logger.addHandler(self.file_handler)
    def printcuowu(self): #输出
        self.my_logger.debug(self.l1)
        self.my_logger.info(self.l2)
        self.my_logger.warning(self.l3)
        self.my_logger.error(self.l4)
        self.my_logger.critical(self.l5)
if __name__=='__main__':
    M=Mylog('debug','info','warning','ERROR','critical','dinglog','%(asctime)s-%(filename)s-%(levelname)s-日志信息:%(message)s')
    M.creatlog()
    M.setformatter()
    M.setstream()
    M.setfile()
    M.ADDhandlet()
    M.printcuowu()

