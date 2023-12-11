n, m = map(int, input().split()) # n, m을 입력받음
a = [] # a를 빈 리스트로 초기화
b = [] # b를 빈 리스트로 초기화
for i in range(n): # n번 반복
    a.append(list(map(int, input().split()))) # a에 리스트로 입력받은 값을 추가
for i in range(n): # n번 반복
    b.append(list(map(int, input().split()))) # b에 리스트로 입력받은 값을 추가
for i in range(n): # n번 반복
    for j in range(m): # m번 반복
        print(a[i][j] + b[i][j], end = " ") # a와 b의 각각의 값을 더한 값을 출력
    print() # 줄바꿈