#导入模块
import pygame,sys,os,random,math,time
#初始化设置
pygame.init()
#1.窗口设置
path0=r"flappybird/img/bird0_0.png"
Gender=pygame.image.load(path0)
pygame.display.set_icon(Gender)
pygame.display.set_caption("Happy Flying-bird")
screen=pygame.display.set_mode((400,900))
discolor=pygame.Color(40,150,150,100)
#音乐背景设置
pygame.mixer.music.load("flappybird/Sounds/a12.mp3")
pygame.mixer.music.play(-1)
#全局变量
Sb=0 #开始界面背景刷新

#开始界面
StGrlist=[pygame.transform.scale(pygame.image.load("flappybird/img/bg_night.png"),(410,900)),
        pygame.image.load("flappybird/img/title.png"),
        pygame.transform.scale(pygame.image.load("flappybird/img/button_play.png"),(58,35)),
        pygame.image.load("flappybird/img/bird0_0.png"),
        pygame.image.load("flappybird/img/bird0_1.png"),
        pygame.image.load("flappybird/img/bird0_2.png")
          ]
class StGround:
    def __init__(self,images,screen,speed):
        self.image0=images[0]
        self.image1= images[1]
        self.image2= images[0].copy()
        self.image3= images[2]
        self.image4=images[3]
        self.image5 = images[4]
        self.image6 = images[5]
        self.speed=speed
        self.screen=screen
        self.rect0=self.image0.get_rect()
        self.rect1=self.image1.get_rect().move(111, 200)
        self.rect2=self.image2.get_rect().move(410,0)
        self.rect3 = self.image3.get_rect().move(161, 350)
        self.rect4= self.image4.get_rect().move(161, 280)
    def Display(self):
        global Sb
        Sb += 1
        if Sb%2==0:
            self.rect0.x-=self.speed
            self.rect2.x-= self.speed
        for i in [self.rect0,self.rect2]:
            if i.x<=-410:
                i.x=410
        self.screen.blit(self.image0,self.rect0)
        self.screen.blit(self.image2,self.rect2)
        self.screen.blit(self.image1,self.rect1)
        bntRect=self.screen.blit(self.image3, self.rect3)
        StGround.isRect=bntRect.collidepoint(pygame.mouse.get_pos())
        print(StGround.isRect)
        if Sb%3==0:
            self.screen.blit(self.image6, self.rect4)
        elif Sb%3==1:
            self.screen.blit(self.image4, self.rect4)
        else:
            self.screen.blit(self.image5, self.rect4)
        if Sb==98:
            Sb=0
StBack=StGround(StGrlist,screen,10)


# print(time.localtime())
# t1 = time.time()
# print(t1)
#事件类：
def Allevent():
    for e in pygame.event.get():#遍历所有事件
        if e.type==pygame.QUIT: #是否点击退出
            pygame.quit()
            sys.exit()

def Main():
    # t1 = int(time.time())
    while True:
        screen.fill(discolor)
        Allevent()
        StBack.Display()
        #所有事件
        #开始界面
        # 游戏界面
        #结束界面
        pygame.display.update()
        # t2=int(time.time())
        # if t2==int(time.time())+600:
        #     break

if __name__ == '__main__':
    Main()