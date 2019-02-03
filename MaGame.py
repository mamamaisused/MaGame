#import basic pygame modules
import pygame
from pygame.locals import *
import MaColor
import os.path

global SCREEN
global FONT
global CLOCK
global Role1
global DIR
class MaGame():
    def __init__(self,SIZE_X = 800,SIZE_Y = 600,_color = (255,255,255)):
        global SCREEN,FONT
        pygame.init()
        SCREEN = pygame.display.set_mode((SIZE_X,SIZE_Y))
        SCREEN.fill(_color)
        pygame.display.update()
        FONT = pygame.font.Font(None,40)
        self.Height = SIZE_Y
        self.Width = SIZE_X
        self.FontColor = MaColor.black
        self.BackColor = _color
    def GamePrint(self,text,location_x_y = None,_font = None):
        global SCREEN,FONT
        if location_x_y is None:
            location_x_y = (self.Width/2,self.Height-50)
        if _font is None:
            _font = FONT
        imgText = FONT.render(text,True,self.FontColor)
        SCREEN.blit(imgText,location_x_y)
        #pygame.display.update()


mygame = MaGame(800,600,MaColor.pink)

def initialize():
    #变量初始化放这里
    global FONT,CLOCK,Role1,DIR
    fontsize = 40
    DIR = os.path.split(os.path.abspath(__file__))[0]
    FONT = pygame.font.Font(None,fontsize)
    CLOCK = pygame.time.Clock()#设置帧率
    Role1 = ImgRole("s.png")
    Role1.SetScale(0.5)
    pass
    #end of initialize

def ClearScreen():
    #清屏
    global SCREEN
    SCREEN.fill(mygame.BackColor)
    #pygame.display.update()
    #end of ClearSCreen

def FrameTask():
    #每帧的任务
    global CLOCK,Role1,role1_x,role1_y,speed
    #Frame = 40 fps   
    CLOCK.tick(60)
    ClearScreen()    
    Role1.Show((role1_x,role1_y))
    mygame.GamePrint("Happy New Year!",(role1_x-50,role1_y-50))
    if role1_x>500 :
        speed = -speed
    if role1_x<50:
        speed = -speed
    #end of FrameTask

#基于图像的角色，后续扩展继续Sprite的角色
class ImgRole():
    costumes = []
    def __init__(self,imgpath):
        global DIR
        imgpath = os.path.join(DIR, imgpath)
        print(imgpath)
        self.costume = pygame.image.load(imgpath).convert_alpha()
        self.costumes = [self.costume]
        #角色尺寸
        self.Width,self.Height = self.costume.get_size()
    def AppendCostume(self,imgpath):
        global DIR
        imgpath = os.path.join(DIR, imgpath)
        surf = pygame.image.load(imgpath).convert_alpha()
        self.costumes.append(surf)
    def Show(self,_position,index = 0):
        global SCREEN
        SCREEN.blit(self.costumes[index],_position)
        #pygame.display.update()
    def SetScale(self,_scale):
        for i in range(len(self.costumes)):
            _width = int(_scale*self.Width)
            _height = int(_scale*self.Height)
            self.costumes[i] = pygame.transform.smoothscale(self.costumes[i],(_width,_height))

role1_x = 100
role1_y = 300
speed = 1

def main():
    global SCREEN,Role1,speed,role1_x
    initialize()
    mygame.GamePrint("Hello, World!",(100,100))
    while True:  
        role1_x+=speed
        pygame.display.update()      
        FrameTask()
        for event in pygame.event.get():
            #事件捕捉          
            if event.type == QUIT:
                return
            if event.type == MOUSEMOTION:
                #鼠标移动事件
                pass
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                #按键处理程序
                if event.key == 13:
                    #回车键
                    print("Enter!")
                

    #end of main



if __name__ == '__main__': main()