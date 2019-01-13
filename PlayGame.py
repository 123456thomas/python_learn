#w,a,s,d控制主角移动，空格控制背景音乐暂停，鼠标滑轮控制音量，左键点击飞机可以用鼠标移动控制飞机，右键切换
#导入pygame模块
import sys,random,pygame,math,os
#pygame初始化
pygame.init()
#时间对象
clock=pygame.time.Clock()
#设置游戏窗口 【屏幕大小，图标，标题】
screen=pygame.display.set_mode((480,640))
pw=pygame.image.load(r"Plane/image/plane.png")
pygame.display.set_icon(pw)
pygame.display.set_caption("Masse")

#设置背景颜色
discolor=pygame.Color(40,120,160,164)
#开始界面图片【背景，底部动画】
StaimgList=[pygame.image.load(r"Plane/image/background.png"),
            pygame.transform.scale(pygame.image.load(r"Plane/image/timg.jpg"),(80,100)),
            pygame.transform.scale(pygame.image.load(r"Plane/image/loading.png"),(480,480)),
            pygame.image.load(r"Plane/image/name.png")]
StaBotimg=[pygame.image.load(r"Plane/image/game_loading1.png"),
            pygame.image.load(r"Plane/image/game_loading2.png"),
            pygame.image.load(r"Plane/image/game_loading3.png")]
#英雄素材图片
Herolist=[pygame.transform.scale(pygame.image.load(r"Plane/image/hero1.png"),(100,122)),
          pygame.image.load(r"Plane/image/hero2.png")]
HeroDie=[pygame.image.load(r"Plane/image/hero_blowup_n1.png"),
          pygame.image.load(r"Plane/image/hero_blowup_n2.png"),
          pygame.image.load(r"Plane/image/hero_blowup_n3.png"),
          pygame.image.load(r"Plane/image/hero_blowup_n4.png")]
#敌机素材图片
Enemylist=[[pygame.image.load(r"Plane/image/enemy0.png"),
           pygame.image.load(r"Plane/image/enemy0_down1.png"),
           pygame.image.load(r"Plane/image/enemy0_down2.png"),
            pygame.image.load(r"Plane/image/enemy0_down3.png"),
            pygame.image.load(r"Plane/image/enemy0_down4.png")],
           [pygame.image.load(r"Plane/image/enemy1.png"),
            pygame.image.load(r"Plane/image/enemy1_hit.png"),
            pygame.image.load(r"Plane/image/enemy1_down1.png"),
            pygame.image.load(r"Plane/image/enemy1_down2.png"),
            pygame.image.load(r"Plane/image/enemy1_down3.png"),
            pygame.image.load(r"Plane/image/enemy1_down4.png")],
           [pygame.image.load(r"Plane/image/enemy2.png"),
            pygame.image.load(r"Plane/image/enemy2_n2.png"),
            pygame.image.load(r"Plane/image/enemy2_hit.png"),
            pygame.image.load(r"Plane/image/enemy2_down1.png"),
            pygame.image.load(r"Plane/image/enemy2_down2.png"),
            pygame.image.load(r"Plane/image/enemy2_down3.png"),
            pygame.image.load(r"Plane/image/enemy2_down4.png"),
            pygame.image.load(r"Plane/image/enemy2_down5.png"),
            pygame.image.load(r"Plane/image/enemy2_down6.png")]
           ]
#子弹素材图片
Bullets=[pygame.image.load(r"Plane/image/bullet.png"),
            pygame.image.load(r"Plane/image/bullet1.png"),
            pygame.image.load(r"Plane/image/bullet2.png")]
#奖励素材图片
Jianglist=[pygame.image.load(r"Plane/image/prop_type_0.png"),
           pygame.image.load(r"Plane/image/prop_type_1.png")]
