''' 작성일: 2024년 4월 4 일
    작성자: 컴퓨터공학부 202495014 이현겸
    설명: 점수를 입력받아 학점을 출력하시오.
    90~100 : A학점
    80~89 : B학점
    70~79 : C학점
    60~69 : D학점
    0~59 : F학점
    
[문제분석]
    필요한 변수 : score(점수)
        점수는 90점에서 100점 사이다.
        => 1) 90 <= score <= 100
        => 2) (score <= 90) and (score <= 100)
        F 학점은 나머지로 처리한다.
[알고리즘]
1. 점수를 입력받는다.
2. 만약 점수가 90점에서 100점 사이이면
    2-1. A학점
3. 아니고 점수가 90점에서 100점 사이이면
    3-1. B학점
4. 아니고 점수가 90점에서 100점 사이이면
    4-1. C학점
5. 아니고 점수가 90점에서 100점 사이이면
    5-1. D학점
6. 아니라면
    6-1. 잘못된 점수

'''

score = int(input("점수를 입력하시오. :"))

if 90 <= score <= 100 :
    print(f"{score}점은 A학점입니다.")
elif 80 <= score <= 89 :
    print(f"{score}점은 B학점입니다.")
elif 70 <= score <= 79 :
    print(f"{score}점은 C학점입니다.")
elif 60 <= score <= 69 :
    print(f"{score}점은 D학점입니다.")
elif 0 <= score <= 59 :
    print(f"{score}점은 F학점입니다.")
else :
    print("점수를 잘못 입력했습니다.")