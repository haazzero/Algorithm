N = int(input())
L = list(map(int, input().split()))
V = int(input())

# count : 리스트 내장 메소드 count() 는 매개변수로 입력된 값이 리스트 안에 몇개 있는지 세어 반환
print(L.count(V))