while True:               #무한 반복
    a, b = map(int, input().split())
    if a == 0 and b == 0: # a와 b가 모두 0이면
        break             # 반복문을 빠져나옴
    else:                 #if에 해당하지 않으면
        print(a+b)