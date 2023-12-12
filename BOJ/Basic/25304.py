# 총 금액 
X = int(input())

# 물건의 종류의 수
N = int(input())

# 물건의 가격과 종류
total = 0
for i in range(N):
    a, b = map(int, input().split())
    total += a*b

if X == total:
    print('Yes')
else:
    print('No')