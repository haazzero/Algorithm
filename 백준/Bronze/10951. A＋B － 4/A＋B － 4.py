# try - except
while True: #무한루프
    try :               
        a, b = map(int, input().split()) 
        print(a+b)  # 에러가 나지 않을 시(값이 있으면) a+b
    except :        # error 발생 시 실행시킬 문장
         break      # 반복문 탈출

