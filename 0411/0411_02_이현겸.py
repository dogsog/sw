''' 작성일: 2024년 4월 5 일
    작성자: 컴퓨터공학부 202495014 이현겸
    설명: 1~10까지의 합을 구하는 프로그램
    
    [문제분석]
        1 + 2 + 3 ... + 10 = 55
        합계 = 합계 + 숫자(다음 수)
        sum = sum + num
        num은 1부터 10까지 1씩 증가
        sum = 0 (변수 초기화)
    [알고리즘]
        0. sum = 0 으로 초기화한다.
        1. num = 1
        2. num <= 10 까지 반복한다.
            2-1. 합계 계산한다. sum = sum + num
            2-2. num은 1씩 증가한다. 없으면 무한반복된다.
        3. 합계 출력한다.
'''
sum = 0
num = 1

while num <= 10 :
    sum = sum + num
    num = num + 1

print(f"1부터 10까지의 합 : {sum}")