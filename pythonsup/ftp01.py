from ftplib import FTP
# print(FTP)

# 建立ftp 连接
ftp=FTP("192.168.12.23")
# print(ftp)
logins=ftp.login("Thomas","123456")
# print(logins)

# 下载以字节流形式
def Down(oriname,filname):
    with open(filname,"w",encoding="utf8") as f:
        result=ftp.retrlines("RETR "+oriname,f.write)
        print(result)
# Down("run.gif",r"D:\测试\1128\a.gif")

def Down2(oriname,filname):
    with open(filname,"wb") as f:
        result=ftp.retrbinary("RETR "+oriname,f.write)
        print(result)
# Down2("11.14.txt",r"D:\测试\1128\a.txt")

def Upper(toname,filname):
    with open(filname,"rb") as f:
        result=ftp.storlines("STOR "+toname,f)
        print(result)
# Upper("work2",r"C:\新建文件夹\wer.doc")

def Upper2(toname,filname):
    with open(filname,"rb") as f:
        result=ftp.storbinary("STOR "+toname,f)
        print(result)
Upper2("生成器.avi",r"D:\Python_sup\20181120\3生成器.avi")

