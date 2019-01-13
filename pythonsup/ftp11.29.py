# 1，编写代码完成ftp文件上传下载功能
from ftplib import FTP
# 建立连接
ftp=FTP(host="192.168.12.23", user="Thomas", passwd='123456')
print(ftp)

#上传文本、图片、音乐
def Upper(orifilename,tofilename):
    with open(orifilename,"rb") as f:
        # ftp.storlines("STOR "+tofilename,f)# bu能读取中文
        ftp.storbinary("STOR "+tofilename,f)
# Upper("D:\Samples\美琴.jpg","meiqin.jpg") # 目标文件名字不能是中文编码

# 下载
def Down1(orifilename,tofilename):
    with open(tofilename, "wb") as f: # 下载音乐图片文本等二进制内容
        # ftp.storlines("STOR "+tofilename,f)# bu能读取中文
        ftp.retrbinary("RETR " + orifilename, f.write)

# Down1("run.gif",r"D:\Python_sup\run.gif")


Down2("work1.py",r"D:\Samples\run2.txt")

