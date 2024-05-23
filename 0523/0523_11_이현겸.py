''' 작성일: 2024년 5월 23 일
    작성자: 컴퓨터공학부 202495014 이현겸
    설명: 학생 점수의 평균을 출력하시오.
    
    [알고리즘]
        1. 학생 이름과 성적을 읽어올 객체 만들기
        2. 반복하면서 내용 읽어오기
            2-1. 점수에 대해 평균을 계산한다.
                 (합계 계산하고, 평균을 계산하여 출력한다.)
                 홍길동의 평균 성적 : 00 점
    
    with open()
    
    읽기 모드 => r
    파일에 읽기 = readline()  => while True 사용
'''
with open("student.txt","r") as f :

    while True :
        student = f.readline()
        
        if student == '' :
            break
        
        # 빈칸을 기준으로 리스트 객체 반환
        studentList = student.split()
        
        # 첫번째 항목을 name 변수에 저장
        name = studentList[0]
        
        # 1번지부터 3번지까지 
        sum = 0
        for i in range(1, 4) :
            sum = sum + int(studentList[i])
        
        avg = sum / 3
        
        print(f"{name}의 평균 성적 : {avg:.2f}점")
