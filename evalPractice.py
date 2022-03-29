#파이썬 eval함수 연습

#eval함수 간단예제
numbers = input("type any numbers you like")
print('you just typed those numbers :', numbers)


#1번을 선택하면 수식계산기, 2번을 선택하면 두 수 사이의 합계 구하기
select, answer, numStr, num1, num2 = 0, 0, "", 0, 0 #변수선언

select = int(input("1번을 누르면 계산기 나오고 2번 누르면 두수 사이의 합계 구하기 나옴, 뭐고를거임?"))

if select == 1: #1번을 눌렀다면?
    numStr = input("아무 수식이나 넣어라 :")

    #매개변수에 string을 넣으면 해당값을 그대로 실행하여 결과 출력
    answer = eval(numStr)
    print("%s 결과는 %5.1f 라고 한다,맞냐?? 너가 계산한거 보단 낫겠지ㅋ : " % (numStr, answer))


elif select == 2: #2번을 눌렀다면??
    num1 = int(input("첫번째 숫자나 입력해라 :"))
    num2 = int(input("두번째 숫자도 입력해라ㅡㅡ :"))
    for i in range(num1,num2+1):
        answer = answer+i
    print("%d + ... + %d 는 %d 라고 한다,그렇다고 한다." % (num1, num2, answer))

#1,2번 외 다른번호를 누를경우???
else:
    print("1또는 2만 입력해라 뭐하냐?")



