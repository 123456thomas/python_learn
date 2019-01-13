# 5，使用type创建对象Goods拥有id，name，getinfo（方法）三个属性
# 使用type创建Goods的子类对象Food 拥有type，getinfo（方法），getname（方法）
# 实例化对象g1，f1 查看父子类方法的相互调用
@classmethod
def Fun1(cls):
    """"eetgrrrs"""
    return cls.__name__#返回对象类型

def Fun2(self,a,b):#对象的初始化
    self.a=a
    self.b=b

def Fun3(self):
    if self.a>self.b:
        print("++++")
    else:
        print("----")
Good=type("Goods",(),{"id":123,"name":"zza","getinfo":Fun1})

Fod=type("Food",(Good,),{"type":"Food","getname":Fun2,"fu":Fun3})
#实例化对象
go1=Good()
fo1=Fod()

#方法调用
 #类的属性
print(fo1.id,go1.id)
go1.getinfo()
fo1.getinfo()#子类对象可以调用父类的属性和方法
print(go1.getinfo(),type(go1))

# print(fo1.type)
# go1.getname(2,6)
fo1.getname(2,6)#父类类对象不能调用子类的属性和对象方法



#对象属性
print(fo1.a)   #对象属性的调用

fo2=Fod()
fo2.getname(21,67)#给对象属性
print(fo2.a)
#调用对象方法
fo2.fu()
