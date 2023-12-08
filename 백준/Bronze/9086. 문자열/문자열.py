T = int(input())    # 테스트 케이스 개수
for i in range(T) :
    word = input()
    print(word.strip()[0]+word.strip()[-1]) #strip 메소드와 인덱스 활용