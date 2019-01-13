#循环:

#while ：无限循环

#for  ：有限个数的循环

#循环的嵌套：外部循环一次，内部执行所有
#
#for i in range(10):
#	for j in range(10): # 0 9
#		print(j)
#	print("*"*50)


#1. 外层控制 【行数】，内层控制 【列数】
#正三角：（外层索引+1）
#倒三角：（行数-外层索引）


#2、案例2
#        打印九九乘法表

#for  i  in range(1,10): #i：1 ...9
#	for j in range(1,i+1):# j:1 ...9
#		print("%s*%s=%s\t"%(i,j,i*j),end="") #【\t 字符串的制表符】
#	print()

#
#5.编程求出满足以下条件的三位数:
#	它除以11所得的商等于它各位数字之和.

#123//100 
#123//10%10
#for i in range(100,1000): #【穷举法】
#	if i/11==i//100 +i//10%10+i%10:
#		print(i)

#循环嵌套
#for i in range(1,10):# 1... 9
#	for j in range(0,10):# 0 ...9
#		for k in range(0,10): #0 ..9
#			if i+j+k==int(str(i)+str(j)+str(k))/11:
#				print(int(str(i)+str(j)+str(k)))
#




#break：打断 循环
#import random
#while True:
#	print(random.randint(1,4),random.randint(1,7))
#	x=input()
#
#	if x=="q":
#		break #断开循环，后面语句不在执行
#	print("你好%s"%x)


#找出 10000 以内 【7的倍数】 【最大的值】？

#i=10000
#while i>0:
#	if i%7==0:
#		print(i)
#		break #断掉后面的查找
#	i-=1

# 实现 账号登录，admin  ， 888888 ，三次冻结

#i=1
#while True:
#	userName=input("请输入用户名》")
#	userPwd=input("请输入密码》")
#	if userName=="admin" and userPwd=="888888":
#		print("登录成功！")
#		break
#	else:
#		print("登录失败,从新登录，次数：",i)
#		if i==3:
#			print("账户冻结，无法继续登录")
#			break
#
#	i+=1




#continue：结束本次循环  ，进行下次循环


#for i in range(10):
#	if i==5:
#		continue #后面的语句不在执行
#	print(i)

#逢7 过
#x="125"
#print(x.count("7"))

#for i in range(1,101):
#	if i%7==0 or str(i).count("7")!=0:
#		print("过")
#		continue #跳过本次。后面的语句不在执行，下一次循环
#	print(i)



#break/continue 只能出现在循环语句中，不能单独使用，并就近原则找匹配的循环
#for j in range(100):
#	for i in range(100):
#		print(i)
#		break



#示例：
#计算并输出100以内的所有素数(质数)。
#素数：按照素数的定义，除了1和它自身以外，
#不能被其它数整除的数即为（质素)数。

# 2  3   5  7   11  13  17  19  23 .........

#17/(2....16)
#14/(2....13)
#13/(2....12)

#循环嵌套
# 外层 ：i: 【2 ，100】#
# 内层 ：j: 【2，i-1】

 
#for  i in range(2,101):#  13
#	#假定思维：
#	isFind =True #True 假定这个数 是素数
#	for j in range(2,i):#
#		if i%j==0:
##			print(i,"不是素数")
#			isFind=False
#			break # 如果出现一个能除尽，此数一定不是素数
#
#	#此时这里需要约束
#	if isFind:
#		print(i,"是素数")



#注册的账号密码 ： 100  【admin 888 ，admin 123， admin 333】


#admin 123






#循环的重点：


#while  ：无限循环  
#       ：倒序求数据
#

#for  ：有限循环
#       正顺序 range(1,100)

#嵌套：
#打图形： 外层 行，内层列，外层一次 ，内层所有。


#break:   打断循环
#continue ：结束本次，继续下一次
#注意:break/continue 只能用作于循环语句中，匹配自己循环体







#遍历：一个一个输出

#strA="akasdadsfaserafsbsew"

#for i in range(len(strA)):# 0 1 2
#	print(strA[i])

#for i in strA: #【迭代】
#	print(i)
# a=[1,2,3,4]
# a.pop(0)
# print(a)






















