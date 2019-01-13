from hashlib import md5
from Project.sqltext.mysqlhelp import Helper as he
# row=he(_database='py1809',_password='361365').queryall("select pwd from userdata")


# shaltool=md5()
# #给数据库密码加密
# # for i in range(len(row)):
# #     shaltool.update(row[i][0].encode("utf8"))
# #     result=shaltool.hexdigest()
# #     he(_database='py1809', _password='361365').update("update userdata set pwd=%s where id=%s",(result,i+1))
# # print(he(_database='py1809',_password='361365').queryall("select pwd from userdata"))
#
# user2=he(_database='py1809',_password='361365').queryall("select user from userdata")
# count=3
# while count>0:
#     name=input("用户名：")
#     pwds=input("密码")
#     pwd=he(_database='py1809',_password='361365').queryall("select pwd from userdata where user=%s",(name))[0][0]
#     if pwd is not None:
#         shaltool.update(pwds.encode('utf8'))
#         results=shaltool.hexdigest()
#         print(results,pwd)
#         if results==pwd:
#             print("登录成功")
#             break
#         else:
#             count-=1
#     else:
#         count-=1




#
# pwd=input()
#
# shaltool.update(pwd.encode("utf8"))
#
# rese=shaltool.hexdigest()
#
# print(rese)

