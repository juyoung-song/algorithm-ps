T = int(input())

hap = []
for i in range(T):
    a, b = map(int, input().split())
    hap.append(a+b)

for j in range(1, T+1):
    print("Case #{0}: {1}".format(j, hap[j-1]))