''' 작성일: 2024년 5월 16 일
    작성자: 컴퓨터공학부 202495014 이현겸
    설명: 다음과 같은 튜플을 생성하고
          각 요소(숫자)가 튜플에 몇 개 있는지를 출력하시오.
          
    len(), count(), 0번지부터
    
    개수를 찾은 숫자는 리스트에 따로 저장한다.
    이미 찾슨 숫자는 또 개수를 찾을 필요가 없다.
'''
# 튜플 생성
num = (4,1,3,6,5,7,9,5,1,4,6,0,1,2,7,8,9)
print("생성된 튜플 : ", num)

num_list =[]

for i in range(10) :
    num_list.append(num.count(i))
    print(f"{i}의 개수 :", num_list[i])

'''
for i in range(len(num)) :
    if num[i] in num_list :
        continue
    else :
        print(num[i],"의 개수 : ", num.count(num[i]))
        num_list.append(num[i])

print()
num_list = []   # 다시 초기화

for i in range(len(num)) :
    if num[i] not in num_list :
        print(num[i],"의 개수 : ", num.count(num[i]))
        num_list.append(num[i])
'''