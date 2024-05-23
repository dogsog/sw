''' 작성일: 2024년 5월 23 일
    작성자: 컴퓨터공학부 202495014 이현겸
    설명: for() 문을 이용하여 읽어오기
'''
print("== for 문을 이용하여 읽기 ==")

# with open 을 이용하여 읽기 모드로 파일객체 생성
with open("test2.txt", "r") as f :
    for line in f :  # for 문에 파일객체를 지정하여 한 줄씩 반복하여 읽어온다.
        print(line)

# with open 을 사용하면 f.close 를 쓸 필요없다.