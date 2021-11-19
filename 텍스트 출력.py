import pygame

from pygame import *
from pygame.locals import *
from pygame.rect import *
from vector import Vector
import pyc

init()

t = 0
dt = 0.0004



def draw_point(text, pos):                                                              ##글자 출력하는 함수
    img = font.render(text, True, (255, 0, 100))                                        ##글자 및 글씨 색깔
    draw.circle(screen, pyc.WHITE, pos, 5)
    screen.blit(img, pos)

#######텍스트 출력   잡다한 설정들
SIZE = 1280, 800
C1= (255, 255, 255)                                                                     #흰바탕

screen = display.set_mode(SIZE)

score=1                                                                                 ##게임에서 기록한 점수, 0~4 0이 좋은거 추후 코드 수정
pts = ('잘하셨어요!', '좋은것 같아요!', '조금만 힘내보죠!', '???')
font = font.Font("훈떡볶이R.ttf", 50)
xy=(800, 150)                                                                           ##글씨의 위치값
running = True

######도형만들고 움직이기
x1=150
x2=300
x3=450
y1=650
y2=650
y3=650
rect1 = Rect(x1, y1, 150, 400)       ####스코어 따라서 y값 바뀌게 코드수정해야함
rect2 = Rect(x2, y2, 150, 500)        ####(x, y, 가로, 세로)
rect3 = Rect(x3, y3, 150, 550)

rect4 = Rect(150, 600, 600, 400)
g = -9.81
speed = [0, -1]
speed0 = [0, -1]
speed1 = [0, -1]
while running:
    
    t += dt
    for ev in event.get():
        if ev.type == QUIT:
            running = False
    screen.fill(C1)
    pass
    draw_point(pts[score], xy)                                                          ##점수값 입력받고 함수로 보내서 알맞은 텍스트 출력

    pygame.draw.rect(screen, pyc.GREEN, rect1)                                          ##사각형 그리기
    pygame.draw.rect(screen, pyc.BLUE, rect2)
    pygame.draw.rect(screen, pyc.RED, rect3)
    pygame.draw.rect(screen, pyc.WHITE, rect4)
    rect1.move_ip(speed)                                                                ##속도주기
    rect2.move_ip(speed0)
    rect3.move_ip(speed1)
    if rect1.top < 200:
        speed[1] *= 0
    if rect2.top < 100:
        speed0[1] *= 0
    if rect3.top < 50:
        speed1[1] *= 0
    display.flip()
quit()