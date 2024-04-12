''' 작성일: 2024년 4월 12 일
    작성자: 컴퓨터공학부 202495014 이현겸
    설명: 단을 입력받아 구구단을 출력하는 프로그램
          반복문 for
'''
dan = int(input("알고싶은 단을 입력하세요. : "))
print(f"{dan} 단 출력")

for su in range(1, 10) :
    print(f"{dan} * {su} = {dan * su}")