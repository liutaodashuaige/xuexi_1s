import pygame
import sys

#初始化
pygame.init()
size=width,height=800,600
speed=[-2,1]
#bj=pygame.image.load("wallpaper_201701(1600x1200).jpg")
#clock=pygame.display.time.Clock()

#创建窗口
ck=pygame.display.set_mode(size)
#窗口标题
pygame.display.set_caption("流浪印传")

#加载图片
tp=pygame.image.load("yc.jpg")
#获取图片位置矩形
jx=tp.get_rect()

#主循环
while 1:
    #监测退出事件
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    #移动图像
    jx=jx.move(speed)
    #边界检测
    if jx.left<0 or jx.right>width:
        #水平翻转图像
        tp=pygame.transform.flip(tp,True,False)
        #改变速度方向
        speed[0]=-speed[0]
    if jx.top<0 or jx.height:
        speed[1]=-speed[1]
    #背景填充
    #ck.fill(bj)
    #刷新图像
    ck.blit(tp,jx)
    #刷新界面
    pygame.display.flip()
    #帧数控制
    pygame.time.delay(10)
    #clock.tick(200)