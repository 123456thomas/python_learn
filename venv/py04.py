#正则表达式，导入模块
import re

#1.从开头开始匹配如果匹配成功，返回一个match对象，否则返回None
# str1="relasdfrelgg"
# result1=re.match("rel",str1)
#re.Match类型都可以用group()方法
# print(result1,result1.__class__,result1.group())

#2匹配是否含有"rel",若检查到含有，之后的不再匹配
# str1="rlasdfrelgg"
# result1=re.search("rel",str1)
# print(result1,result1.__class__,result1.group())

# #3.整体匹配,即是否相等,相等返回一个对象，否则返回None
# str1="rlasdfrelgg"
# result1=re.fullmatch("rlasdfrelgg",str1)
# print(result1,result1.__class__,result1.group())
#

# #4.返回一个列表
# str1="r4lasdfrelgr2lg"
# result1=re.findall("rl",str1)
# print(result1,result1.__class__)
# re.findall()

#
# #5. re.split()用字符串用分割含有它的字符串，得到一个列表
# str1="rlasdfrlgrlg"
# result1=re.split("rl",str1)
# print(result1,result1.__class__)
#

## 6.re.sub匹配并替换，默认全替换,flags=2则替换2个，为0，全替换
# re.sub(str1,str2,string1,flags=0)
# str1="rlasdfrlgrlg"
# result1=re.sub("rl","22",str1)
# print(result1,result1.__class__)
#

# #7.将匹配到的内容都放入迭代器，匹配每一个
# re.finditer(str1,string1)
# str1="rlasdfrlgrlg"
# result1=re.finditer("rl",str1)
# print(result1,result1.__class__)


# #8. re.compile得到一个匹配模型，然后用匹配模型去匹配
partch=re.compile("rel")
str1="rlasdfrlgrlg"
result=partch.search("wertyrel")
print(result,result.__class__,result.group())