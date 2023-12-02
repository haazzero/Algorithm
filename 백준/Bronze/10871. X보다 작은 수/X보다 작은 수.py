N, X = map(int,input().split())     # 첫째줄에 N과 X가 주어짐
A = list(map(int, input().split())) # 둘째 줄에 수열 A를 이루는 정수 N개가 주어짐
for i in range(N) :
  if A[i] < X :                     # X보다 작은 수를 입력받은 순서대로
    print(A[i], end=" ")            # 공백으로 구분해 출력