Bulletslist=[]     #子弹对象库
Enelist=[]         #敌机对象库
JingList=[]        #奖励对象库
#开始音乐设置【循环播放】
pygame.mixer.music.load(r"Plane/sound/game_music.mp3")
pygame.mixer.music.play(-1)
#开始界面类
class StartPlane:
    def __init__(self,staimalist,strabotimg,screen):
        self.staimlist=staimalist    #背景图片
        self.strabotimg=strabotimg   #下面的飞机动画列表
        self.screen=screen
        self.s=0                     #控制飞机上下bodong
        self.bom=0                   # 控制底层动画的参数
    def Display(self): #开始界面类的渲染
        self.screen.blit(self.staimlist[0],(0,0))
        btnRect =self.screen.blit(self.staimlist[1],(200,300))         #按钮渲染
        self.screen.blit(self.staimlist[2],(0,80))
        StartPlane.isInRect=btnRect.collidepoint(pygame.mouse.get_pos())#判断鼠标是否在btnRec区域
        #文字波动渲染
        self.screen.blit(self.staimlist[3],(40,50+50*math.sin(self.s*0.5)))
        #底层动画渲染，每8帧换一张图片
        self.screen.blit(self.strabotimg[self.bom//8],(180, 500))
        self.bom+=1
        self.s+=1
        if self.bom==24:
            self.bom=0
        if self.s==100:
            self.s=0

#全局变量
HisScore=0         #历史分
Strong1=False     #子弹奖励布尔参数
Strong2=False     #全暴奖励布尔参数
MouseInpoint=False#判断鼠标是否在飞机上
MouseMove=False   #游戏开始时鼠标是否在飞机上

# 文字对象设置文字大小
font=pygame.font.Font(r"Plane/font/zhongwen.ttf",28)
#游戏音效【发射子弹，按钮，捡起奖励，敌机爆炸，全屏爆炸，游戏结束】
SoundList=[pygame.mixer.Sound(r"Plane/sound/bullet.wav"),
           pygame.mixer.Sound(r"Plane/sound/button.ogg"),
            pygame.mixer.Sound(r"Plane/sound/get_bomb.ogg"),
           pygame.mixer.Sound(r"Plane/sound/enemy0_down.wav"),
           pygame.mixer.Sound(r"Plane/sound/use_bomb.ogg"),
           pygame.mixer.Sound(r"Plane/sound/game_over.ogg")]

#游戏界面
#游戏背景类
class GameBaground:
    def __init__(self,image,screen,speed):
        self.image__1=image                 #背景平面的传入
        self.image__2=image.copy()
        self.screen=screen
        self.speed=speed
        self.rect1=self.image__1.get_rect() #获取背景平面的区域
        self.rect2=self.image__2.get_rect().move(0,-852)  #让两个背景平面的区域衔接起来
    def Display(self):                     #屏幕的渲染
        #图片移动速度
        self.rect1=self.rect1.move(0,self.speed)
        self.rect2=self.rect2.move(0,self.speed)
        # 实现图片的衔接
        if self.rect1.y>860:
            self.rect1.y=self.rect2.y-852
        if self.rect2.y>860:
            self.rect2.y=self.rect1.y-852
        #背景渲染
        self.screen.blit(self.image__1, self.rect1)
        self.screen.blit(self.image__2, self.rect2)
Gabagro=GameBaground(StaimgList[0],screen,2)          #创建游戏背景
# 奖励类【碰撞对象继承精灵类】
class Jingli(pygame.sprite.Sprite):
    def __init__(self,jianglist,screen,speed):
        randum=random.randint(1,100)#确定奖励种类
        if randum<=80:
            self.tag=0
            pos=(random.randint(0,422),-88)
            self.speed=speed
        elif randum>80:
            self.tag=1
            pos=(random.randint(0, 420),-122)
            self.speed=speed
        self.image=jianglist[self.tag]   #平面
        self.rect =self.image.get_rect() # 矩形区域
        self.rect.topleft=pos            #初始化位置
        self.screen=screen
        JingList.append(self)            # 添加到奖品列表
    def JimMove(self):
        self.rect.y += self.speed        #奖品下落速度
        self.screen.blit(self.image, self.rect)
        if self.rect.y > 640:            #限制奖励出现区域，过界销毁
            if self in Enelist:
                JingList.remove(self)
#敌机类
class Enemys(pygame.sprite.Sprite):
    def __init__(self,employs,screen,speed,hp):
        randum=random.randint(1,100)          #随机确定敌机标签
        if randum<=60:
            self.tag=0
            pos=(random.randint(0,429),-40)   #随机敌机的初始化位置
            self.speed=speed+4
            self.hp=hp
        elif randum<=90:
            self.tag=1
            pos=(random.randint(0,411),-90)
            self.speed=speed+3
            self.hp=hp+1
        else:
            self.tag=2
            pos=(random.randint(0,315),-246)
            self.speed =speed+1
            self.hp=hp+2
        self.index=1                          #敌机图片索引
        self.numej=0                          #敌机死亡动画速度参数
        self.image=employs[self.tag][0]       #敌机图片
        self.images=employs[self.tag]         #图片列表
        self.rect=self.image.get_rect()       #矩形区域
        self.rect.topleft=pos                 #传入初始化位置
        self.screen=screen                    #屏幕
        Enelist.append(self)                  #添加到敌机列表
    def Move(self):#移动方法【敌机血量为0时，播放死亡音乐和死亡动画】
        if self.hp>0:
            self.rect.y+=self.speed
            self.screen.blit(self.image,self.rect)
            if self.rect.y>640:               #限制敌机区域，超出则消除
                if self in Enelist:
                    Enelist.remove(self)
        else:
            SoundList[3].play()
            self.Death()
    def Death(self):#死亡方法【播放完动画前可继续移动，结束后对象从敌机列表消除，主角加分】
        self.rect.y+=self.speed
        self.screen.blit(self.images[self.index], self.rect)
        if self.numej==2:
            self.index+=1
            if len(self.images)==self.index:
                if self.tag==0:              #死亡加分
                    HeroMasse.score+=1
                elif self.tag==1:
                    HeroMasse.score+=3
                else:
                    HeroMasse.score+=5
                Enelist.remove(self)
            self.numej=0
        self.numej+=1
# 敌机工厂
class EnemyFactory:
    crearidex=0
    @staticmethod
    def CreatEnemy(screen):          #需要一个形参，传送屏幕
        if EnemyFactory.crearidex==20:  #每20帧产生一个敌机
            Enemyjj=Enemys(Enemylist, screen,3,2)
            EnemyFactory.crearidex=0
        for i in Enelist:            #敌机移动
            i.Move()
        EnemyFactory.crearidex+=1
# 奖励对象工厂
class JiangFactory:
    crearidex=0
    @staticmethod
    def CreatJiang(screen):           #需要一个形参，传屏幕
        if JiangFactory.crearidex==100:#每100帧产生一个奖品
            JingM=Jingli(Jianglist, screen, 6)
            JiangFactory.crearidex=0
        for i in JingList:
            i.JimMove()
        JiangFactory.crearidex+=1
#子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self,bullist,screen,speed,pos):
        self.image=bullist                        #图片平面列表
        self.screen=screen                        #导入屏幕
        self.rect=self.image.get_rect()           #矩形区域
        self.speed=speed                          #子弹速度
        self.rect.center=pos                      #子弹初始化位置
        Bulletslist.append(self)
    def BuMove(self):#【子弹移动方法】
        self.rect.y-=self.speed
        self.screen.blit(self.image,self.rect)    #子弹渲染
        if self.rect.y<-10:                       #超过画面子弹销毁
            if self in Bulletslist:
                Bulletslist.remove(self)
        #移动时检测子弹碰撞
        self.Collide()
    def Collide(self):#【碰撞检测方法】
        temp=pygame.sprite.spritecollideany(self,Enelist,pygame.sprite.collide_mask)
        if temp!=None:
            # 如果是敌机，减血
            if temp in Enelist: #temp为碰撞的敌机
                temp.hp-=1
                if self in Bulletslist:
                    Bulletslist.remove(self)

class HeroMasse(pygame.sprite.Sprite):
    y=0
    score=0#全局分数
    def __init__(self,herolist,herodie,screen,speed,hp,pos=(100,200)):
        self.image=herolist[0]
        self.heroimag=herolist  #主角喷气动画列表
        self.herodie=herodie    #主角死亡列表
        self.hp=hp
        self.screen=screen
        self.speed=speed        #按键灵敏度
        self.rect=self.image.get_rect()
        self.rect.topleft=pos
        self.Canclollide=True   #是否主角敌机发生碰撞
        self.Collidetime=0      #主角碰撞后，无敌时间因子
        self.dienum=0           #死亡图片索引
        self.dieindex=0         #确定主角死亡画面播放快慢的参数
        self.strongindex=0      #确定奖励子弹时间长短的参数
    def CtroMove(self):#主角移动
        global isPlay,HisScore,Strong1
        if self.hp>0:
            if MouseMove:
                self.rect.center=pygame.mouse.get_pos()
            else:
                if x==1:
                    self.rect.y-=self.speed
                elif x==2:
                    self.rect.y+=self.speed
                elif x==3:
                    self.rect.x-=self.speed
                elif x==4:
                    self.rect.x+=self.speed
            # 主角区间约束
            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > 380:
                self.rect.x = 380
            elif self.rect.y<0:
                self.rect.y=0
            elif self.rect.y> 518:
                self.rect.y= 518
            #发射子弹
            if (HeroMasse.y+1)%3==0:#每3帧产生一个子弹
                Bullet(Bullets[0],screen,30,self.rect.midtop)
                if Strong1:#奖励子弹发射，并播放子弹音乐
                    SoundList[0].play()
                    self.strongindex+=1
                    Bullet(Bullets[1], screen,30, (self.rect.midtop[0]+40, self.rect.midtop[1]+30))
                    Bullet(Bullets[2], screen,30, (self.rect.midtop[0]-40, self.rect.midtop[1]+30))
                    if self.strongindex==50:
                        Strong1=False
            # 奖品碰撞检测
            self.JCollide()
            for i in Bulletslist:#子弹移动
                i.BuMove()
            #主角动画刷新
            if HeroMasse.y==6:
                HeroMasse.y=0

            #碰撞后，有3秒安全时间（无敌）
            if self.Canclollide:#没有与敌机碰撞
                self.screen.blit(self.heroimag[HeroMasse.y //3% 2], self.rect)  #飞机喷气效果渲染
                self.HeroCollide()
                HeroMasse.y+=1
            else:#发生碰撞后，在安全时间内不再检测碰撞
                self.Collidetime+=1
                #发生碰撞，则主角发生偏移并闪烁
                if self.Collidetime%3==0:#每3帧闪一次
                    self.rect.x+=3
                    self.screen.blit(self.heroimag[HeroMasse.y //3% 2], self.rect)
                    HeroMasse.y += 1
                    self.rect.x-=3
                    self.screen.blit(self.heroimag[HeroMasse.y //3% 2], self.rect)
                    HeroMasse.y+= 1
                if self.Collidetime==120:
                    self.Canclollide=True
                    self.Collidetime=0
        else:#主角血量为0，执行死亡音乐和方法
            SoundList[5].play()
            self.Herdie()

    def JCollide(self):#主角奖励碰撞检测方法
        global Strong1
        temp = pygame.sprite.spritecollideany(self, JingList, pygame.sprite.collide_mask)
        if temp != None:
            # 如果是，奖品消失，主角发动特技
            SoundList[2].play()   #播放捡到奖励音乐
            if temp in JingList:  # temp为碰撞的奖励
                if temp.tag==0:   #捡到子弹
                    self.strongindex=0  #每捡到奖励，将奖励时间重置
                    Strong1=True
                else:
                    SoundList[4].play()
                    for enmy in Enelist:#敌机全爆
                        enmy.hp=0
                JingList.remove(temp)    #捡到后，奖励清除

    def HeroCollide(self):#主角碰撞检测敌机
        temp=pygame.sprite.spritecollideany(self,Enelist, pygame.sprite.collide_mask)
        if temp != None:
            self.hp-=1
            temp.hp=0
            self.Canclollide=False

    def Herdie(self):#主角死亡方法
        global isPlay
        self.screen.blit(self.herodie[self.dienum], self.rect)
        self.dieindex+=1
        if self.dieindex==7:#每7帧换一个图片
            self.dienum+=1
            self.dieindex=0
            if self.dienum==len(self.herodie):
                self.dienum=0
                if HeroMasse.score>HisScore:#超过最高分，重新更新记录
                    with open("hisScore.txt","w") as f_w:
                        f_w.write(str(HeroMasse.score))

                pygame.time.delay(100)
                isPlay=False
isPlay=False  #是否游戏开始
Pause=False   #控制音乐暂停
m=0           #为音量控制参数
x=0           #为主角移动参数
Staobj=StartPlane(StaimgList,StaBotimg,screen)
Hero=HeroMasse(Herolist,HeroDie,screen,20,3)

def AllEvent():#所有事件
    global isPlay,Pause,m,x,HisScore,MouseMove,MouseInpoint
    for e in pygame.event.get():#遍历所有事件
        if e.type==pygame.QUIT: #是否点击退出
            pygame.quit()
            sys.exit()
        #鼠标事件
        if e.type==pygame.MOUSEBUTTONDOWN:
            m=e.button
            if (StartPlane.isInRect and e.button==1 and isPlay==False):#鼠标在按键区域，并在游戏没开始时按下左键
                SoundList[1].play()
                #读取历史分数
                if os.path.exists("hisScore.txt"):
                    with open("hisScore.txt","r") as f_r:
                        HisScore=int(f_r.read())
                else:
                    with open("hisScore.txt","w") as f_w:
                        f_w.write("0")
                isPlay =True
            MouseInpoint=Hero.rect.collidepoint(pygame.mouse.get_pos())  # 判断鼠标是否在飞机上
            if (MouseInpoint==1 and m==1 and isPlay):
                MouseMove=True
            if MouseMove and m==3:#右键切换
                MouseMove=False

        #键盘事件
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_ESCAPE:#是否按下键盘ESC键
                isPlay=False
            elif e.key==pygame.K_SPACE:#空格控制音乐暂停
                Pause=not Pause
            elif e.key==pygame.K_w:
                x=1                     #主角向上移动
            elif e.key==pygame.K_s:
                x = 2                   #主角向下移动
            elif e.key==pygame.K_a:
                x = 3                   #主角向左移动
            elif e.key==pygame.K_d:
                x =4
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                x = 0  # 主角向上移动
            elif e.key == pygame.K_s:
                x = 0  # 主角向下移动
            elif e.key == pygame.K_a:
                x = 0  # 主角向左移动
            elif e.key == pygame.K_d:
                x = 0
def Main():
    global Strong1,MouseMove
    while True:#循环执行
        AllEvent()#判断事件
        screen.fill(discolor)#窗口背景填充
        if Pause:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        if m==4:
            z=pygame.mixer.music.get_volume()
            z+=0.1
            pygame.mixer.music.set_volume(z)
        elif m==5:
            z = pygame.mixer.music.get_volume()
            z-= 0.1
            pygame.mixer.music.set_volume(z)
        else:
            pass

        if isPlay:
            Gabagro.Display()              #游戏背景
            EnemyFactory.CreatEnemy(screen)#制造敌机
            JiangFactory.CreatJiang(screen)#制造奖品
            Hero.CtroMove()                #主角移动控制
            screen.blit(font.render("血量:%s"%Hero.hp,True,pygame.Color("Red")),(0,0))
            screen.blit(font.render("分数:%s"%HeroMasse.score, True, pygame.Color("Black")),(0,32))
            screen.blit(font.render("最高分:%s"%HisScore, True, pygame.Color("Black")),(0,64))
        else:
            # 主角死亡，初始化对象初始化对象【血量，分数】
            Hero.hp =3
            HeroMasse.score= 0
            Hero.rect.topleft=(100,200)
            Bulletslist.clear()
            Enelist.clear()
            JingList.clear()
            HeroMasse.y = 0
            Strong1 = False
            MouseMove=False
            Hero.Herdie()
            Staobj.Display()
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    Main()