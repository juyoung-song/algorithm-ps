import sys

T = int(input())

hap = []
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    hap.append(a+b)

for i in range(T):
    print(hap[i])