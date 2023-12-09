# 검증수는 고유번호의 처음 5자리에 들어가는 5개의 숫자를 
# 각각 제곱한 수의 합을 10으로 나눈 나머지
A, B, C, D, E = map(int, input().split())
x = 2
print((pow(A,x)+pow(B,x)+pow(C,x)+pow(D,x)+pow(E,x)) % 10)

# pow(a,b) : a의 b 제곱을 계산하여 반환
# a % b : a를 b로 나누었을 때의 나머지 반환