# 3，学习logging模块使用（百度)
import logging

#配置logging在控制台输出日志
#设置日志级别，输出格式
# logging.basicConfig(level=logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)#创建记录器
# Log4j建议只使用四个级别，优先级从高到低分别是 ERROR、WARN、INFO、DEBUG

# logger.info("Start print log")
# logger.debug("Do something")#不满足级别，不会输出
# logger.warning("Something maybe fail.")
# logger.info("Finish")

# logging.basicConfig函数各参数：
# filename：指定日志文件名；
# filemode：和file函数意义相同，指定日志文件的打开模式，'w'或者'a'；
# format：指定输出的格式和内容，format可以输出很多有用的信息，


#将日志写到文件中

#创建文件助手，将日志写到文件中
handler = logging.FileHandler("D:\Python_sup\log.txt",mode="a")#以添加的形式记录日志
handler.setLevel(logging.ERROR)#设置文件助手日志级别
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)#设置日志格式

#创建记录器
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.ERROR)#设置日志级别
logger.addHandler(handler)#给记录器添加文件助手

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.error("Finish")
