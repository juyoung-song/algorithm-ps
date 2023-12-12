N = int(input())

num_list = []
num_list.extend(map(int, input().split()))

v = int(input())

count = 0
for i in range(N):
    if num_list[i]==v:
        count+=1

print(count)