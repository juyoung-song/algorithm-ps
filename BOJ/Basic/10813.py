# 바구니 갯수, 교환 횟수
N, M = map(int, input().split())

# 바구니 리스트 초기화
basket = [k+1 for k in range(N)]

# 공 교환
for l in range(M):
    i, j = map(int, input().split())
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp

# 결과 출력
for m in range(N):
    print(basket[m], end=' ')
    
