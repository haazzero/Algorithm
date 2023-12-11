word = input()
for i in range(0,len(word),10) : #반복문으로 10씩 증가
    print(word[i:i+10]) #문자열을 10단위로 끊어줌