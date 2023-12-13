# 바구니 갯수, 실행 횟수
N, M = map(int, input().split())

# 바구니 list 초기화
basket = [k+1 for k in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    basket1 = basket[i-1:j]
    basket1.reverse()
    basket2 = basket[:i-1]
    basket3 = basket[j:]
    basket = basket2+basket1+basket3

for k in range(len(basket)):
    print(basket[k], end=' ')
