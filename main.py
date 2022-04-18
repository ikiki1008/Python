# list tuple practice
# slice example
# for example when you want to bring 0 to 50, you should slice numbers as [0:4]

# from 0 to 30
a = [0,10,20,30,40,50,60,70]
a[0:4]

# from 10 to 40
a = [0,10,20,30,40,50,60,70]
a[1:5]


# from 20 to 50, add 20 numbers
a = [0,10,20,30,40,50,60,70]
a[2:6:2]
# result = 20,40

# pick up 40 to 60
a = [0,10,20,30,40,50,60,70]
a[4:7]

# pick up numbers from beginning to 50
# let the first place blank, so they could bring numbers from beginning
a = [0,10,20,30,40,50,60,70]
a[:6]
# result = 0,10,20,30,40,50


a = [0,10,20,30,40,50,60,70]
a[5:]
# result = 50,60,70

# sequence object
# if you dont type any numbers in space. they show you the whole numbers in object
a = [0,10,20,30,40,50,60,70]
a[:]
# or a[::]
# result = 0,10,20,30,40,50,60,70


# if you wanna bring numbers from beginning but until specific number, and wanna set rules
a = [0,10,20,30,40,50,60,70]
a[:7:3]
# result = 0,30,60


#특정 숫자부터 증폭시켜서 끝까지 나오게 하고 싶을때, 다른 방법으로는 [4:-1:3] 이 있지만 따옴표를 두번써서 간단히 출력
a = [0,10,20,30,40,50,60,70]
a[4::3]
# result = 40,70

# from beginning to the end, adds 2
a[::2]
# result = 0,20,40,60

a[::-1]
# result = 70,60,50,40,30,20,10,0

# 6부터 거꾸로 2씩 줄여서 표현
a[6:0:-2]
# result = 60,40,20,0















