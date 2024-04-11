''' 작성일: 2024년 4월 5 일
    작성자: 컴퓨터공학부 202495014 이현겸
    설명: 반복문 while 
'''
#1~10까지 출력하기

num1 = 1 #초기값. 1 부터

while num1 <= 10 : #조건식. 10 까지
    print(num1, end = ', ') #반복하면서 할 일
    num1 = num1 + 1 #증감식. 1씩 증가하면서
    #증감식은 반복문의 제일 마지막에 작성

print() #한 줄 바꿈
print("====반복문 while로 1부터 10까지 출력하기====")

num1 = 1 #초기값
num2 = 10 #종료 값

while num1 <= num2 :
    print(num1, end = ', ') #반복하면서 할 일
    num1 = num1 + 1 #증감식. 1씩 증가하면서

print() #한 줄 바꿈
print("=== 반복문으로 자기 이름 출력하기 ===")

num1 = 1

while num1 <= 10 :
    print("이현겸", end = ' ')
    num1 = num1 + 1
    
i = 1

while i <= 10 :
    print(i, end = '. ')
    print("이현겸")
    i = i + 1