# 2，编写代码完成发送普通邮件、图片附件邮件、页面中显示图片邮件
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# 创建实例smtp
smtp=smtplib.SMTP( host='smtp.sina.cn', port=25)

# 创建发送人，接受人帐号
# resv="17625809083m@sina.cn"
sender="17625809083m@sina.cn"
resv="vonneuman@qq.com"
# 登录
smtp.login(sender,"liye361365")

# 编写邮寄内容普通文本
# text="这是最好的世界，也是最坏的世界，新旧世代在这里碰撞，岁月的流逝中，流淌着血与泪，还有那只言片语"
# msg=MIMEText(text,"plain","utf8")



msg = MIMEMultipart()
#wangye
html = """
    <html><head><head/>
        <body>
            <h1>Python 1809 Very Good</h1>
            <h1>Mult</h1>
            <p>这是最好的世界，也是最坏的世界，新旧世代在这里碰撞，岁月的流逝中，流淌着血与泪，还有那只言片语</p>
            <img src="cid:imageid" />
             <h1>御坂美琴</h1>
        </body>
    </html>
"""
msgtxt = MIMEText(html, "html")
# 将html  msg 作为子项目
msg.attach(msgtxt)

# 见图片作为子项目
with open("d:\Samples\meiqin.jpg", "rb") as f:
    msgimg = MIMEImage(f.read())
    msgimg.add_header("Content-ID", "imageid") # 图片作为html子元素
    msg.attach(msgimg)

# 添加文件附件
with open(r"D:\Samples\neutral.pdf","rb") as f:
    mgsgfile=MIMEText(f.read(),"base64", "utf-8")
    mgsgfile["Content-Type"] = 'application/octet-stream'
    mgsgfile["Content-Disposition"] = 'attachment; filename="神经网络.pdf"'
    msg.attach(mgsgfile)


msg["from"]=sender
msg["to"]=resv
msg["subject"]="HeWorld"
# 发送
smtp.sendmail(sender,resv,msg.as_string())
# 退出
smtp.quit()
