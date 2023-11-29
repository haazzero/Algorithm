x = int(input()) # 첫 줄에는 정수 x
y = int(input()) # 다음 줄에는 정수 y
# print(type(x),type(y)) # 데이터 타입 확인

# 점 (x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력
# 1 : +, + 
# 2 : -, +
# 3 : -, -
# 4 : +, -

# if문 논리 연산자
if x>0 and y>0 : 
    print("1")
if x<0 and y>0 : 
    print("2")
if x<0 and y<0 : 
    print("3")
if x>0 and y<0 :
    print("4")            
