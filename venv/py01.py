# 1，使用元方法实现以下功能
def Fun1(classname,parentclass,oriattrdict):
    newattrs={}
    newclassname="new"+classname
    for k,v in oriattrdict.items():
        if not k.startswith("__"):
            key=k+"attr"
            newattrs[key]=v
    return type(newclassname,parentclass,newattrs)

class Benz:
    weight="2t"

class Car(Benz,metaclass=Fun1):
    color="red"
    engin="4T"
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def getname(self):
        print("Hello",self.a)


hose=Car()#创建对象
hose.a=12#赋予对象属性
hose.b=34

#查看类的所有属性
for i in dir(Car):
    if not i.startswith("__"):
        print(i)

print(hose,type(hose),Car.__class__)#查看对象和类的属性
hose.getnameattr()#调用对象方法
print(hose.colorattr)
print(hasattr(hose,"color"),hasattr(hose,"colorattr"))
print(getattr(hose,"colorattr"))#查看对象的属性