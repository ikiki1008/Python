import turtle
import turtle as t
import random

# col = ['red', 'green', 'yellow', 'blue', 'pink', 'orange']
# print(col)
# print(col[0], col[4], col[2])
# print('length =', len(col))
# print(type(col))
#
r = 0.0 #필요한 변수 준비
g =0.0
b = 0.0
#
# def screenLeftClick(x,y) :
#     global r,g,b
#     turtle.pencolor((r,g,b))
#     turtle.pendown()
#     turtle.goto(x,y)


t.setup() #turtle screen setup
t.shape('turtle')
t.speed(100)
t.pensize(20)
t.color('blue')
t.circle(100)

t.up()
t.goto(100,-100) #xy좌표로 거북이를 옮긴다
t.down()
t.color('yellow')
t.circle(100)

t.up()
t.goto(200,0)
t.down()
t.color('black')
t.circle(100)

t.up()
t.goto(300,-100)
t.down()
t.color('green')
t.circle(100)

t.up()
t.goto(400,0)
t.down()
t.color('red')
t.circle(100)


t.done()


#클릭하면 랜덤하게 바뀌는 거북이

def screenLeftCLick(x,y) :
    tSize  = random.randrange(2,10)
    turtle.Shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color((r,g,b))
    tAngle = random.randrange(0,300)

    turtle.penup()
    turtle.goto(x,y)
    turtle.left(tAngle)

