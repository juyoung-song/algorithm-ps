N, X = map(int, input().split())

num_list = []
num_list.extend(map(int, input().split()))

result_list = []
for i in range(len(num_list)):
    if num_list[i] < X:
        result_list.append(num_list[i])

for j in range(len(result_list)):
    print(result_list[j], end=' ')