rest_list = []

for i in range(10):
    rest_list.append(int(input())%42)

count = 10
for j in range(0, 9):
    for k in range(j+1,10):
        if rest_list[j]==rest_list[k]:
            count-=1
            break

print(count)