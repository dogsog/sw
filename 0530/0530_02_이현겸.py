''' 작성일: 2024년 5월 30 일
    작성자: 컴퓨터공학부 202495014 이현겸
    설명: 정수를 입력받아 팩토리얼을 출력하시오.
          팩토리얼 계산하는 부분은 함수로 작성하고 결과는 돌려줍니다.
    
    [문제분석]
        n! = n * (n - 1) * (n - 2) ... * 1
        5! = 5 * 4 * 3 * 2 * 1
        3! = 3 * 2 * 1
        입력받은 수부터 1씩 감소한다.
        곱한다.
        fac = fac * num
    
    [알고리즘]
        1. 함수
            3) 정수를 전달받는다.
            4) 결과를 1로 초기화한다.
            5) 정수부터 1 까지 1씩 감소하며 반복한다. i에 저장한다.
                5-1) 결과는 결과 * i
            6) 결과를 리턴한다.
        
        2. 메인
            1) 정수를 입력받는다.
            2) 함수를 호출하여 돌려받은 값을 출력한다.
'''
# 함수 선언
def pac(num) :
    result = 1
    for i in range(num, 0, -1) :
        result = result * i
    return result

# 메인
num = int(input("정수를 입력하세요. : "))
print(f"{num}! = {pac(num)}")