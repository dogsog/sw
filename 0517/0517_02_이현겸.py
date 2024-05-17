''' 작성일: 2024년 5월 17 일
    작성자: 컴퓨터공학부 202495014 이현겸
    설명: 5명의 학생 정보를 입력받는다.
          이름과 전화번호를 입력받는다.
'''
# 빈 딕셔너리 생성
phone = {}

for i in range(5) :
    # 이름을 입력받아 변수에 저장
    name = input(str(i+1) + "번 학생의 이름을 입력하시오. : ")
    # 전화번호 입력받아 변수에 저장
    phone_num = input(str(i+1) + "번 학생의 전화번호를 입력하시오. : ")
    
    # 딕셔너리에 이름과 전화번호 추가
    phone[name] = phone_num

print("학생 전화번호부가 완성되었습니다.")
print()

# 학생 정보 출력
# 이름 : 전화번호

for name, phone_num in phone.items() :
    print(name, ":", phone_num)

print()

# 학생 검색
# 학생 이름을 입력하면 해당 학생의 전화번호를 출력하시오.
# 만약 학생 이름이 없으면 "입력한 학생의 전화번호가 없습니다." 출력한다.
# 무한 반복합니다. 단, 0을 입력하면 종료합니다.

while True :
    name = input("검색할 학생 이름을 입력하세요. (0 : 종료): ")
    if name == '0' :
        print("프로그램을 종료합니다.")
        break
    else:
        if name in phone :
            print(name, ":", phone[name])
        else :
            print("입력한 학생의 전화번호가 없습니다.")