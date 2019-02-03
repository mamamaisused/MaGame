#import basic pygame modules
import pygame
from pygame.locals import *
import MaColor

global SCREEN
global FONT
global CLOCK
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
        pygame.display.update()


mygame = MaGame(800,600,MaColor.pink)

def initialize():
    #变量初始化放这里
    global FONT,CLOCK
    fontsize = 40
    FONT = pygame.font.Font(None,fontsize)
    CLOCK = pygame.time.Clock()#设置帧率
    pass
    #end of initialize

def ClearScreen():
    #清屏
    global SCREEN
    SCREEN.fill(mygame.BackColor)
    pygame.display.update()

def FrameTask():
    #每帧的任务
    global CLOCK
    #Frame = 40 fps
    CLOCK.tick(40)   

def main():
    global SCREEN
    initialize()
    mygame.GamePrint("Hello, World!",(100,100))
    while True:
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