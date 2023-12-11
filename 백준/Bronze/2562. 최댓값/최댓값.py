num_list = []
for i in range(9) :
    num_list.append(int(input()))  			## num_list 안에 입력된 값들 차례대로 넣기

print(max(num_list))
print(num_list.index(max(num_list))+1) #index는 0부터 시작하기에 +1