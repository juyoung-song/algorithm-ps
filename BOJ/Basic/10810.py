N, M = map(int, input().split())

basket = [0 for i in range(N)]

for j in range(M):
    start, end, ball = map(int, input().split())
    for k in range(start-1, end):
        basket[k]=ball

for l in range(0, N):
    print(basket[l], end=" ")