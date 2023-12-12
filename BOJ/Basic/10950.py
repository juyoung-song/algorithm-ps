T = int(input())
hap = []

for i in range(0, T):
    a, b = map(int, input().split())
    hap.append(a+b)

for i in range(0, T):
    print(hap[i])