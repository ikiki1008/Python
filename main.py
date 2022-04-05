#ㅍㅏ이썬 별 출력하기

#.1
for i in range(5):  #0부터 4까지 반복, 세로방향
    for j in range(5): #0부터 4까지 반복, 가로방향
        if j <= i: #세로방향 변수 i 만큼
            print('*', end='') #별출력, end에 ''를 지정하여 줄바꿈을 하지 않는다
    print() #가로방향으로 별을 다 그린뒤 다음줄로 넘어간다


#.2
for i in range(5):
    for j in range(5):
        if j==i: #세로방향 변수값이 서로 같을 시.
            print('*', end='')
    print()



#.3
for i in range(5):
    for j in range(5):
        if j==i:
            print('*', end='')
        else:  #세로방향 변수값이 다를때는 공백을 출력해서 나오게 하라.
            print(' ', end='')
    print()


#.4
for i in range(5,0,-1): #5개부터 하나씩 줄어들게 하라.
    for j in range(i):
        print('*', end='')
    print('')



#.5
for i in range(1,6):
    for j in range(5-i):
        print(' ', end='')
    for j in range(1,i*2,1): #*2배씩 출력되게 하라.
        print('*', end='')
    print('')



#.6
for i in range(1,6):
    for j in range(5-i):
        print(' ', end='')
    for j in range(1,2*i,1):
        print('*',end='')
    print('')
for i in range(5):
    for j in range(i):
        print(' ',end='')
    for j in range(10,1+i*2,-1):
        print('*', end='')
    print('')