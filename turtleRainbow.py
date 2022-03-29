#for문으로 복잡한 원 그리기
import turtle
import turtle as t
import random

n = 60
t.shape("turtle")
t.speed(10) #속도 가장 빠른것 0, 빠른것 10, 보통 6, 느린것 3, 가장 느린것 1

for i in range(n):
    t.circle(120)
    t.right(360/n) #360도 원 그리기


#거북이 색색깔 원 그리기
# t.penup()
# t.goto(0,-100) #펜들고 이동하기
# t.pendown()
# t.pencolor("red")
# t.circle(100)
#
# t.penup()
# t.goto(0,-100) #펜들고 이동하기
# t.pendown()
# t.pencolor("blue")
# t.circle(200)
#
# t.penup()
# t.goto(0,-100) #펜들고 이동하기
# t.pendown()
# t.pencolor("green")
# t.circle(300)



