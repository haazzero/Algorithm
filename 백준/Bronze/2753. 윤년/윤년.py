year = int(input()) # 첫 줄에 연도가 주어짐

# 윤년은 year이
# 4의 배수 and NOT 100의 배수
# 400의 배수
# --> % 했을 때 0으로 떨어져야함

# if문 윤년이면 1, 아니면 0을 출력
# elif의 중요성
if year % 4 == 0 and year % 100 != 0 :
    print("1")
elif year % 400 == 0 : 
    print("1")
else : 
    print("0")
