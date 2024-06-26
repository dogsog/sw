''' 작성일: 2024년 4월 18 일
    작성자: 컴퓨터공학부 202495014 이현겸
    설명: 정수를 입력받아 그 수가 소수인지 아닌지 판별하시오.
    
    [문제분석]
        소수는 1과 자기자신으로 나누어 떨어지는 수
                              (나누어 나머지가 0인 수)
                              
        1을 제외하고 2부터 자기자신까지 나누어
        나머지가 0인 것을 확인하자.
        
        반복 조건 : 자기자신까지(입력 수 까지)
        선택 조건 : 나누어 나머지가 0 이면
        
    [알고리즘]
        0. count = 0
        1. 정수를 입력받는다.
        2. 2부터 입력받은 수까지 반복하면서
            2-1. 입력수를 2부터 나누어 나머지가 0이면
                2-1-1. 개수를 증가시킨다.
        # 반복이 끝나면 개수를 확인한다.
        3. 개수가 1이면 (자신으로만 나누어 떨어지니 개수는 1이다.)
            3-1. 00은 소수이다.
        4. 아니면
            4-1. 00은 소수가 아니다.
'''
count = 0
num = int(input("소수인지 판단할 정수를 입력하세요. : "))

for i in range(2, num+1) :
    if num % i == 0 :
        count = count + 1
        
if count == 1:
    print(f"{num}은 소수입니다.")
else :
    print(f"{num}은 소수가 아닙니다.")