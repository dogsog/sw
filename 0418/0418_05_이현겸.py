''' 작성일: 2024년 4월 18 일
    작성자: 컴퓨터공학부 202495014 이현겸
    설명: 1 ~ 10 까지의 합을 출력하시오.
          합계를 계산하되, 합이 30 이상이면 프로그램을 종료하고
          그 때의 합을 출력하시오.
          
    [문제분석]
        반복의 조건: 10 까지
        선택의 조건: 합이 30 이상이면
        반복하면서 비교. 판단(선택)한다.
        1 부터 10 까지 반복하면서 합계를 계산하다가
        합계가 30 이상이면 계산을 멈춘다.
        30 이상일 때 합계를 출력한다.
        
        break => (자신을 포함하고 있는) 반복을 멈춘다.
        
    [알고리즘]
        1. sum = 0
        2. 1 부터 10 까지 반복하면서
            2-1. 합계를 계산한다.
            2-2. 합계가 30 이상이면
                2-2-1. 반복을 멈춘다.
        3. 합계를 출력한다.
'''
print("== for ==")
sum = 0
for num in range(1, 11):
    sum = sum + num
    if sum >= 30:
        break  # 반복을 멈춘다.
print("sum = ", sum)

print("== while ==")
num = 1
sum = 0
while num <= 10:
    sum = sum + num
    if sum >= 30:
        break  # 반복을 멈춘다.
    num = num + 1
print("sum = ", sum)
