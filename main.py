#xy좌표 상에서 마음대로 거북이 움직이기
import turtle
import turtle as t
import random

#폭과 높이, 펜 두께, exitCount는 윈도우창 밖으로 빠져나간 횟수를 세는것, angle과 dist는 임의로 이동할 거리와 각도
#curX,Y는 현재 거북이의 위치를 저장하는 변수다
swidth, sheight, pSize, exitCount = 300,300,3,0
r,g,b, angle, dist, curX, curY = [0] * 7

t.shape('turtle')
t.pensize(pSize)
t.setup(width = swidth + 30, height = sheight+30)
t.screensize(swidth,sheight)

while True:
    r=random.random()
    g=random.random()
    b=random.random()
    t.pencolor(r,g,b)
    #임의의 색상 지정하고 각도는 0~360 범위에서, 거리는 1~100 범위에서 임의로 추출한다

    angle = random.randrange(0,360)
    dist = random.randrange(1,100)
    t.left(angle)
    t.forward(dist)
    curX = turtle.xcor()
    curY = turtle.ycor()

    #pass 실행해서 if문을 그냥 종료하고 다시 while 문 수행한다.
    #이범위를 벗어나면 else 부분을 실행한다.
    if(-swidth /2 <= curX and curX <= swidth /2) and (-sheight /2 <= curY and curY <= sheight /2) :
        pass
    else:
        t.penup()
        t.goto(0,0)
        t.pendown()

        #거북이가 5회이상 넘어갈 경우 break 걸기
        exitCount += 1
        if exitCount >= 5 :
            break
t.done()
