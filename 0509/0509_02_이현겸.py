''' 작성일: 2024년 5월 9 일
    작성자: 컴퓨터공학부 202495014 이현겸
    설명: 사용자로부터 입력받은 문장에서 스페이스바가 몇 개인지 출력하시오.
          그리고 스페이스바를 없앤 문장을 출력하시오.
    
    [알고리즘]
        1. 문장을 입력받는다.
        2. 스페이스가 몇 개인지 출력한다.
        3. 스페이스를 삭제한 문장을 출력한다.
'''
text1 = input("문장을 입력하세요. : ")
print("입력받은 문장에서 스페이스바의 수는", text1.count(' '))
print("문장에서 스페이스바 삭제 : ", text1.replace(' ', ''))