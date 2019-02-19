#import basic pygame modules
import pygame
from pygame.locals import *
import MaColor
import os.path
import numpy
import math

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
        SCREEN = pygame.display.set_mode((SIZE_X,SIZE_Y),DOUBLEBUF)
        pygame.display.set_caption('By MAMAMA')
        SCREEN.fill(_color)
        pygame.display.update()
        #FONT = pygame.font.Font(None,40)
        FONT = pygame.font.SysFont('C:\Windows\Fonts\simhei.ttf',40)
        self.Height = SIZE_Y
        self.Width = SIZE_X
        self.FontColor = (255,255,255)
        self.BackColor = _color
    def GamePrint(self,text,location_x_y = None,_font = None):
        global SCREEN,FONT
        if location_x_y is None:
            location_x_y = (self.Width/2,self.Height-50)
        if _font is None:
            _font = FONT
        imgText = _font.render(text,True,self.FontColor)
        SCREEN.blit(imgText,location_x_y)
        #pygame.display.update()


mygame = MaGame(400,600,MaColor.black)

def initialize():
    #变量初始化放这里
    global FONT,CLOCK,DIR
    global SCREEN_WIDTH,SCREEN_HEIGHT
    fontsize = 45
    SCREEN_WIDTH = mygame.Width
    SCREEN_HEIGHT = mygame.Height
    DIR = os.path.split(os.path.abspath(__file__))[0]
    FONT = pygame.font.SysFont('C:\Windows\Fonts\simhei.ttf',fontsize)
    CLOCK = pygame.time.Clock()#设置帧率
    #end of initialize

def ClearScreen():
    #清屏
    global SCREEN
    SCREEN.fill(mygame.BackColor)
    #pygame.display.update()
    #end of ClearSCreen

class Point():
    def __init__(self,_x,_y,_z):
        self.x = _x
        self.y = _y
        self.z = _z
    def get_flat_pos(self):
        return (self.x+200,self.y+100)
    def RotY(self,ang):
        _x = self.x
        _y = self.y
        _z = self.z
        self.x = _x * math.cos(ang) + _z * math.sin(ang)
        self.z = _x * (-math.sin(ang)) + _z * math.cos(ang)
    def RotX(self,ang):
        _x = self.x
        _y = self.y
        _z = self.z
        self.y = _y * math.cos(ang) + _z * (-math.sin(ang))
        self.z = _y * math.sin(ang) + _z * math.cos(ang)
    def RotZ(self,ang):
        _x = self.x
        _y = self.y
        _z = self.z
        self.x = _x * math.cos(ang) + _y * (-math.sin(ang))
        self.y = _x * math.sin(ang) + _y * math.cos(ang)


Point1 = Point(0,0,0)
Point2 = Point(100,0,0)
Point3 = Point(100,100,0)
Point4 = Point(0,100,0)

Point5 = Point(100,0,100)
Point6 = Point(100,100,100)

Point7 = Point(0,100,100)
Point8 = Point(0,0,100)

Point1.RotX(math.pi/6)
Point2.RotX(math.pi/6)
Point3.RotX(math.pi/6)
Point4.RotX(math.pi/6)
Point5.RotX(math.pi/6)
Point6.RotX(math.pi/6)
Point7.RotX(math.pi/6)
Point8.RotX(math.pi/6)

