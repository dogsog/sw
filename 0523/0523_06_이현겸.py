''' 작성일: 2024년 5월 23 일
    작성자: 컴퓨터공학부 202495014 이현겸
    설명: readline() 메소드 사용법
'''
print("== readline() 메소드 이용하여 읽기 ==")

# readline() 메소드는 주로 while 반복문과 함께 사용

# with open 을 이용하여 읽기 모드로 파일객체 생성
with open("test2.txt", "r") as f :
    # while 문을 사용하여 무한 반복
    while True :
        line = f.readline()  # 한 줄씩 읽어와서 변수에 저장
        print(line)
        
        if line == '' :  # 읽어온 값이 없을 경우 반복을 벗어난다.
            break

# with open 을 사용하면 f.close 를 쓸 필요없다.