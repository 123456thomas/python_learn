# 1.引入模块
import smtplib
from  email.mime.text import MIMEText


sender="17625809083m@sina.cn"
recver="1304895886@qq.com"
# 2.构造通讯对象(邮箱服务器地址，端口
smtp=smtplib.SMTP("smtp.sina.cn",25)
try:
    # pwd=input("密码：")
    # 3.登陆认证
    smtp.login(sender,"liye361365" )
    #4.构造发送消息
    msg=MIMEText("这是一个好消息,zefh9ahwe98p(Yf89,fwaeru98ur9,weuar89yu9q804","plain","utf8")
    msg["from"]=sender
    msg["to"]=recver
    msg["subject"]="news1"

    # 5.发送
    smtp.sendmail(sender,recver,msg.as_string())
    print("+++")
    # 6.退出
    smtp.quit()
except Exception as e:
    print(e)

