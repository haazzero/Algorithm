word = input()

for i in range(len(word)): # len()으로 문자열의 길이만큼 반복
    if word[i].isupper():  # 만약 해당 문자가 대문자라면
        print(word[i].lower(), end='') # 소문자로 바꾸어 출력
    else: # 만약 해당 문자가 소문자라면
        print(word[i].upper(), end='') # 대문자로 바꾸어 출력