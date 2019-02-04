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
global SCREEN_WIDTH
global SCREEN_HEIGHT
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


mygame = MaGame(600,600,MaColor.powderblue)

def initialize():
    #变量初始化放这里
    global FONT,CLOCK,DIR
    global SCREEN_WIDTH,SCREEN_HEIGHT
    global Role1
    fontsize = 40
    SCREEN_WIDTH = mygame.Width
    SCREEN_HEIGHT = mygame.Height
    DIR = os.path.split(os.path.abspath(__file__))[0]
    FONT = pygame.font.Font(None,fontsize)
    CLOCK = pygame.time.Clock()#设置帧率
    Role1 = ImgRole("s2.png")
    Role1.SetScale(0.1)
    #end of initialize

def ClearScreen():
    #清屏
    global SCREEN
    SCREEN.fill(mygame.BackColor)
    #pygame.display.update()
    #end of ClearSCreen
angle = 0
def FrameTask():
    #每帧的任务
    global CLOCK,Role1,role1_x,role1_y,speed,angle
    angle+=1
    #Frame = 40 fps   
    CLOCK.tick(40)
    ClearScreen()    
    #Role1.Show((role1_x,role1_y))
    Role1.Rotate(angle,(100,100))
    #mygame.GamePrint("Happy New Year!",(role1_x-50,role1_y-50))
    if role1_x>500 :
        speed = -speed
    if role1_x<50:
        speed = -speed
    #end of FrameTask

#基于图像的角色，后续扩展基于Sprite的角色
class ImgRole():
    costumes = []
    def __init__(self,imgpath,position = (0,0)):
        global DIR        
        imgpath = os.path.join(DIR, imgpath)
        print(imgpath)
        #costume是用于初始化的，具体使用的时候用costumes list中的图像
        self.costume = pygame.image.load(imgpath).convert_alpha()
        self.costumes = [self.costume]
        #角色尺寸
        self.Width,self.Height = self.costume.get_size()
        self.Center_x = position[0]
        self.Center_y = position[1]
        self.ImgIndex = 0
    def AppendCostume(self,imgpath):
        global DIR
        imgpath = os.path.join(DIR, imgpath)
        surf = pygame.image.load(imgpath).convert_alpha()
        self.costumes.append(surf)
    def Show(self,_position = None):
        global SCREEN
        global SCREEN_WIDTH,SCREEN_HEIGHT
        if _position is None:
            _position = self.Center_x,self.Center_y
        else:
            self.Center_x = _position[0] + self.Width//2
            self.Center_y = _position[1] + self.Height//2
        SCREEN.blit(self.costumes[self.ImgIndex],_position)
        #pygame.display.update()
    def SetScale(self,_scale):
        for i in range(len(self.costumes)):
            _width = int(_scale*self.Width)
            _height = int(_scale*self.Height)
            self.costumes[i] = pygame.transform.smoothscale(self.costumes[i],(_width,_height))
    def Rotate(self,_angle,_position = None):
        global SCREEN
        if _position is None:
            _position = self.Center_x,self.Center_y
        newsurf = pygame.transform.rotate(self.costumes[self.ImgIndex],_angle)
        SCREEN.blit(newsurf,_position)

role1_x = 0
role1_y = 0
speed = 1

def main():
    global SCREEN,Role1,speed,role1_x
    initialize()
    mygame.GamePrint("Hello, World!",(100,100))
    while True:  
        #role1_x+=speed
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