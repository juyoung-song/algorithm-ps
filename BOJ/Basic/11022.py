T = int(input())

hap = []
for i in range(T):
    a, b = map(int, input().split())
    hap.append(a+b)
    print('Case #{0}: {1} + {2} = {3}'.format(i+1, a, b, hap[i]))
