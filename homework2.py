import turtle
import random

turtle.title("turtle stamp program")
turtle.shape("turtle")

#왼쪽마우스 클릭하면 도장찍는거
#색깔은 랜덤
def screenLeftClick(x,y):
    global r,g,b
    r = random.random()
    g = random.random()
    b = random.random()

    #크기조정, 1부터 5까지. 앵글은 360도까지
    tSize = random.randrange(1,6)
    tAngle = random.randrange(0,361)


    turtle.shapesize(tSize)
    turtle.color(r,g,b)
    turtle.right(tAngle)
    #turtle stamp
    turtle.stamp()

#거북이 이동함수
def screenRightClick(x,y) :
    turtle.penup()
    turtle.goto(x,y)

#변수 초기값
r,g,b = 0.0,0.0,0.0

turtle.onscreenclick(screenLeftClick,1)
turtle.onscreenclick(screenRightClick,3)

turtle.done()