def FrameTask():
    #每帧的任务
    global CLOCK,SCREEN
    global role1,testgroup
    global Point1,Point2,Point3,Point4
    Point1.RotY(math.pi / 60)
    Point2.RotY(math.pi / 60)
    Point3.RotY(math.pi / 60)
    Point4.RotY(math.pi / 60)
    Point5.RotY(math.pi / 60)
    Point6.RotY(math.pi / 60)
    Point7.RotY(math.pi / 60)    
    Point8.RotY(math.pi / 60)
    #Frame = 40 fps   
    CLOCK.tick(40)
    if role1.rect.left < 400:
        role1.rect.move_ip(1,0)
    #when you need to clear the screen
    ClearScreen() 
    #testgroup.draw(SCREEN) 
    pygame.draw.lines(SCREEN,MaColor.cyan,True,[Point1.get_flat_pos(),Point2.get_flat_pos(),\
        Point3.get_flat_pos(),Point4.get_flat_pos()],3) 
    pygame.draw.lines(SCREEN,MaColor.cyan,True,[Point2.get_flat_pos(),Point5.get_flat_pos(),\
        Point6.get_flat_pos(),Point3.get_flat_pos()],3) 
    pygame.draw.lines(SCREEN,MaColor.cyan,True,[Point3.get_flat_pos(),Point6.get_flat_pos(),\
        Point7.get_flat_pos(),Point4.get_flat_pos()],3)
    pygame.draw.lines(SCREEN,MaColor.cyan,True,[Point1.get_flat_pos(),Point8.get_flat_pos(),\
        Point7.get_flat_pos(),Point4.get_flat_pos()],3)
    pygame.draw.lines(SCREEN,MaColor.cyan,True,[Point1.get_flat_pos(),Point2.get_flat_pos(),\
        Point5.get_flat_pos(),Point8.get_flat_pos()],3)  
    pygame.draw.lines(SCREEN,MaColor.cyan,True,[Point7.get_flat_pos(),Point8.get_flat_pos(),\
        Point5.get_flat_pos(),Point6.get_flat_pos()],3)
    mygame.FontColor = (255,255,255)
    mygame.GamePrint('Happy Lantern Festival',(30,230))
    font = pygame.font.SysFont('Times New Roman',20,True,True)
    mygame.FontColor = MaColor.powderblue
    mygame.GamePrint('by MAMAMA',(240,265),font)
    #end of FrameTask

#Based on Sprite
class Actor(pygame.sprite.Sprite):
    costumes = []
    def __init__(self,imgpath,position = (0,0)):
        global DIR
        pygame.sprite.Sprite.__init__(self)        
        imgpath = os.path.join(DIR, imgpath)
        print(imgpath)
        #image是用于初始化的，pygame的Sprite必须有一个image对象，用于保存其需要展示的图像
        self.image = pygame.image.load(imgpath).convert_alpha()
        self.images = [self.image]
        #pygame的Sprite必须有一个rect对象，用于设定图像显示的区域
        self.rect = self.image.get_rect()
        #角色尺寸
        self.Width,self.Height = self.image.get_size()
        self.Loc_x = position[0]
        self.Loc_y = position[1]
        self.ImgIndex = 0
    def AppendImage(self,imgpath):
        global DIR
        imgpath = os.path.join(DIR, imgpath)
        surf = pygame.image.load(imgpath).convert_alpha()
        self.images.append(surf)
    #Sprite功能很强大，可以不用去定义Show函数，采用下面的方法实现显示会更便捷：
    #先定义一个Group，<group name> = pygame.sprite.Group()
    #然后将先前声明的Sprite实例加入到这个Group中，<group name>.add(<actor name>)
    #最后用<group name>.draw(screen)方法绘制角色，而绘制角色的大小和位置则取决于rect属性
    '''
    def Show(self,_position = None):
        global SCREEN
        global SCREEN_WIDTH,SCREEN_HEIGHT
        if _position is None:
            _position = self.Loc_x,self.Loc_y
        SCREEN.blit(self.images[self.ImgIndex],_position)
    '''
    def SetScale(self,_scale):
        for i in range(len(self.images)):
            _width = int(_scale*self.Width)
            _height = int(_scale*self.Height)
            self.images[i] = pygame.transform.smoothscale(self.images[i],(_width,_height))
        self.image = self.images[0]

global role1,testgroup

def main():
    global SCREEN
    global role1,testgroup
    initialize() 
    testgroup = pygame.sprite.Group()
    role1 = Actor("s.png") 
    rect1 = pygame.Rect(0,0,100,100)
    role1.image = role1.image.subsurface(rect1)   
    testgroup.add(role1)   
    print(role1.rect)    
    testgroup.draw(SCREEN) 
    #role1.Show()
    while True:          
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