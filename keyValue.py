import operator

trainDic, trainList = [], {}

trainDic = {'thomas':'tommy', 'michael':'mike','juliana':'julie'}
trainList = sorted(trainDic.items(), key=operator.itemgetter(0))

print(trainList)

#-----------------------------------

# 앞부분은 key
foods = {'pasta':'coke',
         'sandwich':'juice',
         'ramen':'sprite',
         'cheese':'wine',
         'grape fruit':'champagne',
         'strawberry cake':'milk'
         };

# 무한반복
while(True):
    myfood = input(str(list(foods.keys())) + "whats your favorite food? if there isn't, just type done to break out!")
    if myfood in foods :
        print("with %s, the best combination is %s." %(myfood, foods.get(myfood)))
    elif myfood == "done" :
        break
    else:
        print("there's no such food like that!")


#-----------------------------------------

data = {
    'c':98,
    'd':90,
    'a':100,
    'e':100
};

# 키 값만 뽑아서 4로 나누기
for value in data.values():
    print((value/4))

# 평균 구하기
sum=0
for i in data.values():
    sum+=i
print(sum/4)








