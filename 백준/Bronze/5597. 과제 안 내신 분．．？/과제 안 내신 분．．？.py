numbers = list(range(1,31)) #1~30까지 리스트 숫자

for i in range(28) : # 28번 반복
  numbers.remove(int(input())) # 입력받은 숫자를 리스트에서 제거

for i in numbers : # 리스트에 남은 숫자 출력
  print(i)