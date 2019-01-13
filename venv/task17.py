# 1.去掉字符串中的所有空格
# 2.根据完整的路径从路径中分离文件路径、文件名及扩展名
# 3.获取字符串中汉字的个数
# 4.对字符串进行加密与解密
# 5.将字母全部转换为大写或小写
# 6.根据标点符号对字符串进行分行
# 7.去掉字符串数组中每个字符串的空格
# 8.随意输入你心中想到的一个书名，然后输出它的字符串 长度。  （len()属性:可以得字符串的长度）
# 9.两个学员输入各自最喜欢的游戏名称，判断是否一致,如 果相等,则输出你们俩喜欢相同的游戏；如果不相同,则输 出你们俩喜欢不相同的游戏。
# 10.上题中两位同学输入 lol和 LOL代表同一游戏，怎么办?
# 11.让用户输入一个日期格式如“2008/08/08”，将 输入的日 期格式转换为“2008年-8月-8日”。
# 12.接收用户输入的字符串，将其中的字符进行排序（升 序），并以逆序的顺序输 出，“cabed”→"abcde"→“edcba”。
# 13.接收用户输入的一句英文，将其中的单词以反序输 出，“hello c sharp”→“sharp c hello”。
# 14.从请求地址中提取出用户名和域名 http://www.163.com?userName=admin&pwd=123456
# 15.有个字符串数组，存储了10个书名，书名有长有短，现 在将他们统一处理，若书名长度大于10，则截取长度8的 子串并且最后添加“...”，加一个竖线后输出作者的名字。
# 16.让用户输入一句话,找出所有"呵"的位置。
# 17.让用户输入一句话,找出所有"呵呵"的位置。
# 18.让用户输入一句话,判断这句话中有没有邪恶,如果有邪 恶就替换成这种形式然后输出,如:“老牛很邪恶”,输出后变 成”老牛很**”;
# 75/75
# 19.如何判断一个字符串是否为另一个字符串的子串
# 20.如何验证一个字符串中的每一个字符均在另一个字符串 中出现过
# 21.如何随机生成无数字的全字母的字符串
# 22.如何随机生成带数字和字母的字符串
# 23.如何判定一个字符串中既有数字又有字母
# 24.字符串内的字符排序（只按字母序不论大小写）
# 25.字符串的补位操作 1  =》001 2  =》002 10=》010

#任务1
# strA=input("请输入字符串 ")
# x=strA.split(" ")
# x="".join(x)
# print(x)
# 方法2
# x=strA.replace(" ","")
# print(x)

#任务2
# strA=r"C:\Program Files (x86)\Google\Update\GoogleUpdate.exe"
# z=strA.rfind(".")
# kz=strA[z+1:]
# t=strA.rfind("\\")
# file=strA[t+1:z]
# adress=strA[:t]
# print("地址是%s,文件名是%s,扩展名是%s"%(adress,file,kz))
#print("文件名：")
#任务3
# strA=input("请输入字符串 ")
# for i in strA:
#     x=i.encode()
#     j=len(x)
#     if j==3:
#         print(i,end=" ")
#方法：2
# strA=input("请输入字符串 ")
# print(len(strA))
# print("%s的中文个数是:%s"%(strA,(len(strA.encode())-len(strA))/2))


#任务4
# strA=input("请输入字符串 ")
# x=strA.encode()
# print(x)
# y=x.decode()
# print(y)

#任务5
# strA=input("请输入字母字符串 ")
# Dx=strA.upper()
# Xx=strA.lower()
# print(Dx,"\n",Xx)

#任务6
# strA=input("请输入字母字符串 ")
# for i in strA:
#     print(i, end="")
#     if i in ",.;?><，。；‘“”：《》！（）()？’":
#         print("\n")
#方法2：replace
#for i in strA:
#     if i in ",.;?><，。；‘“”：《》！（）()？’":
#         strA.replace(i,"\n")
#print(strA)
#验证码验证
# import random
# str1="0 0 0 0 0 0".split(" ")
# for i in range(5):
#     if 0==random.randint(0,1):
#         str1[i]=chr(random.randint(48,57))
#     else:
#         str1[i]= chr(random.randint(97, 122))
# str1="".join(str1)
# print(str1)
# strA=input("请输入验证码")
# strA=strA.lower()
# print(strA)
# if strA==str1:
#     print("Welcome back")


#任务8
# strA=input("请输入书名 ")
# print("书名长度是%s"%len(strA))


#任务9
# strA=input("学生A请输入游戏名： ")
# strB=input("学生B请输入游戏名： ")
# if strA==strB:
#     print("喜欢相同游戏")
# else:
#     print("喜欢不相同游戏")

#任务10
# strA=input("学生A请输入游戏名： ")
# strB=input("学生B请输入游戏名： ")
# strA=strA.lower()
# strB=strB.lower()
# if strA==strB:
#     print("喜欢相同游戏")
# else:
#     print("喜欢不相同游戏")

#任务11
# strA=input("请输入日期如（2008/08/08）： ")
# x=strA.find("/")
# yue=int(strA[5:7])
# ri=int(strA[8:])
# y=strA[:x]+"年-"+str(yue)+"月-"+str(ri)+"日"
# print(y)
##方法2
# strA=input("请输入日期如（2008/08/08）： ")
# y=strA.split("/")
# print("%s年-%s月-%s日"%(y[0],int(y[1]),int(y[2])))
#任务13
# strA=input("请输入字符串： ")
# x=strA.split(" ")
# x=" ".join(strA.split(" ")[::-1])
# print(x)

#任务14
# strA=r"http://www.163.com?userName=admin&pwd=123456"
# strA=strA.split("?")
# print("域名：%s\n用户名：%s\n密码：%s\n"%(strA[0][strA[0].rfind("/")+1:],strA[1].split("&")[0][strA[1].split("&")[0].rfind("=")+1:],strA[1].split("&")[1][strA[1].split("&")[1].rfind("=")+1:]))
#任务15
# strA=input("请输入书名 ")
# strA=strA.split("，")
# print(strA)
# for i in strA:
#     if len(i[:i.rfind("|")])>8:
#         i=i[:8]+"...|"+i[(i.rfind("|")+1):]
#     print(i)

#任务16
# strA=input("请输入一段字符串： ")
# for i in range(len(strA)):
#     if "呵"==strA[i]:
#         print(i,end=",")

#任务17
# strA=input("请输入一段字符串： ")
# for i in range(len(strA)-1):
#     if "呵"==strA[i] and "呵"==strA[i+1]:
#         print(i,end=",")

#任务18
# strA=input("请输入一段话： ")
# if "邪恶" in strA:
#     strA=strA.replace("邪恶","**")
# print(strA)

#任务19
# strA=input("请输入一段字符串： ")
# strB=input("可能子串？：")
# # if strA.count(strB)!=0:
# if strB in strA:
#     print("%s是%s的子串"%(strB,strA))
# else:
#     print("%s不是%s的子串" % (strB, strA))

#任务20
# strA=input("请输入一段字符串： ")
# strB=input("可能子串：")
# isFind=True
# for i in strB:
#     if i not in strA:
#         isFind=False
#         break
# print(isFind)
# 方法2
# strA=input("请输入一段字符串： ")
# strB=input("可能子串：")
# isFind=True                           #假定为真
# for i in strB:
#     if strA.count(i)==0:
#         isFind=False
#         break
# if isFind==True:
#     print("%s的所有字符都在%s里"%(strB,strA))
# else:
#     print("%s的字符不全在%s里" % (strB, strA))

#任务21
# import random
# x=int(input("全英文字符串的位数："))
# for i in range(x):
#     if 0==random.randint(0,1):
#         print(chr(random.randint(65,90)),end="")
#     else:
#         print(chr(random.randint(97,122)), end="")

#任务22
# import random
# x=int(input("全英文字符串的位数："))
# for i in range(x):
#     if 0==random.randint(0,2):
#         print(chr(random.randint(65,90)),end="")
#     elif 1==random.randint(0,2):
#         print(random.randint(0, 9), end="")
#     else:
#         print(chr(random.randint(97,122)), end="")
#方法2：import random
# x=int(input("字符串的位数："))
# str1=list(range(x))
# print(str1)
# for i in range(x):
#     if 0==random.randint(0,2):
#         str1[i]=chr(random.randint(65,90))
#     elif 1==random.randint(0,2):
#         str1[i]=str(random.randint(0, 9))
#     else:
#         str1[i]=chr(random.randint(97,122))
# str1="".join(str1)
# print(str1)
#方法2：
# import random
# x=int(input("字符串的位数："))
# str1=""
# for i in range(x):
#     if 0==random.randint(0,2):
#         str1+=chr(random.randint(65,90))
#     elif 1==random.randint(0,2):
#         str1+=str(random.randint(0, 9))
#     else:
#         str1+=chr(random.randint(97,122))
# print(str1)
# 任务23
# strA=input("请输入字符串？")
# strA=strA.upper()
# isFind=False
# t=0
# for i in strA:
#     if ord(i) in range(65,91):
#         t=1
#     elif ord(i) in range(48,58):
#         isFind = True
#     if isFind and t==1:
#         print("%s数字和字符都存在"%strA)
#         break
# if isFind==False or t==0:
#     print("%s数字和字符不都存在"%strA)

#任务25
x=int(input("请输入一个数字0-999的数字》"))
print("%03d"%x)



